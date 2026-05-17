"""BMI Calculator Application - MVC Architecture."""
import streamlit as st

from controllers.bmi_controller import BMIController
from views.sidebar_view import SidebarView
from views.results_view import ResultsView


def main() -> None:
    """Main application entry point."""
    # Inisialisasi session state
    BMIController.inisialisasi_session_state()

    # Render sidebar dan dapatkan input dari pengguna
    nama, jenis_kelamin, berat, tinggi, tombol_hitung = SidebarView.render()

    # Alur utama aplikasi
    if tombol_hitung:
        _proses_hitung_bmi(nama, jenis_kelamin, berat, tinggi)
    elif st.session_state.tombol_hitung_ditekan and st.session_state.tombol_simpan_ditekan:
        _proses_simpan_data()
    elif st.session_state.tombol_hitung_ditekan:
        _tampilkan_hasil_dengan_tombol_simpan()
    else:
        ResultsView.render_welcome()


def _proses_hitung_bmi(nama: str, gender: str, berat: float, tinggi: float) -> None:
    """Proses ketika tombol Hitung BMI ditekan."""
    if len(nama.strip()) < 3:
        st.sidebar.error("⚠️ Nama minimal terdiri dari 3 karakter (spasi tidak dihitung).")
        ResultsView.render_welcome()
        return

    try:
        # Hitung BMI menggunakan controller
        record = BMIController.proses_hitung_bmi(nama, gender, berat, tinggi)

        # Simpan record ke session state
        st.session_state.bmi_record = record
        st.session_state.tombol_hitung_ditekan = True
        st.session_state.tombol_simpan_ditekan = False

        # Render hasil
        ResultsView.render_hasil_bmi(record)

        # Rerun agar tombol "Simpan Data" muncul segera
        st.rerun()

    except ValueError as e:
        st.sidebar.error(f"⚠️ {e}")
        ResultsView.render_welcome()


def _proses_simpan_data() -> None:
    """Proses ketika tombol Simpan Data ditekan."""
    record = st.session_state.bmi_record
    if record is None:
        st.error("❌ Data BMI tidak ditemukan")
        return

    try:
        BMIController.proses_simpan_data(record)
        st.session_state.tombol_simpan_ditekan = False
        st.success("Data berhasil disimpan ke riwayat! ✅")
    except PermissionError:
        st.error(
            "❌ **Gagal Menyimpan:** Tidak ada akses ke spreadsheet. "
            "Pastikan Anda sudah memberikan izin yang benar."
        )
    except KeyError:
        st.error(
            "❌ **Gagal Menyimpan:** Worksheet 'Sheet1' tidak ditemukan. "
            "Periksa nama worksheet Anda."
        )
    except ValueError as e:
        st.error(f"❌ **Gagal Menyimpan:** Format data tidak valid. {e}")
    except FileNotFoundError as e:
        st.error(f"❌ **Gagal menyimpan data:** {e}")

    # Render hasil BMI lagi setelah proses simpan
    ResultsView.render_hasil_bmi(record)


def _tampilkan_hasil_dengan_tombol_simpan() -> None:
    """Tampilkan hasil BMI dengan tombol Simpan."""
    record = st.session_state.bmi_record
    if record:
        ResultsView.render_hasil_bmi(record, show_save_button=True)


if __name__ == "__main__":
    main()
