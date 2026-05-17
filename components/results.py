"""Results display components."""
def tampilkan_hasil_bmi(
    nama_pengguna: str,
    gender: str,
    nilai_bmi: float,
    kategori_bmi: str,
    saran_bmi: str):
    """Fungsi khusus untuk mengurus tampilan (render) hasil BMI ke layar utama."""
    import streamlit as st
    st.header("📊 Hasil Analisis Kesehatan")
    st.subheader(f"Halo, {nama_pengguna}!")
    st.write(f"Jenis Kelamin: {gender}")
    st.divider()
    # Menampilkan metrik utama
    st.metric(label="Nilai BMI Anda", value=f"{nilai_bmi:.2f}")
    # Menggunakan \n\n untuk newline Markdown yang aman di st.info
    st.info(f"Kategori BMI: **{kategori_bmi}**\n\n**Saran**: {saran_bmi}")
    # Menampilkan progress posisi BMI
    st.write("Posisi BMI Anda dalam skala umum (maksimal skala 40):")
    progress_bmi = min(nilai_bmi / 40, 1.0)
    st.progress(progress_bmi)

def tampilkan_welcome():
    """Display welcome page when no calculation is triggered."""
    import streamlit as st
    st.title("🏃‍♂️ Kalkulator BMI")
    st.markdown("""
    ### Selamat Datang!
    Silakan isi data diri pada **panel di sebelah kiri**, lalu klik tombol **Hitung BMI** untuk mengetahui skor BMI dan kategori kesehatan Anda.
    """)
