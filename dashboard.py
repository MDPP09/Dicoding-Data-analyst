import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("main_dataset.csv")  # Ganti dengan path dataset Anda

df = load_data()

# Sidebar
st.sidebar.title("📊 Dashboard E-Commerce")
st.sidebar.write("Dashboard ini adalah hasil analisis data penjualan marketplace.")

# Tombol untuk mengunduh dataset
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode("utf-8")

csv = convert_df_to_csv(df)
st.sidebar.download_button(label="📥 Download Dataset", data=csv, file_name="main_dataset.csv", mime="text/csv")

# Menampilkan preview dataset
st.subheader("📄 Preview Dataset")
st.dataframe(df.head(10))  # Menampilkan 10 data pertama

# Distribusi Jumlah Cicilan
st.subheader("📊 Distribusi Jumlah Cicilan dalam Pembayaran")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=df['payment_installments'].value_counts().sort_index().index, 
            y=df['payment_installments'].value_counts().sort_index().values, 
            palette="coolwarm", ax=ax)
plt.xlabel("Jumlah Cicilan")
plt.ylabel("Jumlah Transaksi")
st.pyplot(fig)

# Top 10 Kota dengan Transaksi Terbanyak
st.subheader("🏙️ Top 10 Kota dengan Jumlah Pembelian Terbanyak")
top_cities = df['customer_city'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=top_cities.values, y=top_cities.index, palette="Blues_r", ax=ax)
plt.xlabel("Jumlah Transaksi")
plt.ylabel("Kota")
st.pyplot(fig)

# Top 10 Metode Pembayaran
st.subheader("💳 Top 10 Metode Pembayaran Terbanyak")
top_payment_methods = df['payment_type'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=top_payment_methods.index, y=top_payment_methods.values, palette="viridis", ax=ax)
plt.xlabel("Metode Pembayaran")
plt.ylabel("Jumlah Transaksi")
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("© 2025 Dashboard E-Commerce - Dibuat dengan ❤️ oleh Muhammad Dafa Putra")
