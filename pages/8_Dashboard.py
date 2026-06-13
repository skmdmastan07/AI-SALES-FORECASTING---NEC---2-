import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Executive Dashboard")

if "cleaned_data" not in st.session_state:
    st.warning("Please complete preprocessing first.")
    st.stop()

df = st.session_state["cleaned_data"]

# ---------- KPIs ----------

total_revenue = df["Revenue"].sum()
total_orders = len(df)
units_sold = df["Quantity Sold"].sum()

top_product = (
    df.groupby("Product Name")
    ["Revenue"]
    .sum()
    .idxmax()
)

top_region = (
    df.groupby("Region")
    ["Revenue"]
    .sum()
    .idxmax()
)

st.markdown("""
<div style="
background:linear-gradient(
135deg,
#1e3c72,
#2a5298,
#2096f3
);
padding:30px;
border-radius:20px;
color:white;
margin-bottom:20px;
">
<h1>📊 Executive Dashboard</h1>
<p>Business Intelligence & Sales Analytics</p>
</div>
""", unsafe_allow_html=True)

r1 = st.columns(4)

r1[0].metric(
    "Revenue",
    f"₹{total_revenue:,.0f}"
)

r1[1].metric(
    "Orders",
    total_orders
)

r1[2].metric(
    "Units Sold",
    units_sold
)

r1[3].metric(
    "Top Region",
    top_region
)

r2 = st.columns(2)

r2[0].success(
    f"🏆 Top Product : {top_product}"
)

r2[1].info(
    f"🌍 Best Region : {top_region}"
)

st.divider()

# ---------- Revenue Trend ----------

st.subheader(
    "📈 Revenue Trend"
)

trend = (
    df.groupby("Order Date")
    ["Revenue"]
    .sum()
    .reset_index()
)

fig = px.line(
    trend,
    x="Order Date",
    y="Revenue",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------- Charts ----------

col1, col2 = st.columns(2)

with col1:

    category = (
        df.groupby("Category")
        ["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category,
        names="Category",
        values="Revenue",
        hole=0.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    region = (
        df.groupby("Region")
        ["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        region,
        x="Region",
        y="Revenue",
        text_auto=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------- Top Products ----------

st.subheader(
    "🔥 Top 10 Products"
)

top_products = (
    df.groupby("Product Name")
    ["Revenue"]
    .sum()
    .reset_index()
    .sort_values(
        "Revenue",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    top_products,
    x="Revenue",
    y="Product Name",
    orientation="h"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------- Insights ----------

st.subheader(
    "💡 AI Insights"
)

st.info(f"""
• Revenue Generated: ₹{total_revenue:,.0f}

• Top Product: {top_product}

• Best Region: {top_region}

• Orders Processed: {total_orders}

• Units Sold: {units_sold}
""")