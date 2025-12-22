# End-to-End Data Science Pipeline Project

## Overview

This project demonstrates a complete end-to-end data science pipeline, starting from data ingestion and preprocessing to model training, experiment tracking, and model versioning.  
The pipeline is designed with industry best practices such as modular code structure, logging, exception handling, experiment tracking, and data versioning.

The project runs locally on the developer’s machine while leveraging DagsHub, MLflow, and DVC to track experiments, manage data versions, and store model history.

---

## Project Architecture

The project follows a modular and scalable structure:

Data-Science-Pipe-Line/
├─ README.md
├─ requirements.txt
├─ setup.py
├─ environment.yml          # optional (conda)
├─ .gitignore
├─ app.py
├─ artifact/                # generated artifacts: raw/train/test csvs, models, preprocessors
├─ logs/
├─ src/
│  └─ datascienceproject/
│     ├─ components/
│     │  ├─ data_ingestion.py
│     │  ├─ data_transformation.py
│     │  └─ model_trainer.py
│     ├─ pipelines/
│     │  └─ (pipeline definition files)
│     ├─ utils.py
│     ├─ logger.py
│     ├─ exception.py
│     └─ __init__.py
├─ notebooks/
│  └─ (optional exploratory / demo notebooks)
├─ data/
│  ├─ raw/
│  └─ processed/
└─ dvc.yaml / .dvc/          # if using DVC

---

## Pipeline Flow

The pipeline is divided into the following stages:

### 1. Data Ingestion
- Reads raw student performance data.
- Splits the dataset into training and testing sets.
- Stores raw, train, and test data as CSV files in the `artifact/` directory.
- Although PostgreSQL connectivity is implemented, the current execution uses CSV data for development and testing.

---

### 2. Data Transformation
- Handles missing values using appropriate imputation strategies.
- Separates numerical and categorical features.
- Applies:
  - Median imputation and standard scaling for numerical features.
  - Mode imputation, one-hot encoding, and scaling for categorical features.
- Uses `ColumnTransformer` and `Pipeline` for clean preprocessing.
- Saves the fitted preprocessing object as `preprocessor.pkl`.

---

### 3. Model Training
- Trains multiple regression models including:
  - Linear Regression
  - Random Forest
  - Decision Tree
  - Gradient Boosting
  - XGBoost
  - CatBoost
  - AdaBoost
- Performs hyperparameter tuning using `GridSearchCV`.
- Evaluates models using R² score, RMSE, and MAE.
- Selects the best-performing model based on evaluation metrics.
- Saves the trained model as `model.pkl`.

---

## Experiment Tracking with MLflow and DagsHub

To track experiments and avoid losing model history, MLflow is integrated with DagsHub.

### How it works
- The pipeline runs locally on the machine.
- MLflow logs:
  - Model parameters
  - Evaluation metrics
  - Trained model artifacts
- DagsHub stores and visualizes all experiment runs for this repository.

### Initialization
MLflow tracking is initialized once at the application entry point:

python
import dagshub
dagshub.init(
    repo_owner="samuelrajgarikimukku",
    repo_name="Data-Science-Pipe-Line",
    mlflow=True
) 

## Logged Information

For each training run, MLflow logs the following:

- Model parameters (hyperparameters)
- Metrics (R², RMSE, MAE)
- Model artifacts
- Run metadata (timestamp, run ID)

All runs are isolated to this repository and do not interfere with other projects.

---

## Model Registry and Versioning

MLflow’s **Model Registry** is used to version trained models.

- Each training run can register a new model version
- Older high-performing models remain accessible
- Models can be promoted or rolled back without retraining

---

### Example: Load a Previous Model Version

import mlflow

model = mlflow.sklearn.load_model(
    "models:/Linear Regression/1"
)

This allows restoring a previously better-performing model even if newer experiments perform worse.

---

## Data Versioning with DVC

DVC is used to track large data files instead of Git.

- Raw datasets are tracked using `.dvc` files
- Git stores lightweight pointers instead of actual data
- Ensures reproducibility by linking data versions with code and experiments

---

## Logging and Exception Handling

- Centralized logging is implemented using Python’s `logging` module
- Logs are stored with timestamps for debugging and monitoring
- Custom exception handling provides meaningful error messages and stack trace context

---

## Key Features

- Modular and scalable pipeline design
- Reproducible preprocessing and training
- Hyperparameter tuning
- Experiment tracking and visualization
- Model versioning and rollback
- Data version control
- Production-oriented structure

---

## Conclusion

This project reflects a real-world machine learning workflow where:

- Training is performed locally
- Experiments are tracked centrally
- Models are versioned and reproducible
- Data, code, and results are tightly linked

The setup closely mirrors industry-standard practices used in production-grade data science systems.

