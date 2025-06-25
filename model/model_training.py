from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split, StratifiedKFold
import pandas as pd
import joblib
from skopt.space import Categorical, Integer
from skopt import BayesSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

heart_disease = fetch_ucirepo(id=45)
df = pd.DataFrame(heart_disease['data']['features'])
df['ill'] = heart_disease['data']['targets']
df['ill'] = (df['ill'] > 0).astype(int)

X = df.drop('ill', axis = 1)
y = df['ill']

df_notnull_values = df.dropna()
X_train_nn, X_test_nn, y_train_nn, y_test_nn = train_test_split(
    df_notnull_values.drop('ill', axis = 1),
    df_notnull_values['ill'], test_size = 0.2,
    stratify = df_notnull_values['ill'],
    random_state = 432)

max_iter = Integer(100,300)
c = Categorical([0.001, 0.01, 0.1, 1, 10])

space_lr = [
    {'logisticregression__solver' : Categorical(['newton-cg', 'lbfgs']),
      'logisticregression__penalty' : Categorical(['l2']),
      'logisticregression__max_iter' : max_iter,
       'logisticregression__C' : c},
    {'logisticregression__solver' : Categorical(['liblinear']),
      'logisticregression__penalty' : Categorical(['l1', 'l2']),
      'logisticregression__max_iter' : max_iter,
      'logisticregression__C' : c},
]

inner_cv = StratifiedKFold(shuffle = True, random_state = 42)

outter_cv = StratifiedKFold(n_splits = 3, shuffle = True, random_state = 42)

opt_lr = BayesSearchCV(estimator = make_pipeline(StandardScaler(), LogisticRegression()),
              search_spaces = space_lr,
              n_iter=25,
              scoring= 'recall',
              n_jobs=-1,
              cv= inner_cv,
              random_state= 42)

opt_lr.fit(X_train_nn, y_train_nn)

joblib.dump(opt_lr, 'opt_HD.pkl')