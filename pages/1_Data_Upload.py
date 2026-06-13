import streamlit as st
import pandas as pd

st.title("📂 Data Upload")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    else:
        df = pd.read_excel(uploaded_file)

    st.session_state["raw_data"] = df

    st.success("Dataset Uploaded Successfully")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric(
        "Missing Values",
        df.isnull().sum().sum()
    )

    st.subheader("Dataset Preview")

    st.dataframe(df.head())