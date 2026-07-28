import pandas as pd
import joblib

with open('model/insurance_premium_model.pkl', 'rb') as f:
    model = joblib.load(f)

class_labels = model.classes_.tolist()

def get_prediction(data: dict):

    input_df = pd.DataFrame([data])

    prediction_class = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    # Create mapping: {class_name: probability}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": prediction_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
        }