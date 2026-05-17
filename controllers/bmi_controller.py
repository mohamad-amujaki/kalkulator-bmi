"""BMI Controller - Orchestrates BMI business logic."""
import streamlit as st

from models.bmi_model import BMIRecord, BMICalculator
from models.storage_model import StorageManager


class BMIController:
    """
    Controller class yang mengkoordinasikan logika bisnis BMI.

    Controller dalam pattern MVC bertanggung jawab untuk:
    - Menerima input dari View
    - Memanggil Model untuk pemrosesan data
    - Mengembalikan hasil ke View

    Menggunakan prinsip Controller dalam MVC -
    mengkoordinasikan alur data antara Model dan View.
    """

    @staticmethod
    def proses_hitung_bmi(nama: str, gender: str, berat: float,
                          tinggi: float) -> BMIRecord:
        """
        Proses perhitungan BMI.

        Args:
            nama: Nama pengguna
            gender: Jenis kelamin
            berat: Berat badan (kg)
            tinggi: Tinggi badan (cm)

        Returns:
            BMIRecord: Record BMI hasil perhitungan

        Raises:
            ValueError: Jika input tidak valid
        """
        # Validasi input
        if not nama or len(nama.strip()) < 3:
            raise ValueError("Nama minimal 3 karakter")
        if berat <= 0 or tinggi <= 0:
            raise ValueError("Berat dan tinggi harus lebih dari 0")

        # Buat record BMI
        return BMICalculator.buat_record(
            nama=nama.strip(),
            gender=gender,
            berat_kg=berat,
            tinggi_cm=tinggi
        )

    @staticmethod
    def proses_simpan_data(record: BMIRecord) -> bool:
        """
        Proses penyimpanan data BMI ke Google Sheets.

        Args:
            record: Record BMI yang akan disimpan

        Returns:
            bool: True jika berhasil
        """
        return StorageManager.simpan_record(record)

    @staticmethod
    def inisialisasi_session_state() -> None:
        """Inisialisasi session state yang dibutuhkan aplikasi."""
        defaults = {
            'tombol_hitung_ditekan': False,
            'tombol_simpan_ditekan': False,
            'reset_form': False,
            'bmi_record': None,  # Simpan BMIRecord object
        }
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    @staticmethod
    def reset_form() -> None:
        """Reset form ke kondisi awal."""
        st.session_state.tombol_hitung_ditekan = False
        st.session_state.tombol_simpan_ditekan = False
        st.session_state.reset_form = True
        st.session_state.bmi_record = None

        # Hapus nilai input dari session state widget
        if 'nama_input' in st.session_state:
            del st.session_state['nama_input']
