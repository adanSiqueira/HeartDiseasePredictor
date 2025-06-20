from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import xgboost as xgb
import pandas as pd
import joblib

heart_disease = fetch_ucirepo(id=45)
df = pd.DataFrame(heart_disease['data']['features'])
df['ill'] = heart_disease['data']['targets']
df['ill'] = (df['ill'] > 0).astype(int)

X = df.drop('ill', axis = 1)
y = df['ill']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state = 432)
model = xgb.XGBClassifier(objective = 'binary:logistic', random_state = 432)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

if __name__ == "__main__":
    print(classification_report(y_test, y_pred))
    joblib.dump(model, 'modelHD.pkl')