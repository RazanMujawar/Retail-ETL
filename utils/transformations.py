#utils/ transformations.py

import pandas as pd


def apply_missing_strategy(df, strategy):

    transformed_df = df.copy()

    numeric_cols = transformed_df.select_dtypes(
        include=['number']
    ).columns

    categorical_cols = transformed_df.select_dtypes(
        exclude=['number']
    ).columns

    if strategy == "Fill Numeric with Mean":

        transformed_df[numeric_cols] = (
            transformed_df[numeric_cols]
            .fillna(transformed_df[numeric_cols].mean())
        )

    elif strategy == "Fill Numeric with Median":

        transformed_df[numeric_cols] = (
            transformed_df[numeric_cols]
            .fillna(transformed_df[numeric_cols].median())
        )

    elif strategy == "Fill All with Mode":

        for col in transformed_df.columns:

            transformed_df[col] = (
                transformed_df[col]
                .fillna(transformed_df[col].mode()[0])
            )

    elif strategy == "Fill Categorical with 'Unknown'":

        transformed_df[categorical_cols] = (
            transformed_df[categorical_cols]
            .fillna("Unknown")
        )

    elif strategy == "Drop Missing Rows":

        transformed_df = transformed_df.dropna()

    return transformed_df