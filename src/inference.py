import pandas as pd

from .request import RequestData

def predict_new(data: RequestData, model):
    
    # To DF
    df = pd.DataFrame([data.model_dump()])
    
    # predict
    y_pred = model.predict(df)
    y_prob = model.predict_proba(df)

    return {
        "Cancer prediction": bool(y_pred[0]),
        "Malignant Probability": float(y_prob[0][1])
    }  


