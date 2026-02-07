# MLOPS Lab Project

This repository contains the code for multiple MLOPS labs, structured according to standard practices.

## Folder Structure Mapping

The folder structure has been consolidated. Here is where you can find the files for each Lab:

| Lab | Description | Folder / File Location |
| :--- | :--- | :--- |
| **Lab 2** | **Model Training** | `src/train.py`<br>`dataset/winequality-red.csv`<br>`models/` (Generated outputs) |
| **Lab 3** | **Deployment (Docker)** | `deployment/DataFrame`<br>`deployment/app/` |
| **Lab 4** | **Jenkins Setup** | *Manual Server Setup* (See `walkthrough.md`) |
| **Lab 5** | **Pipeline & Testing** | `Jenkinsfile`<br>`tests/test_train.py`<br>`tests/quality_check.py` |

## How to Run

### Lab 2: Train Model
```bash
python src/train.py
```

### Lab 3: Build Docker Image
```bash
cd deployment
docker build -t my-python-app .
```

### Lab 5: Run Tests
```bash
pytest tests/
```
