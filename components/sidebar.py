"""Sidebar components for user input."""
import streamlit as st
from typing import Tuple


# Konstanta
NAMA_PLACEHOLDER = "Masukkan nama Anda"
BERAT_DEFAULT = 60.0
TINGGI_DEFAULT = 165.0


def render_sidebar() -> Tuple[str, str, float, float, bool]:
    """
    Render komponen input di sidebar dan kembalikan data pengguna.

    Returns:
        Tuple berisi: (nama, jenis_kelamin, berat, tinggi, tombol_hitung)
    """
    st.sidebar.title("Silakan isi data berikut")

    # Handle reset form
    if st.session_state.get('reset_form', False):
        nama_value = ""
    else:
        nama_value = st.session_state.get('nama_input', "")

    # Input nama
    nama = st.sidebar.text_input(
        "Nama:",
        value=nama_value,
        placeholder=NAMA_PLACEHOLDER,
        key="nama_input"
    )

    # Input jenis kelamin
    jenis_kelamin = st.sidebar.radio(
        "Jenis Kelamin:",
        ["Laki-laki", "Perempuan"]
    )

    # Input berat badan dengan nilai default yang logis
    berat = st.sidebar.number_input(
        "Masukkan Berat Badan (kg)",
        min_value=1.0,
        value=BERAT_DEFAULT,
        step=0.1
    )

    # Input tinggi badan
    tinggi = st.sidebar.number_input(
        "Masukkan Tinggi Badan (cm)",
        min_value=1.0,
        value=TINGGI_DEFAULT,
        step=1.0
    )

    # Tombol Hitung BMI
    tombol_hitung = st.sidebar.button("Hitung BMI", type="primary")

    # Info tentang BMI
    st.sidebar.divider()
    st.sidebar.markdown("""
    ### Tentang BMI 💡
    **Body Mass Index (BMI)** adalah cara sederhana untuk memantau status gizi orang dewasa.

    *   **Penting:** Skor ini tidak memperhitungkan massa otot, kepadatan tulang, dan komposisi tubuh secara keseluruhan.
    """)

    return nama, jenis_kelamin, berat, tinggi, tombol_hitung
