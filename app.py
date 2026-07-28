from fastapi import (
    FastAPI, 
    Path, 
    HTTPException, 
    Query,
    responses
)
from schema.user_input import UserInput
from schema.prediction_response_parser import PredictionResponse
from model.predict import model, get_prediction

app = FastAPI()
    
# <-----! FastAPI Routes !----->
# Human Readable API Documentation is available at http://localhost:8000/about
@app.get('/about')
def about():
    return responses.JSONResponse(status_code=200, content={
        'app_name': 'Insurance Premium Prediction API',
        'version': '1.0.0',
        'description': 'This API predicts the insurance premium category based on user input data.',
        'is_model_loaded': model is not None
    })

# Machine or Cloud Readable API Documentation is available at http://localhost:8000/health
@app.get('/health')
def health_check():
    return responses.JSONResponse(status_code=200, content={
        'status': 'ok',
        'message': 'The API is running and ready to accept requests.',
        'last_updated': '2024-06-01T12:00:00Z',
        'prediction_model': 'insurance_premium_model.pkl',
        'model_version': '1.0.0',
        'ML_model_loaded': model is not None
    })

@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:
        prediction = get_prediction(user_input)

        return responses.JSONResponse(status_code=200, content={'response': prediction})
    except Exception as e:
        raise responses.JSONResponse(status_code=500, detail=f"Prediction failed: {str(e)}")