# Dataset: https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries
# File: ds_salaries.csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset
df = pd.read_csv("./data/ds_salaries.csv")

# === Info dasar dataset ===
print("🔎 Info Dataset")
print(df.info())
print("\n🔎 5 Data Teratas")
print(df.head())
print("\n🔎 Statistik Deskriptif")
print(df.describe(include="all"))

# === Visualisasi 1: Distribusi gaji per level pengalaman ===
plt.figure(figsize=(8,5))
sns.boxplot(x="experience_level", y="salary_in_usd", data=df, palette="Set2")
plt.title("Distribusi Gaji per Level Pengalaman")
plt.show()

# === Visualisasi 2: Top 10 job dengan gaji tertinggi ===
top_jobs_df = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False).head(10).reset_index()
plt.figure(figsize=(10,6))
sns.barplot(x="salary_in_usd", y="job_title", data=top_jobs_df, palette="Blues_r")
plt.title("Top 10 Job dengan Gaji Rata-rata Tertinggi")
plt.xlabel("Rata-rata Gaji (USD)")
plt.ylabel("Pekerjaan")
plt.show()

# === Visualisasi 3: Tren gaji per tahun ===
avg_year_df = df.groupby("work_year")["salary_in_usd"].mean().reset_index()
plt.figure(figsize=(7,5))
sns.lineplot(x="work_year", y="salary_in_usd", data=avg_year_df, marker="o")
plt.title("Tren Rata-rata Gaji per Tahun")
plt.xlabel("Tahun")
plt.ylabel("Rata-rata Gaji (USD)")
plt.show()

# === Visualisasi 4: Remote vs Onsite ===
plt.figure(figsize=(8,5))
sns.boxplot(x="remote_ratio", y="salary_in_usd", data=df, palette="coolwarm")
plt.title("Perbandingan Gaji: Remote vs Onsite")
plt.show()

# === Visualisasi 5: Gaji rata-rata berdasarkan ukuran perusahaan ===
avg_size_df = df.groupby("company_size")["salary_in_usd"].mean().reset_index()
plt.figure(figsize=(6,5))
sns.barplot(x="company_size", y="salary_in_usd", data=avg_size_df, palette="viridis")
plt.title("Rata-rata Gaji Berdasarkan Ukuran Perusahaan")
plt.xlabel("Ukuran Perusahaan")
plt.ylabel("Rata-rata Gaji (USD)")
plt.show()

# === Dashboard Interaktif ===
fig = px.box(df, x="experience_level", y="salary_in_usd", title="Distribusi Gaji per Level (Interaktif)")
fig.show()