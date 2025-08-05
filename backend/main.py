import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI app
app = FastAPI(title="Arch-AI Cost Prediction API")

# Allow Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Model for Input Validation
class BuildingFeatures(BaseModel):
    total_area_sqft: int
    num_floors: int
    num_bedrooms: int
    num_bathrooms: int
    city: str
    building_type: str
    finish_quality: str

# Load the trained model from the file (we'll create a dummy model for now)
try:
    model = joblib.load('cost_model.joblib')
except FileNotFoundError:
    # Create a dummy model if the actual model doesn't exist
    from sklearn.ensemble import RandomForestRegressor
    import numpy as np
    model = RandomForestRegressor(n_estimators=10, random_state=42)
    # Create dummy training data
    X_dummy = np.random.rand(100, 7)
    y_dummy = np.random.rand(100) * 10000000  # Random costs between 0-1 crore
    model.fit(X_dummy, y_dummy)

@app.get("/")
def read_root():
    """A simple endpoint to check if the API is running."""
    return {"status": "ok", "message": "Welcome to the Arch-AI Prediction API!"}

@app.post("/predict")
def predict_cost(features: BuildingFeatures):
    """Accepts building features and returns a predicted construction cost."""
    try:
        # Convert the input data into a pandas DataFrame
        input_data = {
            'total_area_sqft': [features.total_area_sqft],
            'num_floors': [features.num_floors],
            'num_bedrooms': [features.num_bedrooms],
            'num_bathrooms': [features.num_bathrooms],
            'city': [features.city],
            'building_type': [features.building_type],
            'finish_quality': [features.finish_quality]
        }
        
        # Simple cost calculation based on area and quality multipliers
        base_cost_per_sqft = 2000  # Base cost per sq ft in INR
        
        # City multipliers
        city_multipliers = {
            'Bhubaneswar': 1.0,
            'Delhi': 2.0,
            'Mumbai': 2.5,
            'Bengaluru': 1.8
        }
        
        # Quality multipliers
        quality_multipliers = {
            'Basic': 0.8,
            'Standard': 1.0,
            'Premium': 1.5
        }
        
        city_mult = city_multipliers.get(features.city, 1.0)
        quality_mult = quality_multipliers.get(features.finish_quality, 1.0)
        
        # Calculate estimated cost
        estimated_cost = (features.total_area_sqft * base_cost_per_sqft * 
                         city_mult * quality_mult * features.num_floors)
        
        return {"estimated_cost_inr": round(estimated_cost)}
    
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}", "estimated_cost_inr": 5000000}
