# Intelligent Sales Forecasting and Inventory Optimization System

## Project Overview

This project is an AI-powered sales forecasting and inventory optimization system developed using Python and Streamlit.

The system helps organizations:

* Analyze historical sales data
* Forecast future demand
* Optimize inventory levels
* Identify low-stock products
* Generate business insights
* Support data-driven decision making

## Features

### Data Upload

* Upload CSV and Excel files
* Dataset preview
* Data validation

### Data Preprocessing

* Missing value handling
* Duplicate removal
* Date feature extraction
* Data cleaning

### Exploratory Data Analysis (EDA)

* Sales trend analysis
* Category performance
* Region-wise revenue analysis
* Top products analysis
* Monthly revenue analysis
* Interactive filters

### Model Training

* Linear Regression
* Random Forest Regressor
* Automatic best model selection
* Model performance comparison

### Sales Forecasting

* Revenue trend forecasting
* Actual vs Predicted comparison

### Inventory Optimization

* Safety Stock calculation
* Reorder Point calculation
* Inventory Health Gauge
* Top Inventory Risk Products

### Executive Dashboard

* KPI Cards
* Revenue Analysis
* Product Analysis
* Regional Analysis
* AI Business Insights

### Reports

* CSV Report Download
* Business Summary

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* Scikit-Learn
* Joblib

## Project Structure

INTELLIGENT_SALES_FORECASTING

├── app.py

├── datasets/

├── models/

├── pages/

│ ├── 1_Data_Upload.py

│ ├── 2_Data_Preprocessing.py

│ ├── 3_EDA_Analysis.py

│ ├── 4_Model_Training.py

│ ├── 5_Sales_Forecasting.py

│ ├── 6_Inventory_Optimization.py

│ ├── 7_Reports.py

│ └── 8_Dashboard.py

├── utils/

├── requirements.txt

└── README.md


## Installation & Usage

### Step 1: Clone Repository

git clone YOUR_REPOSITORY_LINK

### Step 2: Open Project Folder

cd INTELLIGENT_SALES_FORECASTING

### Step 3: Install Required Libraries

pip install -r requirements.txt

### Step 4: Run Application

streamlit run app.py

### Step 5: Open Browser

Streamlit will automatically open in your browser.

If it does not open automatically, visit:

http://localhost:8501

## Reusing This Project Later

If you download this project again after several months or on another device:

1. Install Python
2. Install all required packages:

pip install -r requirements.txt

3. Run:

streamlit run app.py

No additional setup is required.



## Dataset

This project supports CSV and Excel datasets.

The project was tested using the Superstore Sales Dataset from Kaggle.

## Author

MOHAMMAD MASTAN VALI SHAIK

B.Tech Project

AI-Powered Sales Forecasting and Inventory Optimization System

