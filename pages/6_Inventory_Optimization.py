import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("📦 Inventory Optimization")

if "cleaned_data" not in st.session_state:
    st.warning("Run preprocessing first.")
    st.stop()

df = st.session_state["cleaned_data"].copy()

revenue_col = "Revenue"
if "Sales" in df.columns:
    revenue_col = "Sales"

inventory_df = (
    df.groupby("Product Name")
    .agg({
        "Quantity Sold": "sum",
        revenue_col: "sum"
    })
    .reset_index()
)

inventory_df["Current Stock"] = (
    inventory_df["Quantity Sold"] * 0.8
).astype(int)

inventory_df["Safety Stock"] = (
    inventory_df["Quantity Sold"] * 0.20
).astype(int)

inventory_df["Reorder Point"] = (
    inventory_df["Quantity Sold"] * 0.50
).astype(int)

inventory_df["Recommended Stock"] = (
    inventory_df["Current Stock"]
    + inventory_df["Safety Stock"]
).astype(int)

inventory_df["Risk"] = (
    inventory_df["Current Stock"]
    - inventory_df["Reorder Point"]
)

# KPI Cards

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Products",
    len(inventory_df)
)

c2.metric(
    "Low Stock",
    len(
        inventory_df[
            inventory_df["Risk"] < 0
        ]
    )
)

c3.metric(
    "Inventory Units",
    int(
        inventory_df["Current Stock"].sum()
    )
)

c4.metric(
    "Inventory Value",
    f"₹{inventory_df[revenue_col].sum():,.0f}"
)

st.divider()

# Product Selector

product = st.selectbox(
    "Select Product",
    inventory_df["Product Name"]
)

selected = inventory_df[
    inventory_df["Product Name"] == product
].iloc[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Current Stock",
    int(selected["Current Stock"])
)

col2.metric(
    "Safety Stock",
    int(selected["Safety Stock"])
)

col3.metric(
    "Reorder Point",
    int(selected["Reorder Point"])
)

col4.metric(
    "Recommended",
    int(selected["Recommended Stock"])
)

# Gauge Meter

fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=float(selected["Current Stock"]),
        title={"text": "Inventory Health"},
        gauge={
            "axis": {
                "range": [
                    0,
                    float(selected["Recommended Stock"]) * 1.3
                ]
            },
            "steps": [
                {
                    "range": [
                        0,
                        float(selected["Reorder Point"])
                    ],
                    "color": "red"
                },
                {
                    "range": [
                        float(selected["Reorder Point"]),
                        float(selected["Recommended Stock"])
                    ],
                    "color": "orange"
                },
                {
                    "range": [
                        float(selected["Recommended Stock"]),
                        float(selected["Recommended Stock"]) * 1.3
                    ],
                    "color": "green"
                }
            ]
        }
    )
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="inventory_gauge"
)

# Risk Table

st.subheader("⚠ Top Inventory Risk Products")

risk_table = (
    inventory_df
    .sort_values("Risk")
    .head(10)
)

st.dataframe(
    risk_table,
    use_container_width=True
)

# Inventory Chart

st.subheader("📊 Top 15 Inventory Comparison")

top_inventory = (
    inventory_df
    .sort_values(
        revenue_col,
        ascending=False
    )
    .head(15)
)

fig2 = px.bar(
    top_inventory,
    x="Product Name",
    y=[
        "Current Stock",
        "Reorder Point"
    ],
    barmode="group",
    title="Top 15 Products Inventory"
)

fig2.update_layout(
    xaxis_tickangle=-45
)

st.plotly_chart(
    fig2,
    use_container_width=True,
    key="inventory_comparison"
)