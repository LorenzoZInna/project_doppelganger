from fastapi import FastAPI
import pickle
app = FastAPI ()

@app.get("/")

def root():
    return{'greeting':"gooodbye"}

@app.get("/predict")
def predict ():
    print("hello world predict")

    with open ('models/best_model.pkl','rb') as file:
        model = pickle.load(file)

    prediction = model.predict()

    return {"prediction":prediction}
