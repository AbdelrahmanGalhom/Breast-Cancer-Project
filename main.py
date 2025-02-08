from fastapi import FastAPI, HTTPException
from src.config import APP_NAME, VERSION, forest_model, xgboost_model
from src.inference import predict_new
from src.request import RequestData

# Initialize an app
app = FastAPI(title=APP_NAME, version=VERSION)


@app.get('/', tags=['Healthy'], description="Healthy Check")
async def home():
    return {
        "message": f"Welcome to {APP_NAME} API v{VERSION}"
    }
    
    
@app.post("/predict/forest", tags=['Models'], description="Prediction of Breast Cancer using Random Forest")
def predict_forest(data: RequestData):
    
    try:
        result = predict_new(data=data, model=forest_model)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in prediction using Random Forest {str(e)}")
    
    
@app.post("/predict/xgboost", tags=['Models'], description="Prediction of Breast Cancer using XGBoost")
def predict_xgboost(data: RequestData):
    
    try:
        result = predict_new(data=data, model=xgboost_model)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in prediction using XGBoost {str(e)}")
    
