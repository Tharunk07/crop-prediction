import pandas as pd
import pickle
df=pd.read_csv("Crop_recommendation.csv")
df.head()
X=df[['N','P','K','temperature','humidity','rainfall']]
Y=df['label']
print(X)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
import lightgbm as lgb
model = lgb.LGBMClassifier()
model.fit(X_train, Y_train)
pickle.dump(model,open("model.pkl","wb"))
model.predict(X_test)
print(model.score(X_test,Y_test))