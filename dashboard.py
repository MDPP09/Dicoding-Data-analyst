import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Streamlit App
st.set_page_config(page_title="Analisis data E-commerce", layout="wide")
st.title("📊 Analisis data E-commerce")

# Sidebar

st.sidebar.header("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Preview Dataset", "Visualization & Analysis", "Conclusion"])
st.sidebar.markdown("---")
st.sidebar.write("📌 **Copyright Dafa putra © 2025**")
st.sidebar.markdown("[📂 dataset yang digunakan](https://drive.google.com/file/d/1MsAjPM7oKtVfJL_wRp1qmCajtSG1mdcK/view)")

# Load Data
df = pd.read_csv('main_dataset.csv')

if page == "Preview Dataset":
    st.subheader("📌 Preview Dataset")
    st.dataframe(df.head(20))

elif page == "Visualization & Analysis":
    st.markdown("### 📅 Tren Belanja Berdasarkan Hari")
    purchase_trend = df.groupby('order_purchase_day').size().reset_index(name='count')
    date_trend = df.groupby('order_purchase_date').size().reset_index(name='count')
    min_purchase_date = date_trend.loc[date_trend['count'].idxmin()]

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=purchase_trend['order_purchase_day'], y=purchase_trend['count'], palette="coolwarm", ax=ax)
    ax.set_title("Tren Belanja Berdasarkan Hari")
    ax.set_xlabel("Hari")
    ax.set_ylabel("Jumlah Transaksi")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)
    st.write(f"📉 **Tanggal dengan jumlah transaksi paling sedikit**: {min_purchase_date['order_purchase_date']} dengan {min_purchase_date['count']} transaksi.")

    st.markdown("### 🏙️ Kota dengan Pembelian Terbanyak Setiap Bulan")
    top_cities_monthly = df.groupby(['order_purchase_month', 'customer_city']).size().reset_index(name='count')
    top_cities_monthly = top_cities_monthly.sort_values(['order_purchase_month', 'count'], ascending=[True, False]).groupby('order_purchase_month').head(2)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=top_cities_monthly['customer_city'], y=top_cities_monthly['count'], palette="Blues_r", ax=ax)
    ax.set_xlabel("Kota")
    ax.set_ylabel("Jumlah Transaksi")
    ax.set_title("Dua Kota dengan Pembelian Terbanyak Setiap Bulan")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

    st.markdown("### 💳 Metode Pembayaran Terbanyak Setiap Hari")
    payment_trend = df.groupby(['order_purchase_day', 'payment_type']).size().reset_index(name='count')
    payment_trend = payment_trend.sort_values(['order_purchase_day', 'count'], ascending=[True, False]).groupby('order_purchase_day').head(3)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=payment_trend['payment_type'], y=payment_trend['count'], palette="viridis", ax=ax)
    ax.set_xlabel("Metode Pembayaran")
    ax.set_ylabel("Jumlah Transaksi")
    ax.set_title("Tiga Metode Pembayaran Terbanyak Setiap Hari")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

elif page == "Conclusion":
    st.subheader("📌 Conclusion")
    
    st.markdown("### Conclution pertanyaan 1")
    st.write("**Bagaimana trend belanja berdasarkan hari dan tanggal berapakah yang paling sedikit belanjanya?**")
    st.write("Hari Selasa adalah hari yang memiliki jumlah transaksi terbanyak di antara hari lainnya, dan hari Sabtu memiliki jumlah transaksi paling sedikit.")
    
    st.markdown("### Conclution pertanyaan 2")
    st.write("**Kota manakah dengan pembelian terbanyak setiap bulannya?**")
    st.write("Kota Sao Paulo adalah kota dengan pembelian terbanyak setiap bulannya, disusul dengan kota Rio de Janeiro dan kota-kota lainnya.")
    
    st.markdown("### Conclution pertanyaan 3")
    st.write("**Metode pembayaran apakah yang paling banyak digunakan setiap harinya?**")
    st.write("Credit card menjadi opsi pembayaran terbanyak setiap hari, disusul dengan boleto kemudian voucher.")