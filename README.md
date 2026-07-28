# Insurance Premium Prediction API & Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Architecture Overview

An end-to-end machine learning system for classifying insurance risk and predicting premium tiers. Built with **FastAPI** for high-performance RESTful inference and **Streamlit** for real-time interactive user assessments.

```

```
              ┌──────────────────┐
              │ Streamlit Client │
              └────────┬─────────┘
                       │ (HTTP POST /predict)
                       ▼
              ┌──────────────────┐
              │  FastAPI Server  │
              └────────┬─────────┘
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼

```

┌─────────────────────┐     ┌─────────────────────┐
│ Pydantic Validation │     │   Inference Engine  │
│ (schema/user_input) │     │   (model/predict)   │
└─────────────────────┘     └─────────────────────┘

```

---

## Directory Layout

```text
.
├── app.py                      # FastAPI application entry point
├── frontend.py                 # Streamlit dashboard interface
├── model/
│   └── predict.py              # ML model wrapper & inference pipeline
├── schema/
│   ├── user_input.py           # Request payload schema (Pydantic)
│   └── prediction_response_parser.py  # Output response formatting
├── requirements.txt            # Project dependencies
└── README.md

```

---

## Getting Started

### Prerequisites

* Python `3.9` or higher
* `pip` / `venv`

### Setup Environment

1. **Clone the repository:**
```bash
git clone [https://github.com/PrashantMali07/insurance-premium-prediction.git](https://github.com/PrashantMali07/insurance-premium-prediction.git)
cd insurance-premium-prediction

```


2. **Create and activate a virtual environment:**
* **Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate

```


* **Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

```




3. **Install dependencies:**
```bash
pip install --upgrade pip
pip install -r requirements.txt

```



---

## Running the Application

### 1. Launch the Backend API

Start the FastAPI server on port `8000`:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000

```

* **Swagger UI Documentation:** `http://localhost:8000/docs`
* **ReDoc Documentation:** `http://localhost:8000/redoc`
* **Health Check:** `http://localhost:8000/health`

### 2. Launch the Frontend Dashboard

In a separate terminal tab, start the Streamlit service:

```bash
streamlit run frontend.py

```

* **Web Dashboard:** `http://localhost:8501`

---

## API Reference

### `POST /predict`

Calculates insurance risk tier and class probabilities based on user metrics.

#### Request Body

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

#### Response (`200 OK`)

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
