import streamlit as st
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

st.title("🤖 Model Training")

if "cleaned_data" not in st.session_state:
    st.warning("Please complete preprocessing first.")
    st.stop()

df = st.session_state["cleaned_data"].copy()

st.subheader("Model Training Dataset")
st.dataframe(df.head())

if st.button("Train Models"):

    model_df = df.copy()

    # Encode ALL object columns automatically
    object_cols = model_df.select_dtypes(
        include=["object"]
    ).columns

    for col in object_cols:

        model_df[col] = (
            model_df[col]
            .astype(str)
        )

        encoder = LabelEncoder()

        model_df[col] = encoder.fit_transform(
            model_df[col]
        )

    # Remove datetime columns
    datetime_cols = model_df.select_dtypes(
        include=["datetime64[ns]"]
    ).columns

    model_df = model_df.drop(
        columns=datetime_cols,
        errors="ignore"
    )

    # Fill null values
    model_df = model_df.fillna(0)

    if "Revenue" not in model_df.columns:
        st.error(
            "Revenue column not found."
        )
        st.stop()

    X = model_df.drop(
        columns=["Revenue"],
        errors="ignore"
    )

    y = model_df["Revenue"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Linear Regression

    lr = LinearRegression()

    lr.fit(
        X_train,
        y_train
    )

    lr_pred = lr.predict(
        X_test
    )

    lr_mae = mean_absolute_error(
        y_test,
        lr_pred
    )

    lr_r2 = r2_score(
        y_test,
        lr_pred
    )

    # Random Forest

    rf = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    rf.fit(
        X_train,
        y_train
    )

    rf_pred = rf.predict(
        X_test
    )

    rf_mae = mean_absolute_error(
        y_test,
        rf_pred
    )

    rf_r2 = r2_score(
        y_test,
        rf_pred
    )

    results = pd.DataFrame({
        "Model": [
            "Linear Regression",
            "Random Forest"
        ],
        "MAE": [
            round(lr_mae, 2),
            round(rf_mae, 2)
        ],
        "R2 Score": [
            round(lr_r2, 4),
            round(rf_r2, 4)
        ]
    })

    st.subheader("📊 Model Comparison")

    st.dataframe(results)

    if rf_r2 >= lr_r2:

        best_model = rf
        best_name = "Random Forest"

    else:

        best_model = lr
        best_name = "Linear Regression"

    joblib.dump(
        best_model,
        "models/best_model.pkl"
    )

    st.success(
        f"🏆 Best Model Selected: {best_name}"
    )

    st.session_state[
        "best_model"
    ] = best_model