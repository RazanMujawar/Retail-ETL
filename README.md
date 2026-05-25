# 📊 Smart ETL Data Cleaner & AI Dashboard Generator

An AI-powered ETL and analytics application built using **Python, Streamlit, Pandas, and Gemini AI**.

This project allows users to upload CSV or Excel datasets, clean and transform data interactively, and automatically generate AI-powered dashboards with dynamic visualizations and business insights.

---

# 🚀 Features

## 📂 File Upload

* Upload CSV and Excel files
* Automatic file validation
* Handles encoding issues

---

# 📈 Dataset Analysis

* Dataset preview
* Column information
* Missing value detection
* Duplicate value detection
* Unique value analysis
* Data quality score calculation

---

# ⚙️ Data Transformation

Users can clean datasets interactively using:

* Fill missing values with Mean
* Fill missing values with Median
* Fill missing values with Mode
* Fill categorical values with "Unknown"
* Drop missing rows
* Remove duplicate rows
* Clean column names

---

# 🤖 AI Dataset Assistant

Powered by **Google Gemini AI**

The AI system:

* Understands dataset structure
* Recommends meaningful visualizations
* Generates business-friendly insights
* Dynamically creates dashboards

---

# 📊 AI-Powered Dynamic Dashboard

The application automatically generates:

* Bar charts
* Line charts
* Scatter plots
* Pie charts

Based on the uploaded dataset structure.

---

# 🎛️ Interactive Dashboard Filters

Dynamic filters are automatically generated for:

* Categorical columns
* Low-cardinality fields

Charts update interactively based on selected filters.

---

# 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Matplotlib
* NumPy
* Google Gemini API
* dotenv

---

# 📁 Project Structure

```bash
Smart-ETL-Project/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
│
├── scripts/
│   ├── extract.py
│   └── transform.py
│
└── data/
```

---

# ⚡ Installation

## 1. Clone Repository

```bash
git clone <your_repo_link>
cd Smart-ETL-Project
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Setup Environment Variables

Create `.env`

```env
GEMINI_API_KEY=your_api_key_here
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 📸 Future Improvements

* Conversational AI dataset querying
* PDF report generation
* Advanced dashboard styling
* Chart export functionality
* AI-based anomaly detection
* Dashboard caching optimization

---

# 👨‍💻 Author

Razan Mujawar

---

# ⭐ Project Goal

The goal of this project is to combine:

* ETL pipelines
* Data cleaning
* AI-powered analytics
* Dynamic dashboard generation

into a single intelligent analytics platform.
