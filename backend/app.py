from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Arch-AI Cost Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BuildingFeatures(BaseModel):
    total_area_sqft: int
    num_floors: int
    num_bedrooms: int
    num_bathrooms: int
    city: str
    building_type: str
    finish_quality: str

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Welcome to the Arch-AI Prediction API!"}

@app.post("/predict")
def predict_cost(features: BuildingFeatures):
    try:
        base_cost_per_sqft = 2000
        city_multipliers = {
            'Bhubaneswar': 1.0,
            'Delhi': 2.0,
            'Mumbai': 2.5,
            'Bengaluru': 1.8
        }
        quality_multipliers = {
            'Basic': 0.8,
            'Standard': 1.0,
            'Premium': 1.5
        }
        
        city_mult = city_multipliers.get(features.city, 1.0)
        quality_mult = quality_multipliers.get(features.finish_quality, 1.0)
        estimated_cost = (features.total_area_sqft * base_cost_per_sqft * 
                         city_mult * quality_mult * features.num_floors)
        
        return {"estimated_cost_inr": round(estimated_cost)}
    
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}", "estimated_cost_inr": 5000000}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
