import streamlit as st
import pandas as pd

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="SmartStock AI",
    page_icon="📦",
    layout="wide"
)
# ==========================================
# Step 21.1: Professional Dashboard Styling
# ==========================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

h1 {
    color: #17365D;
    font-weight: 800;
}

h2, h3 {
    color: #1F4E79;
}

[data-testid="stMetric"] {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.stButton button {
    border-radius: 8px;
    font-weight: bold;
}
/* Sidebar Styling */

[data-testid="stSidebar"] {
    background-color: #17365D;
}

[data-testid="stSidebar"] * {
    color: white;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: white;
}

[data-testid="stSidebar"] label {
    color: white;
}
/* Professional Button Styling */

.stDownloadButton button {
    background-color: #17365D;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
}

.stDownloadButton button:hover {
    background-color: #2874A6;
    color: white;
}

/* Dataframe Styling */

[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
}
/* Step 21.4: KPI Card Hover Effect */

[data-testid="stMetric"] {
    transition: all 0.3s ease;
    border: 1px solid #e0e6ed;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.15);
    border-color: #2874A6;
}
/* Step 21.5: Section Header Styling */

h2 {
    color: #17365D;
    font-weight: 800;
    border-bottom: 2px solid #2874A6;
    padding-bottom: 8px;
}

h3 {
    color: #2874A6;
    font-weight: 700;
}

hr {
    border-top: 2px solid #dce3eb;
}
</style>
""", unsafe_allow_html=True)
# ==========================================
# Dashboard Title
# ==========================================

st.title("📦 SmartStock AI")
st.subheader("Inventory Management Dashboard")

st.divider()

# ==========================================
# Load Inventory Data
# ==========================================

inventory_df = pd.read_csv("final_inventory_report.csv")

# ==========================================
# Dashboard KPIs
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Products",
        len(inventory_df)
    )

with col2:
    st.metric(
        "Total Stock",
        inventory_df["Stock"].sum()
    )

with col3:
    st.metric(
        "Remaining Stock",
        inventory_df["Remaining_Stock"].sum()
    )

with col4:
    st.metric(
        "Products to Reorder",
        (inventory_df["Stock_Status"] == "Reorder Required").sum()
    )

st.divider()

# ==========================================
# Inventory Details
# ==========================================

st.subheader("📋 Inventory Details")

st.dataframe(
    inventory_df,
    width="stretch"
)

# ==========================================
# Low Stock Alerts
# ==========================================

st.subheader("🚨 Low Stock Alerts")

low_stock = inventory_df[
    inventory_df["Stock_Status"] == "Reorder Required"
]

if not low_stock.empty:

    st.warning("Some products need restocking!")

    st.dataframe(
        low_stock[
            [
                "Product",
                "Remaining_Stock",
                "Reorder_Level",
                "Order_Quantity"
            ]
        ],
        width="stretch"
    )

else:
    st.success("All products have sufficient stock!")

st.divider()

# ==========================================
# Step 20.1: Reorder Cost Analysis
# ==========================================

st.divider()
st.subheader("💰 Inventory Reorder Cost Analysis")

total_order_qty = inventory_df["Order_Quantity"].sum()
total_order_cost = inventory_df["Order_Cost"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Reorder Quantity", int(total_order_qty))

with col2:
    st.metric("Total Reorder Cost", f"₹{total_order_cost:,.2f}")

st.write("Product-wise Reorder Details")

reorder_report = inventory_df[
    inventory_df["Order_Quantity"] > 0
][["Product", "Order_Quantity", "Price", "Order_Cost"]]

st.dataframe(reorder_report, width="stretch")


# ==========================================
# Step 20.2: Download Reorder Report
# ==========================================

st.subheader("📥 Download Inventory Reorder Report")

reorder_csv = reorder_report.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Reorder Report",
    data=reorder_csv,
    file_name="SmartStock_Reorder_Report.csv",
    mime="text/csv"
)


# ==========================================
# Step 20.3: Inventory Stock Value Analysis
# ==========================================

st.divider()
st.subheader("💎 Inventory Stock Value Analysis")

inventory_df["Stock_Value"] = (
    inventory_df["Stock"] * inventory_df["Price"]
)

inventory_df["Remaining_Stock_Value"] = (
    inventory_df["Remaining_Stock"] * inventory_df["Price"]
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Inventory Value",
        f"₹{inventory_df['Stock_Value'].sum():,.2f}"
    )

with col2:
    st.metric(
        "Remaining Inventory Value",
        f"₹{inventory_df['Remaining_Stock_Value'].sum():,.2f}"
    )

st.subheader("📊 Product-wise Stock Value")

st.bar_chart(
    inventory_df.set_index("Product")[
        "Remaining_Stock_Value"
    ]
)

st.dataframe(
    inventory_df[
        ["Product", "Stock", "Remaining_Stock",
         "Price", "Remaining_Stock_Value"]
    ],
    width="stretch"
)

# ==========================================
# Step 20.4: Download Stock Valuation Report
# ==========================================

st.subheader("📥 Download Stock Valuation Report")

stock_value_report = inventory_df[
    [
        "Product",
        "Stock",
        "Remaining_Stock",
        "Price",
        "Stock_Value",
        "Remaining_Stock_Value"
    ]
]

stock_value_csv = stock_value_report.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Stock Valuation CSV",
    data=stock_value_csv,
    file_name="SmartStock_Inventory_Valuation.csv",
    mime="text/csv"
)

# ==========================================
# Step 20.5: Interactive Inventory Filters
# ==========================================

st.divider()
st.subheader("🔎 Search & Filter Inventory")

col1, col2 = st.columns(2)

with col1:
    selected_category = st.selectbox(
        "Select Category",
        ["All Categories"] + sorted(inventory_df["Category"].unique())
    )

with col2:
    selected_status = st.selectbox(
        "Select Stock Status",
        ["All Status", "Stock Available", "Reorder Required"]
    )

filtered_inventory = inventory_df.copy()

if selected_category != "All Categories":
    filtered_inventory = filtered_inventory[
        filtered_inventory["Category"] == selected_category
    ]

if selected_status != "All Status":
    filtered_inventory = filtered_inventory[
        filtered_inventory["Stock_Status"] == selected_status
    ]
# ==========================================
# Step 20.9: Empty Search Result Handling
# ==========================================

st.subheader("🔍 Search Result Status")

st.write(f"Products Found: {len(filtered_inventory)}")

if not filtered_inventory.empty:

    st.dataframe(
        filtered_inventory,
        width="stretch"
    )

    st.success("✅ Inventory records found!")

else:

    st.warning(
        "⚠️ No products found. Please try another search!"
    )

# ==========================================
# Step 20.7: Product Search
# ==========================================

search_product = st.text_input(
    "🔍 Search Product by Name"
)

if search_product:
    filtered_inventory = filtered_inventory[
        filtered_inventory["Product"].str.contains(
            search_product,
            case=False,
            na=False
        )
    ]



# ==========================================
# Step 20.6: Download Filtered Inventory
# ==========================================

st.subheader("📥 Download Filtered Inventory")

filtered_csv = filtered_inventory.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Filtered Inventory CSV",
    data=filtered_csv,
    file_name="SmartStock_Filtered_Inventory.csv",
    mime="text/csv"
)

# ==========================================
# Step 22.2: Category-wise Inventory Analysis
# ==========================================

st.divider()
st.subheader("📊 Category-wise Inventory Analysis")

category_summary = inventory_df.groupby("Category").agg(
    Total_Products=("Product", "count"),
    Total_Stock=("Stock", "sum"),
    Total_Sales=("Sales", "sum"),
    Remaining_Stock=("Remaining_Stock", "sum"),
    Inventory_Value=("Stock_Value", "sum"),
    Remaining_Value=("Remaining_Stock_Value", "sum")
).reset_index()

# Category-wise Data Table
st.write("### 📋 Category-wise Complete Report")

st.dataframe(
    category_summary,
    width="stretch"
)

# Category-wise Charts
col1, col2 = st.columns(2)

with col1:
    st.write("Total Stock by Category")
    st.bar_chart(
        category_summary.set_index("Category")["Total_Stock"]
    )

with col2:
    st.write("Remaining Stock by Category")
    st.bar_chart(
        category_summary.set_index("Category")["Remaining_Stock"]
    )

# Download Category Report
category_csv = category_summary.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "Download Category-wise Report",
    data=category_csv,
    file_name="Category_Wise_Inventory_Report.csv",
    mime="text/csv"
)
# ==========================================
# Step 22.3: Category-wise Product Details
# ==========================================

st.divider()
st.subheader("📦 Category-wise Product Details")

# Category Selection
category_list = inventory_df["Category"].dropna().unique()

selected_product_category = st.selectbox(
    "Select Category",
    category_list,
    key="product_category_filter"
)

# Filter Products
category_products = inventory_df[
    inventory_df["Category"] == selected_product_category
]

# Display Selected Category
st.write(f"### {selected_product_category} Products")

# Product Details
st.dataframe(
    category_products,
    width="stretch"
)

# Category KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Products",
        len(category_products)
    )

with col2:
    st.metric(
        "Total Stock",
        int(category_products["Stock"].sum())
    )

with col3:
    st.metric(
        "Remaining Stock",
        int(category_products["Remaining_Stock"].sum())
    )

# ==========================================
# Step 22.4: Download Category-wise Report
# ==========================================

st.subheader("📥 Download Category Report")

category_product_csv = category_products.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Selected Category CSV",
    data=category_product_csv,
    file_name=f"{selected_product_category}_Inventory_Report.csv",
    mime="text/csv",
    key="download_category_report"
)
# ==========================================
# Step 22.5: Category-wise Stock Value Analysis
# ==========================================

st.divider()
st.subheader("💰 Category-wise Stock Value Analysis")

inventory_df["Stock_Value"] = (
    inventory_df["Stock"] * inventory_df["Price"]
)

inventory_df["Remaining_Stock_Value"] = (
    inventory_df["Remaining_Stock"] * inventory_df["Price"]
)

stock_value_summary = inventory_df.groupby("Category").agg(
    Total_Stock_Value=("Stock_Value", "sum"),
    Remaining_Stock_Value=("Remaining_Stock_Value", "sum")
).reset_index()

st.dataframe(stock_value_summary, width="stretch")

st.bar_chart(
    stock_value_summary.set_index("Category")[
        ["Total_Stock_Value", "Remaining_Stock_Value"]
    ]
)
# ==========================================
# Step 22.6: Category-wise Reorder Analysis
# ==========================================

st.divider()
st.subheader("⚠️ Category-wise Reorder Analysis")

reorder_summary = inventory_df.groupby("Category").agg(
    Total_Products=("Product", "count"),
    Reorder_Products=("Stock_Status",
                      lambda x: (x == "Reorder Required").sum()),
    Total_Order_Quantity=("Order_Quantity", "sum"),
    Total_Reorder_Cost=("Order_Cost", "sum")
).reset_index()

st.dataframe(
    reorder_summary,
    width="stretch"
)

# Reorder Cost Chart
st.write("### Category-wise Reorder Cost")

st.bar_chart(
    reorder_summary.set_index("Category")["Total_Reorder_Cost"]
)

# Download Report
reorder_category_csv = reorder_summary.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "Download Category Reorder Report",
    data=reorder_category_csv,
    file_name="Category_Reorder_Report.csv",
    mime="text/csv",
    key="category_reorder_download"
)
# ==========================================
# Step 22.7: Final Dashboard Summary
# ==========================================

st.divider()
st.header("📈 SmartStock AI - Final Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Products",
        len(inventory_df)
    )

with col2:
    st.metric(
        "Total Stock",
        int(inventory_df["Stock"].sum())
    )

with col3:
    st.metric(
        "Remaining Stock",
        int(inventory_df["Remaining_Stock"].sum())
    )

with col4:
    reorder_count = (
        inventory_df["Stock_Status"] == "Reorder Required"
    ).sum()

    st.metric(
        "Reorder Products",
        int(reorder_count)
    )

# Final Status
if reorder_count > 0:
    st.warning(f"⚠️ {reorder_count} products need stock replenishment.")
else:
    st.success("All products have sufficient stock!")

st.success("SmartStock AI Inventory Summary Generated Successfully!")

# ==========================================
# Step 18.1: Sales Forecasting Dashboard
# ==========================================

st.divider()

st.header("🔮 AI Sales Forecasting")

# Load Forecast Data
forecast_df = pd.read_csv("future_sales_forecast.csv")

forecast_df["date"] = pd.to_datetime(forecast_df["date"])


# ==========================================
# Step 19.1: Interactive Filters
# ==========================================

st.sidebar.title("🔍 Dashboard Filters")

# Store Selection
store_list = sorted(forecast_df["store"].unique())

selected_store = st.sidebar.selectbox(
    "Select Store",
    ["All Stores"] + store_list
)

# Product Selection
item_list = sorted(forecast_df["item"].unique())

selected_item = st.sidebar.selectbox(
    "Select Product",
    ["All Products"] + item_list
)

# Apply Filters
if selected_store != "All Stores":
    forecast_df = forecast_df[
        forecast_df["store"] == selected_store
    ]

if selected_item != "All Products":
    forecast_df = forecast_df[
        forecast_df["item"] == selected_item
    ]

st.success("Filters applied successfully!")

# ==========================================
# Step 19.2: Date Range Filter
# ==========================================

st.sidebar.subheader("📅 Date Filter")

min_date = forecast_df["date"].min().date()
max_date = forecast_df["date"].max().date()

selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(selected_dates) == 2:

    start_date, end_date = selected_dates

    forecast_df = forecast_df[
        (forecast_df["date"].dt.date >= start_date) &
        (forecast_df["date"].dt.date <= end_date)
    ]

st.success("All filters applied successfully!")

# Date-wise Sales Forecast
daily_forecast = forecast_df.groupby("date")[
    "predicted_sales"
].sum()

# Total Predicted Sales
total_forecast = forecast_df["predicted_sales"].sum()

# Average Daily Sales
average_forecast = daily_forecast.mean()

# Forecast Metrics
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Predicted Sales (7 Days)",
        int(total_forecast)
    )

with col2:
    st.metric(
        "Average Daily Predicted Sales",
        round(average_forecast)
    )

# Forecast Chart
st.subheader("📊 Next 7 Days Sales Prediction")

st.line_chart(daily_forecast)

# ==========================================
# Step 19.4: Best and Lowest Sales Day
# ==========================================

st.subheader("🏆 Sales Forecast Insights")

if not daily_forecast.empty:

    best_day = daily_forecast.idxmax()
    lowest_day = daily_forecast.idxmin()

    best_sales = daily_forecast.max()
    lowest_sales = daily_forecast.min()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Highest Predicted Sales Day",
            int(best_sales),
            best_day.strftime("%d-%m-%Y")
        )

    with col2:
        st.metric(
            "Lowest Predicted Sales Day",
            int(lowest_sales),
            lowest_day.strftime("%d-%m-%Y")
        )
# ==========================================
# Step 19.5: Store-wise Sales Comparison
# ==========================================

st.subheader("🏬 Store-wise Sales Forecast")

store_forecast = forecast_df.groupby("store")[
    "predicted_sales"
].sum().sort_values(ascending=False)

st.bar_chart(store_forecast)

if not store_forecast.empty:

    best_store = store_forecast.idxmax()
    lowest_store = store_forecast.idxmin()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Best Performing Store",
            f"Store {best_store}",
            int(store_forecast.max())
        )

    with col2:
        st.metric(
            "Lowest Performing Store",
            f"Store {lowest_store}",
            int(store_forecast.min())
        )
# Forecast Table
st.subheader("📋 Forecast Details")

st.dataframe(
    forecast_df,
    width="stretch"
)


# ==========================================
# Step 19.3: Download Forecast Report
# ==========================================

st.subheader("📥 Download Sales Forecast")

csv_data = forecast_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Forecast CSV",
    data=csv_data,
    file_name="SmartStock_Sales_Forecast.csv",
    mime="text/csv"
)

# ==========================================
# Step 19.6: Product-wise Sales Forecast
# ==========================================

st.divider()
st.subheader("📦 Product-wise Sales Forecast")

item_forecast = forecast_df.groupby("item")[
    "predicted_sales"
].sum().sort_values(ascending=False)

st.bar_chart(item_forecast)

if not item_forecast.empty:

    best_item = item_forecast.idxmax()
    lowest_item = item_forecast.idxmin()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Best Selling Product",
            f"Item {best_item}",
            int(item_forecast.max())
        )

    with col2:
        st.metric(
            "Lowest Selling Product",
            f"Item {lowest_item}",
            int(item_forecast.min())
        )

# ==========================================
# Step 19.7: Top 5 High-Demand Products
# ==========================================

st.divider()
st.subheader("🔥 Top 5 High-Demand Products")

top_5_items = item_forecast.head(5)

st.bar_chart(top_5_items)

st.write("Top 5 Products Details:")

top_5_report = top_5_items.reset_index()
top_5_report.columns = ["Item", "Predicted Sales"]

st.dataframe(top_5_report, width="stretch")


# ==========================================
# Step 19.8: Download Top 5 Products Report
# ==========================================

st.subheader("📥 Download Top Products Report")

top_products_csv = top_5_report.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Top 5 Products CSV",
    data=top_products_csv,
    file_name="SmartStock_Top_Products.csv",
    mime="text/csv"
)



# ==========================================
# Step 19.9: Daily Demand Trend
# ==========================================

st.divider()
st.subheader("📈 Daily Demand Trend Analysis")

if len(daily_forecast) >= 2:

    first_day_sales = daily_forecast.iloc[0]
    last_day_sales = daily_forecast.iloc[-1]

    if first_day_sales != 0:
        demand_change = (
            (last_day_sales - first_day_sales)
            / first_day_sales
        ) * 100
    else:
        demand_change = 0

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("First Day Sales", int(first_day_sales))

    with col2:
        st.metric("Last Day Sales", int(last_day_sales))

    with col3:
        st.metric(
            "Demand Change",
            f"{demand_change:.2f}%"
        )

    if demand_change > 0:
        st.success("📈 Sales demand is increasing!")
    elif demand_change < 0:
        st.warning("📉 Sales demand is decreasing!")
    else:
        st.info("Sales demand is stable.")