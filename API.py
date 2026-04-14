import pickle
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 1. Load the Model, Encoders, and Features

try:
    with open("fraud_detection_model.pkl", "rb") as f:
        saved_data = pickle.load(f)
    
    model = saved_data["model"]
    encoders = saved_data["encoders"]
    feature_columns = saved_data["features"]
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")

# 2. Initialize FastAPI App

app = FastAPI(title="Vehicle Insurance Fraud Detection API")

# 3. Define the Input Data Schema using Pydantic

class ClaimData(BaseModel):
    Month: str
    WeekOfMonth: int
    DayOfWeek: str
    Make: str
    AccidentArea: str
    DayOfWeekClaimed: str
    MonthClaimed: str
    WeekOfMonthClaimed: int
    Sex: str
    MaritalStatus: str
    Age: int
    Fault: str
    PolicyType: str
    VehicleCategory: str
    VehiclePrice: str
    Deductible: int
    DriverRating: int
    Days_Policy_Accident: str 
    Days_Policy_Claim: str
    PastNumberOfClaims: str
    AgeOfVehicle: str
    AgeOfPolicyHolder: str
    PoliceReportFiled: str
    WitnessPresent: str
    AgentType: str
    NumberOfSuppliments: str
    AddressChange_Claim: str
    NumberOfCars: str
    Year: int
    BasePolicy: str

# 4. Create the Prediction Endpoint

@app.post("/predict")
def predict_fraud(data: ClaimData):
    try:
        input_dict = data.dict()
        df_input = pd.DataFrame([input_dict])
        
        rename_mapping = {
            "Days_Policy_Accident": "Days:Policy-Accident",
            "Days_Policy_Claim": "Days:Policy-Claim",
            "AddressChange_Claim": "AddressChange-Claim"
        }
        df_input = df_input.rename(columns=rename_mapping)

        for col, le in encoders.items():
            if col in df_input.columns:
                try:
                    df_input[col] = le.transform(df_input[col])
                except ValueError:
                    raise HTTPException(status_code=400, detail=f"Unrecognized category in column: {col}")

        df_input = df_input[feature_columns]

        prediction = model.predict(df_input)
        probability = model.predict_proba(df_input)[0][1] # Probability of Fraud

        result = "Fraud" if prediction[0] == 1 else "Not Fraud"
        
        return {
            "prediction": result,
            "fraud_probability_percentage": round(float(probability) * 100, 2)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "Fraud Detection API is Up and Running!"}