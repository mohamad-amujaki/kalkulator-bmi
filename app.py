"""Import Streamlit"""
import streamlit as st

# Menampilkan judul aplikasi
st.title("Kalkulator BMI Interaktif")

# Membuat 2 Column agar lebih rapi
col_nama, col_gender = st.columns(2)
with col_nama:
    # Membuat input nama pengguna
    nama = st.text_input("Masukkan Nama Anda")
with col_gender:
    # Membuat input jenis kelamin (menggunakan st.selectbox atau st.radio)
    jenis_kelamin = st.selectbox("Pilih Jenis Kelamin", ["Laki-laki", "Perempuan"])

# Membuat 2 Column agar lehi rapi
col_berat, col_tinggi = st.columns(2)
with col_berat:
    # Membuat input angka untuk berat badan
    berat = st.number_input("Masukkan Berat Badan (kg)", min_value=1.0, step=0.1)
with col_tinggi:
    # Membuat input angka untuk tinggi badan
    tinggi = st.number_input("Masukkan Tinggi Badan (cm)", min_value=1.0, step=0.1)

# Siapkan fungsi untuk popup dialog yang menampilkan perhitungan BMI
@st.dialog("Perhitungan BMI")
def tunjukkan_hasil_perhitungan_bmi(nama_pengguna, gender, nilai_bmi, kategori_bmi):
    """Fungsi untuk menampilkan perhitungan BMI"""
    st.write(f"Halo {nama_pengguna}")
    st.write(f"Jenis Kelamin: {gender}")
    st.divider()
    st.metric(label="Nilai BMI: ", value=f"{nilai_bmi:.2f}")
    st.info(f"Kategori BMI: **{kategori_bmi}**")

# Membuat Tombol untuk memicu Perhitungan BMI
if st.button("Hitung BMI"):
    # (Logika perhitungan kita yang sebelumnya diletakkan di sini)
    # Konversi Tinggi ke dalam Meter
    tinggi_m = tinggi / 100

    # Menghitung BMI
    bmi = berat / (tinggi_m ** 2)
    if bmi < 18.5:
        KATEGORI = "Berat Badan Kurang (Underweight)"
    elif 18.5 <= bmi < 24.9:
        KATEGORI = "Berat Badan Ideal (Normal)"
    elif 25 <= bmi < 29.9:
        KATEGORI = "Berat Badan Berlebih (Overweight)"
    else:
        KATEGORI = "Obesitas"
    # Memanggil fungsi popup
    tunjukkan_hasil_perhitungan_bmi(nama, jenis_kelamin, bmi, KATEGORI)
