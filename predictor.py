import pickle
model=pickle.load(open("model.pkl","rb"))
def crop(nitrogen,phosphorus,potassium,temperature,humidity,rainfall):
    ans=model.predict([[nitrogen,phosphorus,potassium,temperature,humidity,rainfall]])
    return ans