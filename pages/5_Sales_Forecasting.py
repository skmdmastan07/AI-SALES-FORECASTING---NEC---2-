import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Sales Forecasting")

if "cleaned_data" not in st.session_state:
    st.warning("Run preprocessing first.")
    st.stop()

df = st.session_state["cleaned_data"]

forecast_df = df[["Order Date", "Revenue"]].copy()

forecast_df["Predicted Revenue"] = (
    forecast_df["Revenue"].rolling(
        3,
        min_periods=1
    ).mean()
)

st.subheader("Actual vs Forecast")

fig = px.line(
    forecast_df,
    x="Order Date",
    y=["Revenue", "Predicted Revenue"]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(forecast_df)