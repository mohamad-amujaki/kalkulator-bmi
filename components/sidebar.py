"""Sidebar components for user input."""


def render_sidebar():
    """Render sidebar input components and return user data."""
    import streamlit as st
    st.sidebar.title("Silahkan isi data berikut")

    nama = st.sidebar.text_input("Nama:", placeholder="Masukkan nama Anda")
    jenis_kelamin = st.sidebar.radio("Jenis Kelamin:", ["Laki-laki", "Perempuan"])

    # Memberikan nilai default (value) yang logis agar aplikasi tidak langsung menghitung angka 1.0
    berat = st.sidebar.number_input("Masukkan Berat Badan (kg)",
                                    min_value=1.0, value=60.0, step=0.1)
    tinggi = st.sidebar.number_input("Masukkan Tinggi Badan (cm)",
                                    min_value=1.0, value=165.0, step=0.1)

    # Menambahkan type="primary" agar tombol utama terlihat lebih menonjol
    tombol_hitung = st.sidebar.button("Hitung BMI", type="primary")

    st.sidebar.divider()
    st.sidebar.markdown("""
    ### Tentang BMI 💡
    **Body Mass Index (BMI)** adalah cara sederhana untuk memantau status gizi orang dewasa. 
    
    *   **Penting:** Skor ini tidak memperhitungkan masa otot, kepadatan tulang, dan komposisi tubuh secara keseluruhan.
    """)
    return nama, jenis_kelamin, berat, tinggi, tombol_hitung
