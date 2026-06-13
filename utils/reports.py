import streamlit as st
import pandas as pd

st.title("📄 Reports")

if "cleaned_data" not in st.session_state:
    st.warning("Please run preprocessing first.")
    st.stop()

df = st.session_state["cleaned_data"]

st.subheader("Dataset Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Records",
    len(df)
)

col2.metric(
    "Columns",
    len(df.columns)
)

col3.metric(
    "Missing Values",
    int(df.isnull().sum().sum())
)

st.divider()

st.subheader("Preview Report Data")

st.dataframe(
    df.head(50),
    use_container_width=True
)

csv = df.to_csv(index=False)

st.download_button(
    label="⬇ Download Report (CSV)",
    data=csv,
    file_name="sales_report.csv",
    mime="text/csv"
)

st.success(
    "Report generated successfully."
)