from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline, make_pipeline
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
import xgboost as xgb
import joblib

heart_disease = fetch_ucirepo(id=45)
df = pd.DataFrame(heart_disease['data']['features'])
df['ill'] = heart_disease['data']['targets']
df['ill'] = (df['ill'] > 0).astype(int)
df = df.dropna()

def find_clinical_outliers(df):
    condition_trestbps = df['trestbps'] >= 168
    condition_chol = df['chol'] >= 300
    super_high_chol = df['chol'] >= 500
    condition_oldpeak = df['oldpeak'] >= 2.5
    super_high_oldpeak = df['oldpeak'] >= 4
    condition_not_ill = df['ill'] == 0
    #Count how many risk conditions each patient satisfies
    risk_conditions = (condition_trestbps.astype(int) +
                       condition_chol.astype(int) +
                       condition_oldpeak.astype(int) +
                       super_high_chol.astype(int) +
                       super_high_oldpeak.astype(int))
    #Flag as outliers: patients with 2 or more conditions and labeled as not ill
    outliers = df[(risk_conditions >= 2) & condition_not_ill]
    return outliers

df.drop(find_clinical_outliers(df).index, inplace=True)

X = df.drop('ill', axis = 1)
y = df['ill']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = y, test_size = 0.2, random_state = 432)

#LogisticRegression Training
space_lr = [
    {
        'logisticregression__solver': Categorical(['lbfgs', 'newton-cg']),
        'logisticregression__penalty': Categorical(['l2']),
        'logisticregression__C': Real(0.001, 10, prior='log-uniform'),
        'logisticregression__max_iter': Integer(100, 300)
    },
    {
        'logisticregression__solver': Categorical(['liblinear']),
        'logisticregression__penalty': Categorical(['l1', 'l2']),
        'logisticregression__C': Real(0.001, 10, prior='log-uniform'),
        'logisticregression__max_iter': Integer(100, 300)
    }
]

pipe_lr = make_pipeline(StandardScaler(), LogisticRegression())

opt_lr = BayesSearchCV(
    estimator=pipe_lr,
    search_spaces=space_lr,
    n_iter=25,
    scoring='recall',
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
    n_jobs=-1,
    random_state=42
)
opt_lr.fit(X_train, y_train)
model_lr = opt_lr.best_estimator_

#RandomForest Training
space_rf = {
    'randomforestclassifier__n_estimators': Integer(50, 300),
    'randomforestclassifier__max_depth': Integer(3, 20),
    'randomforestclassifier__min_samples_split': Integer(2, 10),
    'randomforestclassifier__min_samples_leaf': Integer(1, 5),
    'randomforestclassifier__bootstrap': Categorical([True, False])
}

pipe_rf = make_pipeline(RandomForestClassifier(random_state=42))

opt_rf = BayesSearchCV(
    estimator=pipe_rf,
    search_spaces=space_rf,
    n_iter=25,
    scoring='recall',
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
    n_jobs=-1,
    random_state=42
)
opt_rf.fit(X_train, y_train)
model_rf = opt_rf.best_estimator_

#XGBoost Training
pipe_xgb = Pipeline([
    ('xgb', xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42))
])

search_space = {
    'xgb__n_estimators': Integer(50, 300),
    'xgb__max_depth': Integer(2, 10),
    'xgb__learning_rate': Real(0.01, 0.3, prior='log-uniform'),
    'xgb__subsample': Real(0.5, 1.0),
    'xgb__colsample_bytree': Real(0.5, 1.0),
    'xgb__gamma': Real(0, 5),
    'xgb__reg_lambda': Real(0.1, 10, prior='log-uniform'),
    'xgb__reg_alpha': Real(0.1, 10, prior='log-uniform')
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

opt_xgb = BayesSearchCV(
    estimator=pipe_xgb,
    search_spaces=search_space,
    n_iter=50,  # pode aumentar para melhor resultado
    cv=cv,
    scoring='recall',  # foco no recall da classe positiva (classe 1)
    n_jobs=-1,
    verbose=0,
    random_state=42
)
opt_xgb.fit(X_train, y_train)
model_xgb = opt_xgb.best_estimator_

#VotingSoft Ensemble
model_soft_voting = VotingClassifier(estimators = [('lr', model_lr), ('rf', model_rf), ('xgb', model_xgb)], voting = 'soft')
model_soft_voting.fit(X_train, y_train)

joblib.dump(model_soft_voting, 'model_HD.pkl')