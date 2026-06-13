import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Exploratory Data Analysis")

if "cleaned_data" not in st.session_state:

    st.warning(
        "Please complete preprocessing first."
    )

    st.stop()

df = st.session_state["cleaned_data"]

# ===================================
# FILTERS
# ===================================

st.sidebar.subheader("📌 EDA Filters")

if "Region" in df.columns:

    selected_region = st.sidebar.multiselect(
        "Select Region",
        options=sorted(df["Region"].dropna().unique()),
        default=sorted(df["Region"].dropna().unique())
    )

    df = df[
        df["Region"].isin(selected_region)
    ]

if "Category" in df.columns:

    selected_category = st.sidebar.multiselect(
        "Select Category",
        options=sorted(df["Category"].dropna().unique()),
        default=sorted(df["Category"].dropna().unique())
    )

    df = df[
        df["Category"].isin(selected_category)
    ]

# ===================================
# KPI SECTION
# ===================================

st.subheader("📈 Business KPIs")

col1, col2, col3, col4 = st.columns(4)

revenue_col = "Sales" if "Sales" in df.columns else "Revenue"

col1.metric(
    "Total Revenue",
    f"₹{df[revenue_col].sum():,.0f}"
)

col2.metric(
    "Total Orders",
    len(df)
)

col3.metric(
    "Average Revenue",
    f"₹{df[revenue_col].mean():,.0f}"
)

if "Product Name" in df.columns:

    col4.metric(
        "Products",
        df["Product Name"].nunique()
    )

st.divider()

# ===================================
# SALES TREND
# ===================================

if "Order Date" in df.columns:

    st.subheader("📅 Sales Trend")

    sales_trend = (
        df.groupby("Order Date")[revenue_col]
        .sum()
        .reset_index()
    )

    fig = px.line(
        sales_trend,
        x="Order Date",
        y=revenue_col,
        markers=True,
        title="Revenue Over Time"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ===================================
# CATEGORY ANALYSIS
# ===================================

if "Category" in df.columns:

    st.subheader("🧩 Category Revenue")

    category_sales = (
        df.groupby("Category")[revenue_col]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category_sales,
        names="Category",
        values=revenue_col,
        hole=0.45
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ===================================
# REGION ANALYSIS
# ===================================

if "Region" in df.columns:

    st.subheader("🌍 Region Revenue")

    region_sales = (
        df.groupby("Region")[revenue_col]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        region_sales,
        x="Region",
        y=revenue_col,
        text_auto=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ===================================
# TOP PRODUCTS
# ===================================

if "Product Name" in df.columns:

    st.subheader("🏆 Top 15 Products")

    product_sales = (
        df.groupby("Product Name")[revenue_col]
        .sum()
        .reset_index()
        .sort_values(
            by=revenue_col,
            ascending=False
        )
        .head(15)
    )

    fig = px.bar(
        product_sales,
        x=revenue_col,
        y="Product Name",
        orientation="h",
        title="Top Revenue Generating Products"
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ===================================
# MONTHLY REVENUE
# ===================================

if "Month" in df.columns:

    st.subheader("📆 Monthly Revenue")

    monthly = (
        df.groupby("Month")[revenue_col]
        .sum()
        .reset_index()
    )

    fig = px.area(
        monthly,
        x="Month",
        y=revenue_col
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ===================================
# PROMOTION IMPACT
# ===================================

if "Promotion Flag" in df.columns:

    st.subheader("🎯 Promotion Impact")

    promo = (
        df.groupby(
            "Promotion Flag"
        )[revenue_col]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        promo,
        x="Promotion Flag",
        y=revenue_col,
        text_auto=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ===================================
# DATA PREVIEW
# ===================================

st.subheader("📂 Dataset Preview")

rows = st.slider(
    "Rows to Display",
    min_value=10,
    max_value=500,
    value=50,
    step=10
)

st.dataframe(
    df.head(rows),
    use_container_width=True
)