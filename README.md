# 📦 SmartStock AI – Inventory Management & Demand Forecasting System

An AI-powered Inventory Management and Sales Forecasting Dashboard built using Python, Machine Learning, Pandas and Streamlit.

## 🌐 Live Dashboard

[Click Here to View SmartStock AI](https://smartstock-ai-h5vdjff4dbqmvjbbmcpqya.streamlit.app/)

## 📌 Project Overview

SmartStock AI is a data analytics and machine learning project designed to help businesses understand inventory levels, monitor stock availability, identify products requiring reorder, and forecast future sales demand.

The project combines inventory analysis with machine learning-based sales forecasting in an interactive dashboard.

## 🚀 Key Features

### 1. Inventory Management
- Total Products and Stock Analysis
- Remaining Stock Calculation
- Product-wise Inventory Details
- Low Stock Alerts
- Reorder Quantity Calculation
- Reorder Cost Analysis

### 2. Category-wise Analysis
- Category-wise Product Details
- Category-wise Stock Analysis
- Remaining Stock Analysis
- Category-wise Inventory Value
- Category-wise Reorder Analysis

### 3. Interactive Dashboard
- Store Filter
- Product Filter
- Date Range Filter
- Product Search
- Interactive Charts and KPIs

### 4. Sales Forecasting
- Historical Sales Analysis
- Store-wise Sales Analysis
- Product-wise Sales Analysis
- Daily Demand Forecast
- Top 5 Products Analysis
- Daily Sales Trend

### 5. Data Export
- Download Inventory Report
- Download Filtered Inventory
- Download Category-wise Report
- Download Reorder Report
- Download Sales Forecast CSV

## 🤖 Machine Learning Model

**Algorithm:** Random Forest Regressor

Model Evaluation:
- MAE: 6.4766
- MSE: 71.0579
- RMSE: 8.4296
- R² Score: 0.92869

The model uses historical sales information and engineered time-based features to predict sales demand.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn
- Machine Learning
- Data Analysis
- Data Visualization

## 📂 Project Structure

```text
SmartStock-AI/
│
├── app.py
├── main.py
├── requirements.txt
│
├── train.csv
├── test.csv
├── sample_submission.csv
├── inventory.csv
│
├── future_sales_forecast.csv
├── final_inventory_report.csv
└── category_inventory_report.csv
```

## ⚙️ Installation & Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/anshuyadav9305561518/SmartStock-AI.git
```

### Step 2: Open Project Folder

```bash
cd SmartStock-AI
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Streamlit Dashboard

```bash
streamlit run app.py
```

## 📊 Dataset Information

The project uses two separate datasets:

1. Store Item Demand Forecasting dataset for historical sales analysis and machine learning-based demand forecasting.
2. Inventory demonstration dataset for product stock, category, price, sales and reorder analysis.

These datasets serve different purposes within the project.

## 🎯 Project Objective

The main objective of SmartStock AI is to demonstrate how data analytics and machine learning can support inventory monitoring, stock management and sales demand forecasting.

## 👨‍💻 Developer

**Anshu Yadav**

- GitHub: https://github.com/anshuyadav9305561518
- LinkedIn: https://linkedin.com/in/anshu-yadav-a57917289
- Portfolio: https://
