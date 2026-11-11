import pandas as pd 

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
import numpy as np

# load dataset
df = pd.read_csv('data/train.csv')


# Display first 5 records
# print('first 5 records:')
# print(df.head())


# #dataset shape
# print('\ndataset shape:')
# print(df.shape)


# #dataset columns
# print('\ndataset columns:')
# print(df.columns)

# #dataset information
# print('\ndataset information:')
# df.info()



# convert data column into datetime format
#df['date'] = pd.to_datetime(df['date'])

# #total records
# print('\ntotal records:', len(df))

# # data range
# print('\nstarting date:', df['date'].min())
# print('ending date:',df['date'].max())


# # total stores
# print('\ntotal stores;', df['store'].nunique())

# # total products
# print('\ntotal products:', df['item'].nunique())


# # total sales
# print('\ntotal sales:', df['sales'].sum())


# #missing values
# print('\nmissing values:')
# print(df.isnull().sum())


# # duplicate records
# print('\nduplicate records:', df.duplicated().sum())


# # statistical analysis
# print('\nsales statistical analysis:')
# print(df['sales'].describe())


import matplotlib.pyplot as plt


# # Convert date column into datetime
# df["date"] = pd.to_datetime(df["date"], errors="coerce")

# # Remove invalid dates
# df = df.dropna(subset=["date"])

# # Create Month column
# df["Month"] = df["date"].dt.to_period("M")

# # Monthly Sales Analysis
# monthly_sales = df.groupby("Month")["sales"].sum()

# print("\nMonthly Sales:")
# print(monthly_sales)

# # Highest Sales Month
# best_month = monthly_sales.idxmax()

# print("\nHighest Sales Month:", best_month)
# print("Highest Monthly Sales:", monthly_sales.max())

# # Monthly Sales Graph
# plt.figure(figsize=(14, 6))
# plt.plot(monthly_sales.index.astype(str), monthly_sales.values)

# plt.title("Monthly Sales Analysis")
# plt.xlabel("Month")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()

# Store-wise Sales Analysis

# store_sales = df.groupby("store")["sales"].sum()

# print("\nStore-wise Sales:")
# print(store_sales)

# # Best Performing Store
# best_store = store_sales.idxmax()

# print("\nBest Performing Store:", best_store)
# print("Total Sales:", store_sales.max())

# # Store Sales Graph
# plt.figure(figsize=(10, 5))

# plt.bar(store_sales.index, store_sales.values)

# plt.title("Store-wise Sales Analysis")
# plt.xlabel("Store ID")
# plt.ylabel("Total Sales")

# plt.tight_layout()
# plt.show()


# Product-wise sales analysis


# calculate sales for each item
# product_sales = df.groupby('item')['sales'].sum()

# print('\nproduct-wise sales:')
# print(product_sales)


# #finding best selling product
# best_product = product_sales.idxmax()

# print('\nbest selling product :',best_product)
# print('total sales:', product_sales.max())


# # lowest selling product
# lowest_product = product_sales.idxmin()

# print('\nlowest selling product :',lowest_product)
# print('total sales:', product_sales.min())


# # Top 10 Best Selling Products
# top_products = product_sales.sort_values(ascending=False).head(10)

# print("\nTop 10 Best Selling Products:")
# print(top_products)

# # Product Sales Graph
# plt.figure(figsize=(12, 6))

# plt.bar(top_products.index, top_products.values)

# plt.title("Top 10 Best Selling Products")
# plt.xlabel("Product ID")
# plt.ylabel("Total Sales")

# plt.tight_layout()
# plt.show()




# ==========================================
# Step 8: Daily Sales Trend Analysis
# ==========================================

# print("\n========== DAILY SALES TREND ANALYSIS ==========")

# # Calculate daily sales
# daily_sales = df.groupby("date")["sales"].sum()

# print("\nFirst 10 Days Sales:")
# print(daily_sales.head(10))

# # Find highest sales day
# best_day = daily_sales.idxmax()

# print("\nHighest Sales Date:", best_day)
# print("Highest Daily Sales:", daily_sales.max())

# # Find lowest sales day
# lowest_day = daily_sales.idxmin()

# print("\nLowest Sales Date:", lowest_day)
# print("Lowest Daily Sales:", daily_sales.min())

# # Daily Sales Graph
# plt.figure(figsize=(14, 6))

# plt.plot(daily_sales.index, daily_sales.values)

# plt.title("Daily Sales Trend Analysis")
# plt.xlabel("Date")
# plt.ylabel("Total Sales")

# plt.tight_layout()
# plt.show()



# ==========================================
# Step 9: Day-wise Sales Analysis
# ==========================================

# print("\n========== DAY-WISE SALES ANALYSIS ==========")

# # Convert date into datetime format
# df["date"] = pd.to_datetime(df["date"], errors="coerce")

# # Remove invalid dates
# df = df.dropna(subset=["date"])

# # Extract day name
# df["Day"] = df["date"].dt.day_name()

# # Calculate sales by day
# day_sales = df.groupby("Day")["sales"].sum()

# # Arrange days in correct order
# day_order = [
#     "Monday", "Tuesday", "Wednesday",
#     "Thursday", "Friday", "Saturday", "Sunday"
# ]

# day_sales = day_sales.reindex(day_order)

# print("\nDay-wise Sales:")
# print(day_sales)

# # Best Sales Day
# best_day = day_sales.idxmax()

# print("\nBest Sales Day:", best_day)
# print("Total Sales:", day_sales.max())

# # Lowest Sales Day
# lowest_day = day_sales.idxmin()

# print("\nLowest Sales Day:", lowest_day)
# print("Total Sales:", day_sales.min())

# # Graph
# plt.figure(figsize=(10, 5))
# plt.bar(day_sales.index, day_sales.values)

# plt.title("Day-wise Sales Analysis")
# plt.xlabel("Day")
# plt.ylabel("Total Sales")

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()



# ==========================================
# Step 10: Prepare Data for Machine Learning
# ==========================================

# print("\n========== MACHINE LEARNING DATA PREPARATION ==========")

# # Create a separate copy of dataset
# ml_df = df[["date", "store", "item", "sales"]].copy()

# # Convert date into datetime format
# ml_df["date"] = pd.to_datetime(ml_df["date"], errors="coerce")

# # Remove invalid dates
# ml_df = ml_df.dropna(subset=["date"])

# # Sort dataset
# ml_df = ml_df.sort_values(["store", "item", "date"])

# # Extract date features
# ml_df["day"] = ml_df["date"].dt.day
# ml_df["month"] = ml_df["date"].dt.month
# ml_df["year"] = ml_df["date"].dt.year
# ml_df["day_of_week"] = ml_df["date"].dt.dayofweek

# # Previous day sales
# ml_df["previous_day_sales"] = (
#     ml_df.groupby(["store", "item"])["sales"].shift(1)
# )

# # Previous 7 days average sales
# ml_df["last_7_days_avg"] = (
#     ml_df.groupby(["store", "item"])["sales"]
#     .transform(lambda x: x.shift(1).rolling(7).mean())
# )

# # Remove missing values
# ml_df = ml_df.dropna()

# print("\nMachine Learning Dataset:")
# print(ml_df.head(10))

# print("\nML Dataset Shape:")
# print(ml_df.shape)

# print("\nMissing Values:")
# print(ml_df.isnull().sum())


# # # ==========================================
# # # Step 11: Train-Test Split
# # # ==========================================

# print("\n========== TRAIN TEST SPLIT ==========")

# # Check if ml_df exists
# if "ml_df" in globals():

#     # Sort data by date
#     ml_df = ml_df.sort_values("date")

#     # Define input features
#     X = ml_df[
#         [
#             "store",
#             "item",
#             "day",
#             "month",
#             "year",
#             "day_of_week",
#             "previous_day_sales",
#             "last_7_days_avg"
#         ]
#     ]

#     # Define target variable
#     y = ml_df["sales"]

#     # Calculate 80% training size
#     split_index = int(len(ml_df) * 0.80)

#     # Split training and testing data
#     X_train = X.iloc[:split_index]
#     X_test = X.iloc[split_index:]

#     y_train = y.iloc[:split_index]
#     y_test = y.iloc[split_index:]

#     print("\nTraining Data Shape:", X_train.shape)
#     print("Testing Data Shape:", X_test.shape)

#     print("\nTraining Target Shape:", y_train.shape)
#     print("Testing Target Shape:", y_test.shape)

# else:
#     print("Error: Please run Step 10 first.")






# #     # ==========================================
# # # Step 12: Random Forest Regression Model
# # # ==========================================

# print("\n========== RANDOM FOREST MODEL TRAINING ==========")

# #Create Random Forest Model
# rf_model = RandomForestRegressor(
#     n_estimators=100,
#     max_depth=15,
#     random_state=42,
#     n_jobs=-1
# )

# # Train the Model
# rf_model.fit(X_train, y_train)

# print("\nModel Training Completed Successfully!")

# # Make Predictions
# y_pred = rf_model.predict(X_test)

# print("\nFirst 10 Actual Sales:")
# print(y_test.head(10).values)

# print("\nFirst 10 Predicted Sales:")
# print(y_pred[:10])



# # ==========================================
# # Step 13: Model Evaluation
# # ==========================================

# print("\n========== MODEL EVALUATION ==========")

# # Calculate MAE
# mae = mean_absolute_error(y_test, y_pred)

# # Calculate MSE
# mse = mean_squared_error(y_test, y_pred)

# # Calculate RMSE
# rmse = np.sqrt(mse)

# # Calculate R2 Score
# r2 = r2_score(y_test, y_pred)

# # Display Results
# print("\nMAE:", mae)
# print("MSE:", mse)
# print("RMSE:", rmse)
# print("R2 Score:", r2)





# # ==========================================
# # Step 14: Actual vs Predicted Sales Graph
# # ==========================================

# print("\n========== ACTUAL VS PREDICTED SALES ==========")

# plt.figure(figsize=(12, 6))

# plt.plot(
#     y_test.values[:100],
#     label="Actual Sales"
# )

# plt.plot(
#     y_pred[:100],
#     label="Predicted Sales"
# )

# plt.title("Actual vs Predicted Sales")
# plt.xlabel("Records")
# plt.ylabel("Sales")

# plt.legend()
# plt.grid(True)

# plt.show()




# # ==========================================
# # Step 15: Future Sales Forecasting
# # ==========================================

# print("\n========== FUTURE SALES FORECASTING ==========")

# # Convert date column into datetime
# df["date"] = pd.to_datetime(df["date"], errors="coerce")

# # Find last date
# last_date = df["date"].max()

# # Generate next 7 days
# future_dates = pd.date_range(
#     start=last_date + pd.Timedelta(days=1),
#     periods=7
# )

# # Store historical sales for every store and item
# sales_history = {}

# for (store, item), group in df.groupby(["store", "item"]):
#     sales_history[(store, item)] = group.sort_values("date")["sales"].tolist()

# forecast_results = []

# # Predict sales for next 7 days
# for future_date in future_dates:

#     daily_predictions = []

#     for (store, item), history in sales_history.items():

#         # Prepare features
#         features = pd.DataFrame([{
#             "store": store,
#             "item": item,
#             "day": future_date.day,
#             "month": future_date.month,
#             "year": future_date.year,
#             "day_of_week": future_date.dayofweek,
#             "previous_day_sales": history[-1],
#             "last_7_days_avg": np.mean(history[-7:])
#         }])

#         # Predict sales
#         prediction = rf_model.predict(features)[0]

#         prediction = max(0, prediction)

#         daily_predictions.append({
#             "date": future_date,
#             "store": store,
#             "item": item,
#             "predicted_sales": round(prediction)
#         })

#         # Update history for next prediction
#         history.append(prediction)

#     forecast_results.extend(daily_predictions)

# # Create forecast DataFrame
# forecast_df = pd.DataFrame(forecast_results)

# # Display forecast
# print("\nNext 7 Days Sales Forecast:")
# print(forecast_df.head(20))

# # Total predicted sales by date
# daily_forecast = forecast_df.groupby("date")["predicted_sales"].sum()

# print("\nDate-wise Predicted Sales:")
# print(daily_forecast)

# # Save forecast
# forecast_df.to_csv("future_sales_forecast.csv", index=False)

# print("\nForecast saved successfully!")




# ==========================================
# Step 16: Check Inventory Dataset
# ==========================================

print("\n========== INVENTORY DATA ==========")

inventory_df = pd.read_csv("inventory.csv")

print("\nInventory Shape:")
print(inventory_df.shape)

print("\nInventory Columns:")
print(inventory_df.columns.tolist())

print("\nFirst 10 Records:")
print(inventory_df.head(10))



# ==========================================
# Step 16: Inventory Analysis
# ==========================================

print("\n========== INVENTORY ANALYSIS ==========")

# Calculate Remaining Stock
inventory_df["Remaining_Stock"] = (
    inventory_df["Stock"] - inventory_df["Sales"]
)

# Calculate Reorder Level
inventory_df["Reorder_Level"] = (
    inventory_df["Sales"] * 2
)

# Check Stock Status
inventory_df["Stock_Status"] = inventory_df.apply(
    lambda row: "Reorder Required"
    if row["Remaining_Stock"] <= row["Reorder_Level"]
    else "Stock Available",
    axis=1
)

print("\nInventory Status:")
print(inventory_df)



# ==========================================
# Step 16.2: Calculate Order Quantity
# ==========================================

print("\n========== REORDER QUANTITY ==========")

inventory_df["Order_Quantity"] = (
    inventory_df["Reorder_Level"] -
    inventory_df["Remaining_Stock"]
).clip(lower=0)

inventory_df["Order_Cost"] = (
    inventory_df["Order_Quantity"] *
    inventory_df["Price"]
)

print("\nFinal Reorder Report:")

print(
    inventory_df[
        [
            "Product",
            "Remaining_Stock",
            "Reorder_Level",
            "Stock_Status",
            "Order_Quantity",
            "Order_Cost"
        ]
    ]
)

print("\nTotal Order Cost:")
print(inventory_df["Order_Cost"].sum())


# ==========================================
# Step 16.3: Low Stock Alert
# ==========================================

print("\n========== LOW STOCK ALERT ==========")

low_stock = inventory_df[
    inventory_df["Stock_Status"] == "Reorder Required"
]

if not low_stock.empty:
    print("Warning! These products need restocking:")
    print(low_stock[["Product", "Remaining_Stock", "Reorder_Level"]])
else:
    print("All products have sufficient stock.")


    # ==========================================
# Step 16.4: Save Inventory Report
# ==========================================

print("\n========== SAVE INVENTORY REPORT ==========")

inventory_df.to_csv(
    "final_inventory_report.csv",
    index=False
)

print("Inventory report saved successfully!")
print("File: final_inventory_report.csv")


# ==========================================
# Step 16.5: Inventory Summary
# ==========================================

print("\n========== INVENTORY SUMMARY ==========")

total_products = len(inventory_df)
total_stock = inventory_df["Stock"].sum()
remaining_stock = inventory_df["Remaining_Stock"].sum()

products_to_reorder = (
    inventory_df["Stock_Status"] == "Reorder Required"
).sum()

total_order_cost = inventory_df["Order_Cost"].sum()

print("Total Products:", total_products)
print("Total Stock:", total_stock)
print("Remaining Stock:", remaining_stock)
print("Products Requiring Reorder:", products_to_reorder)
print("Total Reorder Cost: ₹", total_order_cost)

# ==========================================
# Step 16.6: Category-wise Inventory Analysis
# ==========================================

print("\n========== CATEGORY-WISE INVENTORY ==========")

category_summary = inventory_df.groupby("Category").agg(
    Total_Products=("Product", "count"),
    Total_Stock=("Stock", "sum"),
    Remaining_Stock=("Remaining_Stock", "sum"),
    Total_Sales=("Sales", "sum")
)

print(category_summary)



# ==========================================
# Step 16.7: Category-wise Stock Chart
# ==========================================

print("\n========== CATEGORY STOCK CHART ==========")

category_summary["Remaining_Stock"].plot(
    kind="bar",
    figsize=(8, 5),
    title="Category-wise Remaining Stock"
)

plt.xlabel("Category")
plt.ylabel("Remaining Stock")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ==========================================
# Step 16.8: Save Category Report
# ==========================================

# print("\n========== SAVE CATEGORY REPORT ==========")

# category_summary.to_csv(
#     "category_inventory_report.csv"
# )

# print("Category report saved successfully!")
# print("File: category_inventory_report.csv")


# ==========================================
# Step 16.9: Inventory Status Chart
# ==========================================

print("\n========== INVENTORY STATUS CHART ==========")

status_summary = inventory_df["Stock_Status"].value_counts()

print(status_summary)

status_summary.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(7, 7),
    title="Inventory Stock Status"
)

plt.ylabel("")
plt.tight_layout()
plt.show()




