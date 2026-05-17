"""Sidebar View - UI components for sidebar input."""
import streamlit as st
from typing import Tuple


class SidebarView:
    """
    View class untuk komponen sidebar input.

    View dalam pattern MVC bertanggung jawab untuk:
    - Menampilkan UI ke pengguna
    - Mengambil input dari pengguna
    - Tidak mengandung logika bisnis

    Semua method adalah static method karena Streamlit
    menggunakan pendekatan functional rendering.
    """

    # Konstanta
    NAMA_PLACEHOLDER = "Masukkan nama Anda"
    BERAT_DEFAULT = 60.0
    TINGGI_DEFAULT = 165.0

    @staticmethod
    def render() -> Tuple[str, str, float, float, bool]:
        """
        Render komponen input di sidebar.

        Returns:
            Tuple berisi: (nama, jenis_kelamin, berat, tinggi, tombol_hitung)
        """
        st.sidebar.title("Silakan isi data berikut")

        # Handle reset form
        if st.session_state.get('reset_form', False):
            SidebarView._reset_form_state()

        # Input nama
        nama = SidebarView._render_nama_input()

        # Input jenis kelamin
        jenis_kelamin = SidebarView._render_gender_input()

        # Input berat dan tinggi
        berat = SidebarView._render_berat_input()
        tinggi = SidebarView._render_tinggi_input()

        # Tombol Hitung BMI
        tombol_hitung = SidebarView._render_hitut_button()

        # Info tentang BMI
        SidebarView._render_info_bmi()

        return nama or "", jenis_kelamin, berat, tinggi, tombol_hitung

    @staticmethod
    def _reset_form_state() -> None:
        """Reset form state setelah digunakan."""
        st.session_state.reset_form = False

    @staticmethod
    def _render_nama_input() -> str:
        """Render input nama."""
        nama_value = st.session_state.get('nama_input', "")
        result = st.sidebar.text_input(
            "Nama:",
            value=nama_value,
            placeholder=SidebarView.NAMA_PLACEHOLDER,
            key="nama_input"
        )
        return result if result is not None else ""

    @staticmethod
    def _render_gender_input() -> str:
        """Render input jenis kelamin."""
        return st.sidebar.radio(
            "Jenis Kelamin:",
            ["Laki-laki", "Perempuan"]
        )

    @staticmethod
    def _render_berat_input() -> float:
        """Render input berat badan."""
        return st.sidebar.number_input(
            "Masukkan Berat Badan (kg)",
            min_value=1.0,
            value=SidebarView.BERAT_DEFAULT,
            step=0.1
        )

    @staticmethod
    def _render_tinggi_input() -> float:
        """Render input tinggi badan."""
        return st.sidebar.number_input(
            "Masukkan Tinggi Badan (cm)",
            min_value=1.0,
            value=SidebarView.TINGGI_DEFAULT,
            step=1.0
        )

    @staticmethod
    def _render_hitut_button() -> bool:
        """Render tombol Hitung BMI."""
        return st.sidebar.button("Hitung BMI", type="primary")

    @staticmethod
    def _render_info_bmi() -> None:
        """Render info tentang BMI."""
        st.sidebar.divider()
        st.sidebar.markdown("""
        ### Tentang BMI 💡
        **Body Mass Index (BMI)** adalah cara sederhana untuk memantau status gizi orang dewasa.

        *   **Penting:** Skor ini tidak memperhitungkan massa otot, kepadatan tulang, dan komposisi tubuh secara keseluruhan.
        """)
