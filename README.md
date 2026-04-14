# 🛡️ Vehicle Insurance Claim Fraud Detection System

## 📌 Project Overview
Insurance fraud is a significant issue that costs the industry billions of dollars annually. This project is a complete, end-to-end Machine Learning solution designed to automatically evaluate vehicle insurance claims and predict the probability of fraud. 

This project simulates a production-level industry workflow, encompassing everything from raw data exploration and feature engineering to model deployment using a modern tech stack (FastAPI & Streamlit). It is designed to act as a "Forensic Investigation Console" for claims adjusters.

---

##  Technology Stack & Tools
**1. Data Science & Machine Learning:**
* **Python:** Core programming language.
* **Pandas & NumPy:** Data manipulation, cleaning, and numerical computations.
* **Scikit-Learn:** Data preprocessing, encoding, model training, and evaluation metrics.
* **XGBoost:** Advanced gradient boosting library.
* **Imbalanced-Learn (SMOTE):** Handling class imbalance in the dataset.
* **Matplotlib & Seaborn:** Data visualization and exploratory data analysis (EDA).

**2. Backend & API Deployment:**
* **FastAPI:** High-performance web framework used to build the RESTful API for the ML model.
* **Uvicorn:** ASGI web server implementation for Python to run the FastAPI app.
* **Pickle:** Serializing and saving the trained machine learning model.

**3. Frontend & User Interface:**
* **Streamlit:** Rapid framework used to build the interactive, web-based investigation dashboard.
* **Plotly:** Rendering high-quality, interactive radial gauge charts for risk visualization.

---

##  The Machine Learning Pipeline (Step-by-Step)

### Step 1: Data Acquisition & EDA (Exploratory Data Analysis)
* **Data Source:** A real-world tabular dataset from Kaggle containing policy details, incident telemetry, and demographic data.
* **Exploration:** Analyzed data distributions, identified missing values, and visualized relationships between features (e.g., Accident Area vs. Fraud, Age vs. Fraud).
* **Imbalance Detection:** Identified a severe class imbalance where fraudulent claims represented a very small percentage of the total dataset.

### Step 2: Data Preprocessing & Cleaning
* **Handling Missing Values:** Applied strategic imputation for missing or logically inconsistent data points.
* **Categorical Encoding:** Used `LabelEncoder` and `OneHotEncoder` to transform text-based categorical variables (e.g., Make, PolicyType, Month) into numerical formats readable by the ML algorithms.
* **Scaling:** Applied normalization to numerical features to ensure algorithms that rely on distance metrics perform optimally.

### Step 3: Feature Engineering
* Transformed date/time variables into meaningful categorical groups.
* Combined related features (e.g., policy constraints and vehicle categories) to create stronger predictive signals.
* Dropped highly collinear or irrelevant features to reduce dimensionality and noise.

### Step 4: Model Training & Handling Imbalance
* **Algorithms Tested:** Trained and compared multiple models including **Logistic Regression, Support Vector Machines (SVM), Random Forest, Gradient Boosting, and XGBoost**.
* **Imbalance Handling:** Applied **SMOTE (Synthetic Minority Over-sampling Technique)** to balance the training data, allowing the models to learn the patterns of the minority class (Fraud) effectively.
* **Hyperparameter Tuning:** Utilized cross-validation to find the optimal parameters for the ensemble models.

### Step 5: Model Evaluation & Selection
Since accuracy is a misleading metric for imbalanced datasets, models were strictly evaluated based on their ability to catch fraud without overly penalizing honest customers:
* **Metrics Used:** Confusion Matrix, Precision, Recall, F1-Score, and ROC-AUC.
* **Winner:** The best-performing model (highest F1-Score and AUC for the Fraud class) was selected and exported as `fraud_detection_model.pkl`.

---

##  System Architecture

1. **The Engine (Backend):** A `FastAPI` server (`API.py`) loads the `.pkl` model into memory. It exposes a `/predict` POST endpoint that receives JSON payloads containing 30 claim features, processes them, and returns a fraud probability score.
2. **The Dashboard (Frontend):** A `Streamlit` app (`app.py`) provides a premium, dark-themed user interface. It collects user inputs via dropdowns and sliders, constructs the JSON payload, calls the FastAPI backend, and visualizes the returned risk score using an interactive Plotly gauge.

---

## 🚀 How to Run the Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Mohammedelmalahany/Vehicle-Insurance-Fraud-Detection.git
cd Vehicle-Insurance-Fraud-Detection
