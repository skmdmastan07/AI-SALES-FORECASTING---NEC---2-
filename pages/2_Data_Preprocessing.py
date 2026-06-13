import streamlit as st
import pandas as pd
from utils.preprocessing import (
    clean_data,
    create_date_features
)

st.title("🧹 Data Preprocessing")

if "raw_data" not in st.session_state:

    st.warning(
        "Please upload dataset first."
    )

    st.stop()

df = st.session_state["raw_data"]

st.subheader("Raw Dataset")

st.dataframe(df.head())

if st.button("Run Preprocessing"):

    cleaned_df, before, after, duplicates = clean_data(df)

    cleaned_df = create_date_features(
        cleaned_df
    )

    st.session_state[
        "cleaned_data"
    ] = cleaned_df

    st.success(
        "Preprocessing Completed"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Rows Before",
        before
    )

    col2.metric(
        "Rows After",
        after
    )

    col3.metric(
        "Duplicates Removed",
        duplicates
    )

    st.subheader(
        "Processed Dataset"
    )

    st.dataframe(
        cleaned_df.head()
    )