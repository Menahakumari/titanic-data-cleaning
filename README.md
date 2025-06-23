# Titanic-data-cleaning
# 🚢 Titanic Data Cleaning & Preprocessing 

This project contains a complete data cleaning and preprocessing pipeline for the Titanic dataset. The goal is to prepare the raw data for machine learning models by handling missing values, encoding categorical variables, scaling numerical features, and removing outliersrs.

---

## 📌 Objectives

- Load and explore the Titanic dataset
- Handle missing values (numeric and categorical)
- Encode categorical variables (Sex, Embarked)
- Standardize numerical features (Age, Fare)
- Detect and remove outliers using the IQR method
- Analyze correlation with the target variable `Survived`

---

## 📁 Project Structure


---

## 🛠️ Tools & Libraries Used

- **Pandas** – data manipulation
- **NumPy** – numerical operations
- **Seaborn / Matplotlib** – data visualization
- **Scikit-learn** – preprocessing tools (LabelEncoder, StandardScaler)

---

## 📊 Key Techniques Applied

### 🔹 Missing Value Handling
- `Age` → filled with **median**
- `Embarked` → filled with **mode**
- `Cabin` → dropped due to excessive missing values

### 🔹 Categorical Encoding
- `Sex` → **Label Encoding** (female: 0, male: 1)
- `Embarked` → **One-Hot Encoding**

### 🔹 Feature Scaling
- `Age` and `Fare` standardized using **StandardScaler**

### 🔹 Outlier Removal
- **Boxplots** visualized distributions
- Used **Interquartile Range (IQR)** method to drop extreme values

---

## 🔗 Dataset Source

[Titanic Dataset – https://www.kaggle.com/datasets/yasserh/titanic-dataset

---

## ✅ Outcome

After this task:
- The dataset is clean, numeric, and standardized.
- It is ready for use in machine learning models (e.g., Logistic Regression, Decision Trees).

---

## 📬 Contact

**Menaha Kumari K.K.**  
AI & ML Intern @ Elevate Labs  
