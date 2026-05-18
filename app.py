import streamlit as st
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Smart ETL Data Cleaner",
    layout="wide"
)

st.title("📊 Smart ETL Data Cleaner")

st.write("Upload a CSV or Excel file for data analysis.")

# -----------------------------
# FILE UPLOAD
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

# -----------------------------
# PROCESS FILE
# -----------------------------
if uploaded_file is not None:

    try:
        # Read CSV
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        # Read Excel
        else:
            df = pd.read_excel(uploaded_file, encoding='latin1')

        st.success("✅ File uploaded successfully!")

        # -----------------------------
        # DATA PREVIEW
        # -----------------------------
        st.subheader("📌 Dataset Preview")

        st.dataframe(df.head())

        # -----------------------------
        # COLUMN NAMES
        # -----------------------------
        st.subheader("📌 Column Names")

        st.write(list(df.columns))

        # -----------------------------
        # DATASET INFO
        # -----------------------------
        st.subheader("📌 Dataset Information")

        info_df = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Missing Values": df.isnull().sum().values
        })

        st.dataframe(info_df)

        # -----------------------------
        # DUPLICATES
        # -----------------------------
        st.subheader("📌 Duplicate Records")

        duplicate_count = df.duplicated().sum()

        st.write(f"Number of duplicate rows: {duplicate_count}")

        # -----------------------------
        # SHAPE
        # -----------------------------
        st.subheader("📌 Dataset Shape")

        st.write(f"Rows: {df.shape[0]}")
        st.write(f"Columns: {df.shape[1]}")
                # =============================
        # TRANSFORMATION SECTION
        # =============================

        st.header("⚙️ Data Transformation Options")

        transformed_df = df.copy()

        # -----------------------------
        # HANDLE MISSING VALUES
        # -----------------------------
        st.subheader("Handle Missing Values")

        missing_strategy = st.selectbox(
            "Choose strategy",
            [
                "Do Nothing",
                "Fill Numeric with Mean",
                "Fill Numeric with Median",
                "Fill All with Mode",
                "Fill Categorical with 'Unknown'",
                "Drop Missing Rows"
            ]
        )

        numeric_cols = transformed_df.select_dtypes(include=['number']).columns
        categorical_cols = transformed_df.select_dtypes(exclude=['number']).columns

        if missing_strategy == "Fill Numeric with Mean":

            transformed_df[numeric_cols] = transformed_df[numeric_cols].fillna(
                transformed_df[numeric_cols].mean()
            )

            st.success("✅ Numeric missing values filled using Mean")

        elif missing_strategy == "Fill Numeric with Median":

            transformed_df[numeric_cols] = transformed_df[numeric_cols].fillna(
                transformed_df[numeric_cols].median()
            )

            st.success("✅ Numeric missing values filled using Median")

        elif missing_strategy == "Fill All with Mode":

            for col in transformed_df.columns:
                transformed_df[col] = transformed_df[col].fillna(
                    transformed_df[col].mode()[0]
                )

            st.success("✅ All missing values filled using Mode")

        elif missing_strategy == "Fill Categorical with 'Unknown'":

            transformed_df[categorical_cols] = transformed_df[categorical_cols].fillna(
                "Unknown"
            )

            st.success("✅ Categorical missing values filled with 'Unknown'")

        elif missing_strategy == "Drop Missing Rows":

            transformed_df = transformed_df.dropna()

            st.success("✅ Missing rows dropped")

        # -----------------------------
        # REMOVE DUPLICATES
        # -----------------------------
        st.subheader("Duplicate Handling")

        remove_duplicates = st.checkbox("Remove Duplicate Rows")

        if remove_duplicates:
            before = transformed_df.shape[0]

            transformed_df = transformed_df.drop_duplicates()

            after = transformed_df.shape[0]

            st.success(f"✅ Removed {before - after} duplicate rows")

        # -----------------------------
        # CLEAN COLUMN NAMES
        # -----------------------------
        st.subheader("Column Name Cleaning")

        clean_columns = st.checkbox(
            "Convert column names to lowercase and replace spaces"
        )

        if clean_columns:
            transformed_df.columns = (
                transformed_df.columns
                .str.strip()
                .str.lower()
                .str.replace(" ", "_")
                .str.replace("-", "_")
            )

            st.success("✅ Column names cleaned")

        # -----------------------------
        # SHOW TRANSFORMED DATA
        # -----------------------------
        st.subheader("📌 Transformed Dataset Preview")

        st.dataframe(transformed_df.head(20))
        st.write("Remaining Missing Values:")
        st.write(transformed_df.isnull().sum())

        # -----------------------------
        # DOWNLOAD CLEANED FILE
        # -----------------------------
        csv = transformed_df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="📥 Download Cleaned CSV",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"❌ Error: {e}")
        