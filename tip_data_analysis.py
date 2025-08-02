import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
df.head()

df.info()
df.describe()
df.isnull().sum().sum()

print(df[df.isnull().any(axis=1)])

min_total_bill = df["total_bill"].min()
max_total_bill = df["total_bill"].max()
min_tip = df["tip"].min()
max_tip = df["tip"].max()

print(f"Minimum total bill: {min_total_bill}, Maximum total bill: {max_total_bill}")
print(f"Minimum tip: {min_tip}, Maximum tip: {max_tip}")

sns.scatterplot(data=df, x="total_bill", y="tip")
plt.title("Tip vs Total Bill")
plt.show()

correlation = df["total_bill"].corr(df["tip"])
print("Correlation between bill and tip: ", correlation)
