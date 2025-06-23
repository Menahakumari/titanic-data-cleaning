import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
df = pd.read_csv("/content/Titanic-Dataset.csv")
print("Basic Info:\n")
print(df.info())
print("\nMissing Values:\n", df.isnull().sum())
#Handle missing values
#Fill Age with median
if 'Age' in df.columns:
    df['Age'].fillna(df['Age'].median(), inplace=True)
#Fill Embarked with mode
if 'Embarked' in df.columns:
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
#nulls
if 'Cabin' in df.columns:
    df.drop(columns=['Cabin'], inplace=True)

#Encoding
if 'Sex' in df.columns:
    le = LabelEncoder()
    df['Sex'] = le.fit_transform(df['Sex'])  # female=0, male=1

if 'Embarked' in df.columns:
    df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
drop_cols = ['Name', 'Ticket', 'PassengerId']
df.drop(columns=[col for col in drop_cols if col in df.columns], inplace=True)

#Normalize / Standardize numeric features
scaler = StandardScaler()
num_cols = ['Age', 'Fare']  
for col in num_cols:
    if col in df.columns:
        df[col] = scaler.fit_transform(df[[col]])

# Detection & visualize outliers
plt.figure(figsize=(10,4))
for i, col in enumerate(num_cols):
    if col in df.columns:
        plt.subplot(1, len(num_cols), i+1)
        sns.boxplot(x=df[col])
        plt.title(f"Boxplot of {col}")
plt.tight_layout()
plt.show()
# Remove outliers 
for col in num_cols:
    if col in df.columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[col] >= Q1 - 1.5*IQR) & (df[col] <= Q3 + 1.5*IQR)]
#Target (Survived)
numeric_df = df.select_dtypes(include=[np.number])
if 'Survived' in numeric_df.columns:
    print("\nCorrelations with Survived:\n", numeric_df.corr()['Survived'].sort_values())
else:
    print("Column 'Survived' not found for correlation analysis.")

#Final Data Overview(optional)
print("\nFinal Dataset Shape:", df.shape)
print(df.head())
