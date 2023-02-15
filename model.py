import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib

seed = 42

iris_df = pd.read_csv("data/iris.csv")
iris_df.sample(frac=1,random_state = seed)

X = iris_df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y = iris_df[['Species']]


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=seed,stratify=y)
clf = RandomForestClassifier(n_estimators = 100)

clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy: {accuracy}")

joblib.dump(clf,"output_model/rf_model.sav")