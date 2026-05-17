"""Results display components."""
import streamlit as st
import streamlit.components.v1 as components
from typing import NamedTuple

from logic.bmi import SKALA_MAX_BMI


class DataBMI(NamedTuple):
    """Struktur data BMI yang akan ditampilkan."""
    nama: str
    gender: str
    nilai_bmi: float
    kategori: str
    saran: str


def _render_progress_bar(nilai_bmi: float) -> None:
    """Render progress bar untukvisualisasi posisi BMI."""
    st.write("Posisi BMI Anda dalam skala umum (maksimal skala 40):")
    progress_value = min(nilai_bmi / SKALA_MAX_BMI, 1.0)
    st.progress(progress_value)

    # Tampilkan label skala
    col_start, col_end = st.columns(2)
    with col_start:
        st.caption(0)
    with col_end:
        st.markdown(
            f"<p style='text-align: right; color: gray; font-size: small;'>{SKALA_MAX_BMI}+</p>",
            unsafe_allow_html=True
        )


def _render_tombol_reset() -> None:
    """Render tombol untuk perhitungan baru."""
    st.divider()
    col_reset, col_spacer = st.columns([1, 3])

    with col_reset:
        if st.button("🔄 Hitung BMI Baru", type="secondary"):
            # Reset session state
            st.session_state.tombol_hitung_ditekan = False
            st.session_state.tombol_simpan_ditekan = False
            st.session_state.reset_form = True

            # Hapus nilai input dari session state widget
            if 'nama_input' in st.session_state:
                del st.session_state['nama_input']

            st.rerun()


def _render_focus_script() -> None:
    """Render JavaScript untuk focus ke input nama."""
    components.html("""
    <script>
    function focusNama() {
        const inputs = window.parent.document.querySelectorAll('input[type="text"]');
        for (let input of inputs) {
            if (input.placeholder.includes('nama')) {
                input.focus();
                break;
            }
        }
    }
    setTimeout(focusNama, 150);
    </script>
    """, scrolling=False)


def tampilkan_hasil_bmi(nama_pengguna: str, gender: str, nilai_bmi: float,
                         kategori_bmi: str, saran_bmi: str) -> None:
    """
    Render komponen tampilan hasil BMI ke layar utama.

    Args:
        nama_pengguna: Nama pengguna
        gender: Jenis kelamin
        nilai_bmi: Nilai BMI hasil perhitungan
        kategori_bmi: Kategori BMI
        saran_bmi: Saran kesehatan
    """
    # Header dan info pengguna
    st.header("📊 Hasil Analisis Kesehatan")
    st.subheader(f"Halo, {nama_pengguna}!")
    st.write(f"Jenis Kelamin: {gender}")
    st.divider()

    # Metrik utama
    st.metric(label="Nilai BMI Anda", value=f"{nilai_bmi:.2f}")

    # Info kategori dan saran
    st.info(f"Kategori BMI: **{kategori_bmi}**\n\n**Saran**: {saran_bmi}")

    # Progress bar
    _render_progress_bar(nilai_bmi)

    # Tombol reset
    _render_tombol_reset()

    # Script focus
    _render_focus_script()


def tampilkan_welcome() -> None:
    """Tampilkan halaman selamat datang."""
    st.title("🏃‍♂️ Kalkulator BMI")
    st.markdown("""
    ### Selamat Datang!

    Silakan isi data diri pada **panel di sebelah kiri**, lalu klik tombol **Hitung BMI**
    untuk mengetahui skor BMI dan kategori kesehatan Anda.
    """)
