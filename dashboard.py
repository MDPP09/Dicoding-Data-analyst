import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
all_df = pd.read_csv("main_dataset.csv")

# Convert order timestamp to datetime
all_df["order_purchase_timestamp"] = pd.to_datetime(all_df["order_purchase_timestamp"])
all_df["order_date"] = all_df["order_purchase_timestamp"].dt.date
all_df["order_year"] = all_df["order_purchase_timestamp"].dt.year
all_df["order_month"] = all_df["order_purchase_timestamp"].dt.month

st.title("Dashboard E-Commerce")

# Sidebar filter
year_filter = st.sidebar.selectbox("Pilih Tahun", sorted(all_df["order_year"].unique()), index=0)
month_filter = st.sidebar.selectbox("Pilih Bulan", sorted(all_df["order_month"].unique()), index=0)

df_filtered = all_df[(all_df["order_year"] == year_filter) & (all_df["order_month"] == month_filter)]

# 1️⃣ Metode Pembayaran yang Paling Dominan
st.subheader("Metode Pembayaran yang Paling Dominan")
payment_counts = df_filtered["payment_type"].value_counts()
if not payment_counts.empty:
    fig, ax = plt.subplots()
    payment_counts.plot(kind="bar", color="skyblue", ax=ax)
    ax.set_xlabel("Metode Pembayaran")
    ax.set_ylabel("Jumlah Penggunaan")
    ax.set_title("Distribusi Metode Pembayaran")
    st.pyplot(fig)
else:
    st.write("Tidak ada data untuk bulan dan tahun yang dipilih.")

# 2️⃣ Hubungan antara Harga Produk dan Biaya Pengiriman
st.subheader("Hubungan antara Harga Produk dan Biaya Pengiriman")
fig, ax = plt.subplots()
ax.scatter(df_filtered["price"], df_filtered["freight_value"], alpha=0.5, color="purple")
ax.set_xlabel("Harga Produk (BRL)")
ax.set_ylabel("Biaya Pengiriman (BRL)")
ax.set_title("Scatter Plot: Harga Produk vs Biaya Pengiriman")
st.pyplot(fig)

# 3️⃣ Tren Transaksi dari Waktu ke Waktu
st.subheader("Tren Transaksi dari Waktu ke Waktu")
order_trend = df_filtered.groupby("order_date")["payment_value"].sum()
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(order_trend.index, order_trend.values, marker="o", linestyle="-", color="red")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Total Nilai Transaksi (BRL)")
ax.set_title("Tren Nilai Transaksi Seiring Waktu")
plt.xticks(rotation=45)
ax.legend(["Total Transaksi"])
ax.grid()
st.pyplot(fig)

# 4️⃣ Jumlah Angsuran Berdasarkan Metode Pembayaran
st.subheader("Jumlah Angsuran Berdasarkan Metode Pembayaran")
installments_avg = df_filtered.groupby("payment_type")["payment_installments"].mean().sort_values()
if not installments_avg.empty:
    fig, ax = plt.subplots()
    installments_avg.plot(kind="bar", color="green", ax=ax)
    ax.set_xlabel("Metode Pembayaran")
    ax.set_ylabel("Rata-rata Jumlah Angsuran")
    ax.set_title("Rata-rata Jumlah Angsuran per Metode Pembayaran")
    st.pyplot(fig)
else:
    st.write("Tidak ada data untuk bulan dan tahun yang dipilih.")

st.write("\n\n**Gunakan sidebar untuk memfilter berdasarkan tahun dan bulan!**")

st.markdown("© 2025, Dashboard E-Commerce Analysis dafa putra. All Rights Reserved.")