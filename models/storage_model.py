"""Storage Model - Google Sheets storage management."""
import pandas as pd
from datetime import datetime
from typing import Optional
import streamlit as st
from streamlit_gsheets import GSheetsConnection

from models.bmi_model import BMIRecord


class StorageManager:
    """
    Manager class untuk operasi penyimpanan data ke Google Sheets.

    Menggunakan prinsip Single Responsibility -
    hanya bertanggung jawab untuk operasi storage.
    """

    WORKSHEET_NAME = "Sheet1"

    @staticmethod
    @st.cache_resource
    def _get_connection() -> GSheetsConnection:
        """
        Dapatkan koneksi Google Sheets dengan caching.

        Returns:
            GSheetsConnection: Objek koneksi
        """
        return st.connection("gsheets", type=GSheetsConnection)

    @classmethod
    def _read_existing_data(cls) -> Optional[pd.DataFrame]:
        """
        Baca data yang sudah ada di sheet.

        Returns:
            DataFrame atau None jika kosong/error
        """
        try:
            conn = cls._get_connection()
            data = conn.read(worksheet=cls.WORKSHEET_NAME, ttl=0)
            if data is not None and not data.empty:
                # Bersihkan baris kosong/NaN
                return data.dropna(how="all")
            return None
        except Exception:
            return None

    @classmethod
    def _write_data(cls, data: pd.DataFrame) -> None:
        """
        Tulis data ke Google Sheet (replace seluruh konten).

        Args:
            data: DataFrame yang akan ditulis
        """
        conn = cls._get_connection()
        conn.clear(worksheet=cls.WORKSHEET_NAME)
        conn.update(worksheet=cls.WORKSHEET_NAME, data=data)

    @classmethod
    def simpan_record(cls, record: BMIRecord) -> bool:
        """
        Simpan satu record BMI ke Google Sheets.

        Args:
            record: Objek BMIRecord yang akan disimpan

        Returns:
            bool: True jika berhasil
        """
        # Baca data lama
        data_lama = cls._read_existing_data()

        # Buat DataFrame untuk record baru
        data_baru = pd.DataFrame([{
            "Nama": record.nama,
            "Gender": record.gender,
            "Berat": record.berat,
            "Tinggi": record.tinggi,
            "BMI": f"{record.skor_bmi:.2f}",
            "Kategori": record.kategori,
            "Saran": record.saran,
            "Tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }])

        # Gabungkan data lama dan baru
        if data_lama is not None:
            data_total = pd.concat([data_lama, data_baru], ignore_index=True)
        else:
            data_total = data_baru

        # Tulis ke Google Sheet
        cls._write_data(data_total)

        return True
