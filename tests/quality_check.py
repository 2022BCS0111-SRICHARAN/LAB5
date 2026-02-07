import json
import os
import sys

# Define thresholds
MSE_THRESHOLD = 0.5
R2_THRESHOLD = 0.2

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")
RESULTS_PATH = os.path.join(MODELS_DIR, "results.json")

def check_quality():
    if not os.path.exists(RESULTS_PATH):
        print(f"Error: Results file not found at {RESULTS_PATH}")
        sys.exit(1)

    with open(RESULTS_PATH, "r") as f:
        results = json.load(f)

    mse = results.get("MSE")
    r2 = results.get("R2")

    print(f"Checking Quality Gates...")
    print(f"MSE: {mse} (Threshold: < {MSE_THRESHOLD})")
    print(f"R2: {r2} (Threshold: > {R2_THRESHOLD})")

    if mse > MSE_THRESHOLD:
        print("Failure: MSE exceeds threshold.")
        sys.exit(1)
    
    if r2 < R2_THRESHOLD:
        print("Failure: R2 score is below threshold.")
        sys.exit(1)

    print("Success: Quality gates passed.")
    sys.exit(0)

if __name__ == "__main__":
    check_quality()
