"""BMI Calculator Application - Refactored."""
import streamlit as st

from logic.bmi import hitung_dan_kategorikan_bmi
from components.sidebar import render_sidebar
from components.results import tampilkan_hasil_bmi, tampilkan_welcome


# ==========================================
# MAIN APPLICATION
# ==========================================

# Render sidebar and get user inputs
nama, jenis_kelamin, berat, tinggi, tombol_hitung = render_sidebar()

# Jika tombol diklik, jalankan validasi dan tampilkan hasil
if tombol_hitung:
    if len(nama.strip()) < 3:
        st.sidebar.error("⚠️ Nama minimal terdiri dari 3 karakter (spasi tidak dihitung).")
    else:
        # Panggil fungsi logika
        skor_bmi, kategori, saran = hitung_dan_kategorikan_bmi(berat, tinggi)
        # Tampilkan hasil di area utama
        tampilkan_hasil_bmi(nama, jenis_kelamin, skor_bmi, kategori, saran)

# Jika tombol belum diklik, tampilkan halaman Welcome
else:
    tampilkan_welcome()
