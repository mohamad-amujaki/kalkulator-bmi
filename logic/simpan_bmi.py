"""Fungsi untuk menyimpan history perhitungan BMI ke Google Sheet."""
import pandas as pd
from datetime import datetime
from typing import Optional

import streamlit as st
from streamlit_gsheets import GSheetsConnection


# Konstanta
WORKSHEET_NAME = "Sheet1"


@st.cache_resource
def get_gsheets_connection():
    """
    Mendapatkan koneksi Google Sheets dengan caching.
    Menggunakan @st.cache_resource agar koneksi tidak dibuat ulang setiap rerun.
    """
    return st.connection("gsheets", type=GSheetsConnection)


def _baca_data_lama(conn: GSheetsConnection) -> Optional[pd.DataFrame]:
    """Baca data yang sudah ada di sheet, handle error jika sheet kosong."""
    try:
        data = conn.read(worksheet=WORKSHEET_NAME, ttl=0)
        if data is not None and not data.empty:
            # Bersihkan baris kosong/NaN
            return data.dropna(how="all")
        return None
    except FileNotFoundError:
        return None


def _tulis_data(conn: GSheetsConnection, data: pd.DataFrame) -> None:
    """Tulis data ke Google Sheet."""
    conn.clear(worksheet=WORKSHEET_NAME)
    conn.update(worksheet=WORKSHEET_NAME, data=data)


def simpan_ke_gsheets(nama: str, jk: str, berat: float, tinggi: float,
                       bmi: float, kategori: str, saran: str) -> bool:
    """
    Simpan data BMI ke Google Sheet dengan append.

    Args:
        nama: Nama pengguna
        jk: Jenis kelamin
        berat: Berat badan (kg)
        tinggi: Tinggi badan (cm)
        bmi: Nilai BMI
        kategori: Kategori BMI
        saran: Saran kesehatan

    Returns:
        True jika berhasil, False jika gagal
    """
    # Dapatkan koneksi (di-cache)
    conn = get_gsheets_connection()

    # Baca data lama
    data_lama = _baca_data_lama(conn)

    # Siapkan baris baru
    data_baru = pd.DataFrame([{
        "Nama": nama,
        "Gender": jk,
        "Berat": berat,
        "Tinggi": tinggi,
        "BMI": f"{bmi:.2f}",
        "Kategori": kategori,
        "Saran": saran,
        "Tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }])

    # Gabungkan data lama dan baru
    if data_lama is not None:
        data_total = pd.concat([data_lama, data_baru], ignore_index=True)
    else:
        data_total = data_baru

    # Tulis ke Google Sheet
    _tulis_data(conn, data_total)

    return True
