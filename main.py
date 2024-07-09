from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Define the paths
model_path = os.path.join('models', 'model.pkl')
scaler_path = os.path.join('models', 'scaler.pkl')

# Load the model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Define the FastAPI app
app = FastAPI()

# Define the input data model
class CustomerData(BaseModel):
    credit_score: float
    country: str
    gender: str
    age: int
    tenure: int
    balance: float
    products_number: int
    credit_card: int
    active_member: int
    estimated_salary: float

# Encode categorical variables
def encode_features(data):
    country_dict = {"France": 0, "Germany": 1, "Spain": 2}
    gender_dict = {"Female": 0, "Male": 1}
    
    data['country'] = country_dict.get(data['country'], -1)
    data['gender'] = gender_dict.get(data['gender'], -1)
    
    return data

# Prediction endpoint
@app.post("/predict")
def predict_churn(data: CustomerData):
    try:
        data_dict = data.dict()
        data_dict = encode_features(data_dict)
        
        # Prepare the feature array for prediction
        features = np.array([[
            data_dict['credit_score'],
            data_dict['country'],
            data_dict['gender'],
            data_dict['age'],
            data_dict['tenure'],
            data_dict['balance'],
            data_dict['products_number'],
            data_dict['credit_card'],
            data_dict['active_member'],
            data_dict['estimated_salary']
        ]])
        
        # Scale numerical features
        features[:, [0, 3, 4, 5, 6, 9]] = scaler.transform(features[:, [0, 3, 4, 5, 6, 9]])
        
        # Predict churn
        prediction = model.predict(features)
        return {"churn": bool(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
