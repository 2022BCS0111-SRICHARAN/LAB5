import os
import pytest
import pandas as pd
import joblib
import json

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")
MODEL_PATH = os.path.join(MODELS_DIR, "model.pkl")
RESULTS_PATH = os.path.join(MODELS_DIR, "results.json")

def test_model_exists():
    """Test if model.pkl is generated."""
    assert os.path.exists(MODEL_PATH), "Model file model.pkl not found."

def test_results_exist():
    """Test if results.json is generated."""
    assert os.path.exists(RESULTS_PATH), "Results file results.json not found."

def test_model_loading():
    """Test if the model can be loaded."""
    try:
        model = joblib.load(MODEL_PATH)
    except Exception as e:
        pytest.fail(f"Failed to load model: {e}")
    assert model is not None, "Loaded model is None."

def test_metrics_content():
    """Test if results.json contains valid metrics."""
    with open(RESULTS_PATH, "r") as f:
        results = json.load(f)
    
    assert "MSE" in results, "MSE metric not found in results.json"
    assert "R2" in results, "R2 metric not found in results.json"
    assert results["MSE"] > 0, "MSE should be positive."
    assert results["R2"] <= 1.0, "R2 score should be <= 1.0"
