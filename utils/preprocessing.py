import pandas as pd
import numpy as np


def clean_data(df):

    df = df.copy()

    # =====================
    # STANDARDIZE COLUMNS
    # =====================

    df.columns = df.columns.str.strip()

    # Sales → Revenue

    if "Sales" in df.columns and "Revenue" not in df.columns:
        df["Revenue"] = df["Sales"]

    # Product Name

    if "Product Name" not in df.columns:
        df["Product Name"] = "Unknown Product"

    # Category

    if "Category" not in df.columns:
        df["Category"] = "General"

    # Region

    if "Region" not in df.columns:
        df["Region"] = "Unknown"

    # Quantity Sold

    if "Quantity Sold" not in df.columns:

        np.random.seed(42)

        df["Quantity Sold"] = np.random.randint(
            1,
            20,
            len(df)
        )

    # Inventory Level

    if "Inventory Level" not in df.columns:

        np.random.seed(42)

        df["Inventory Level"] = np.random.randint(
            50,
            120,
            len(df)
        )

    # Promotion Flag

    if "Promotion Flag" not in df.columns:

        np.random.seed(42)

        df["Promotion Flag"] = np.random.randint(
            0,
            2,
            len(df)
        )

    # Holiday Indicator

    if "Holiday Indicator" not in df.columns:

        np.random.seed(42)

        df["Holiday Indicator"] = np.random.randint(
            0,
            2,
            len(df)
        )

    rows_before = len(df)

    duplicates = df.duplicated().sum()

    df = df.drop_duplicates()

    # =====================
    # MISSING VALUES
    # =====================

    numeric_cols = df.select_dtypes(
        include=np.number
    ).columns

    for col in numeric_cols:

        df[col] = df[col].fillna(
            df[col].median()
        )

    object_cols = df.select_dtypes(
        include="object"
    ).columns

    for col in object_cols:

        df[col] = df[col].fillna(
            "Unknown"
        )

    rows_after = len(df)

    return (
        df,
        rows_before,
        rows_after,
        duplicates
    )


def create_date_features(df):

    date_column = None

    possible_dates = [
        "Order Date",
        "Date",
        "order_date",
        "date"
    ]

    for col in possible_dates:

        if col in df.columns:

            date_column = col
            break

    if date_column:

        df[date_column] = pd.to_datetime(
            df[date_column],
            errors="coerce"
        )
        
        df = df.dropna(
            subset=[date_column]
        )
        
        df["Order Date"] = df[date_column]

        df["Year"] = (
            df["Order Date"].dt.year
        )

        df["Month"] = (
            df["Order Date"].dt.month
        )

        df["Quarter"] = (
            df["Order Date"].dt.quarter
        )

        df["Week"] = (
            df["Order Date"]
            .dt.isocalendar()
            .week
        )

    return df