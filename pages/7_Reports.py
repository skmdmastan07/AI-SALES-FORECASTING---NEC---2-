import streamlit as st
import pandas as pd

st.title("📄 Reports")

if "cleaned_data" not in st.session_state:
    st.warning("Run preprocessing first.")
    st.stop()

df = st.session_state["cleaned_data"]

st.subheader("Dataset Report")

st.dataframe(df)

csv = df.to_csv(index=False)

st.download_button(
    "⬇ Download CSV Report",
    csv,
    "sales_report.csv",
    "text/csv"
)