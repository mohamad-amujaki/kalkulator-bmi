"""Import Streamlit"""
import streamlit as st

# Menampilkan judul aplikasi
st.sidebar.title("Silahkan isi data berikut")
nama = st.sidebar.text_input("Nama:")
jenis_kelamin = st.sidebar.radio("Jenis Kelamin:", ["Laki-laki", "Perempuan"])
berat = st.sidebar.number_input("Masukkan Berat Badan (kg)", min_value=1.0, step=0.1)
tinggi = st.sidebar.number_input("Masukkan Tinggi Badan (cm)", min_value=1.0, step=0.1)

# Siapkan fungsi untuk popup dialog yang menampilkan perhitungan BMI
def tunjukkan_hasil_perhitungan_bmi(nama_pengguna, gender, nilai_bmi, kategori_bmi, saran_bmi):
    """Fungsi untuk menampilkan perhitungan BMI"""
    st.write(f"Halo {nama_pengguna}")
    st.write(f"Jenis Kelamin: {gender}")
    st.divider()
    st.metric(label="Nilai BMI: ", value=f"{nilai_bmi:.2f}")
    st.info(f"Kategori BMI: **{kategori_bmi}** \n\n**Saran**: {saran_bmi}")
if st.sidebar.button("Hitung BMI"):
    # (Logika perhitungan kita yang sebelumnya diletakkan di sini)
    if len(nama) < 3:
        st.error("Nama minimal terdiri dari 3 karakter")
    # Konversi Tinggi ke dalam Meter
    else:
        tinggi_m = tinggi / 100

        # Menghitung BMI
        bmi = berat / (tinggi_m ** 2)
        if bmi < 18.5:
            KATEGORI = "Berat Badan Kurang (Underweight)"
            SARAN = "Perbanyak asupan nutrisi dan kalori sehat."
        elif 18.5 <= bmi < 24.9:
            KATEGORI = "Berat Badan Ideal (Normal)"
            SARAN = "Pertahankan pola makan seimbang dan olahraga rutin."
        elif 25 <= bmi < 29.9:
            KATEGORI = "Berat Badan Berlebih (Overweight)"
            SARAN = "Cobalah untuk lebih aktif bergerak dan kurangi gula."
        else:
            KATEGORI = "Obesitas"
            SARAN = "Disarankan berkonsultasi dengan tenaga medis."
        # Memanggil fungsi popup
        tunjukkan_hasil_perhitungan_bmi(nama, jenis_kelamin, bmi, KATEGORI, SARAN)

# Menambahkan garis pembatas agar tampilan lebih teratur
st.sidebar.divider()

# Menampilkan informasi tambahan
st.sidebar.markdown("""
### Tentang BMI 💡
**Body Mass Index (BMI)** adalah cara sederhana untuk memantau status gizi orang dewasa. 

*   **Penting:** Skor ini tidak memperhitungkan massa otot, kepadatan tulang, dan komposisi tubuh secara keseluruhan.
""")

st.markdown("""
### Selamat Datang!
Silakan isi data diri pada **panel di sebelah kiri** untuk mengetahui skor BMI dan kategori kesehatan Anda.
""")
