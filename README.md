# Insurance-Premium-Prediction-API
This project builds an insurance premium prediction system using FastAPI for the backend API and Streamlit for an interactive user interface. It accepts user details such as age, weight, height, income, smoker status, city, and occupation to predict the premium category with model-based results.

# Insurance Premium Prediction

This project is a simple machine learning-based web application that predicts an insurance premium category using a FastAPI backend and a Streamlit frontend.

## Overview

The application accepts user input such as:
- BMI
- Age group
- Lifestyle risk
- City tier
- Income
- Occupation

These values are sent to the FastAPI backend, where the prediction logic is applied and the result is returned to the user.

## Project Structure

```text
insaurance_premium_prediction/
├── app.py
├── frontend.py
├── schema/
│   ├── user_input.py
│   └── prediction_response_parser.py
├── model/
│   └── predict.py
└── README.md
```

## Technologies Used

- Python
- FastAPI
- Streamlit
- Pydantic
- Requests

## Features

- FastAPI backend with prediction endpoint
- Streamlit web interface for user input
- Response model validation using Pydantic
- Simple and lightweight architecture for local development

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn streamlit requests pydantic
```

If your model uses additional libraries such as scikit-learn, joblib, or pandas, install them as needed.

## Run the Backend

From the project folder, run:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:

- `http://localhost:8000/about`
- `http://localhost:8000/health`
- `http://localhost:8000/docs`

## Run the Frontend

Open a new terminal and run:

```bash
streamlit run frontend.py
```

Then open:

```text
http://localhost:8501
```

## API Endpoint

### POST /predict

Request body example:

```json
{
  "bmi": 24.1,
  "age_group": "adult",
  "lifestyle_risk": "moderate",
  "city_tier": 2,
  "income_lpa": 12.5,
  "occupation": "private_job"
}
```

Example response:

```json
{
  "response": {
    "predicted_category": "medium",
    "confidence": 0.81,
    "class_probabilities": {
      "low": 0.05,
      "medium": 0.81,
      "high": 0.14
    }
  }
}
```

## Notes

- The request schema is defined in `schema/user_input.py`.
- The prediction logic is implemented in `model/predict.py`.
- The frontend sends requests to the FastAPI backend at `http://localhost:8000/predict`.

## Summary

This project is a basic end-to-end example of combining:
- a machine learning prediction model
- a FastAPI backend
- a Streamlit frontend

for local deployment and testing.
```

If you want, I can also make this README shorter and more professional for GitHub.If you want, I can also make this README shorter and more professional for GitHub.
