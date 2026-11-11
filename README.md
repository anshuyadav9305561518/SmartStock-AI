# 📦 SmartStock AI
### AI-Based Inventory Management & Sales Demand Forecasting System

SmartStock AI is an interactive web-based dashboard that combines Inventory Management, Data Analytics, and Machine Learning to analyze stock levels, monitor inventory, identify reorder requirements, and forecast future sales demand.

## 🌐 Live Project

🚀 **Live Dashboard:**  
https://smartstock-ai-h5vdjff4dbqmvjbbmcpgya.streamlit.app/

## 📌 Project Overview

SmartStock AI helps businesses understand inventory performance and historical sales patterns through interactive dashboards and machine learning-based demand forecasting.

The project contains two separate data modules:
- Inventory Management using product-level demonstration data.
- Sales Forecasting using historical Store Item Demand Forecasting data.

## ✨ Key Features

### 1. Inventory Management
- Total Product Analysis
- Total and Remaining Stock
- Product-wise Stock Details
- Low Stock Alerts
- Reorder Quantity Calculation
- Reorder Cost Analysis
- Inventory Valuation

### 2. Category-wise Analysis
- Category-wise Product Details
- Category-wise Stock Summary
- Remaining Stock Analysis
- Category-wise Inventory Value
- Category-wise Reorder Analysis
- Category Filters

### 3. Interactive Dashboard
- Product Search
- Category Filters
- Stock Status Filters
- Interactive KPIs
- Data Visualization

### 4. Sales Demand Forecasting
- Historical Sales Analysis
- Store-wise Sales Analysis
- Product-wise Sales Analysis
- Daily Sales Trends
- Future Sales Forecast
- Top 5 Products Analysis
- Forecast Performance Evaluation

### 5. Data Export
- Inventory Report Download
- Filtered Inventory Download
- Category-wise Report Download
- Reorder Report Download
- Sales Forecast CSV Download

## 🤖 Machine Learning Model

**Algorithm:** Random Forest Regressor

Model Evaluation Results:

| Evaluation Metric | Result |
|---|---:|
| MAE | 6.4766 |
| MSE | 71.0579 |
| RMSE | 8.4296 |
| R² Score | 0.92869 |

The model uses historical sales data and time-based features to predict future demand.

*Note: R² Score represents the proportion of variance explained by the model, not prediction accuracy.*

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

*The repository structure may vary depending on the files uploaded.*

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

### Step 4: Run Application

```bash
streamlit run app.py
```

## 📊 Dataset Information

This project uses two separate datasets:

**1. Store Item Demand Forecasting Dataset**
- Historical sales records
- Store information
- Item information
- Daily sales quantities

**2. Inventory Demonstration Dataset**
- Product names
- Categories
- Stock quantities
- Product prices
- Sales quantities

These datasets are used independently for sales forecasting and inventory analysis.

## 🎯 Project Objective

The objective of SmartStock AI is to demonstrate how Python, Data Analytics, and Machine Learning can help businesses monitor inventory, identify stock shortages, analyze sales trends, and estimate future demand.

## 👨‍💻 Developer

**Anshu Yadav**

- GitHub: https://github.com/anshuyadav9305561518
- LinkedIn: https://linkedin.com/in/anshu-yadav-a57917289
- Portfolio: https://anshuyadav9305561518.github.io/Portfolio-/

## 📜 License

Created for educational, learning, and portfolio purposes.
