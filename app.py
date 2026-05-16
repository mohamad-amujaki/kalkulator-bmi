"""Import Streamlit"""
import streamlit as st

# Menampilkan judul aplikasi
st.title("Kalkulator BMI Interaktif")

# Membuat input nama pengguna
nama = st.text_input("Masukkan Nama Anda")

# Membuat input jenis kelamin (menggunakan st.selectbox atau st.radio)
jenis_kelamin = st.selectbox("Pilih Jenis Kelamin", ["Laki-laki", "Perempuan"])

# Membuat input angka untuk berat badan
berat = st.number_input("Masukkan Berat Badan (kg)", min_value=1.0, step=0.1)

# Membuat input angka untuk tinggi badan
tinggi = st.number_input("Masukkan Tinggi Badan (cm)", min_value=1.0, step=0.1)

# Konversi Tinggi ke dalam Meter
tinggi_m = tinggi / 100

# Menghitung BMI
bmi = berat / (tinggi_m ** 2)

# Tampilkan perhitungan BMI jika nama telah terisi minimal 3 huruf
if len(nama) >= 3:
    # Menampilkan hasil perhitungan BMI ke layar
    st.success(f"BMI Anda adalah: {bmi:.2f}")
    if bmi < 18.5:
        KATEGORI = "Berat Badan Kurang (Underweight)"
        st.warning(f"Predikat BMI Sdr. {nama} saat ini {KATEGORI}")
    elif 18.5 <= bmi < 24.9:
        KATEGORI = "Berat Badan Ideal (Normal)"
        st.success(f"Predikat BMI Sdr. {nama} saat ini {KATEGORI}")
    elif 25 <= bmi < 29.9:
        KATEGORI = "Berat Badan Berlebih (Overweight)"
        st.warning(f"Predikat BMI Sdr. {nama} saat ini {KATEGORI}")
    else:
        KATEGORI = "Obesitas"
        st.error(f"Predikat BMI Sdr. {nama} saat ini {KATEGORI}")
