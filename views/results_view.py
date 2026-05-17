"""Results View - UI components for displaying BMI results."""
import streamlit as st
import streamlit.components.v1 as components

from models.bmi_model import BMIRecord, BMICalculator


class ResultsView:
    """
    View class untuk komponen tampilan hasil BMI.

    View dalam pattern MVC bertanggung jawab untuk:
    - Menampilkan hasil ke pengguna
    - Tidak mengandung logika bisnis

    Semua method adalah static method karena Streamlit
    menggunakan pendekatan functional rendering.
    """

    @staticmethod
    def render_hasil_bmi(record: BMIRecord, show_save_button: bool = False) -> None:
        """
        Render komponen tampilan hasil BMI.

        Args:
            record: Objek BMIRecord yang akan ditampilkan
            show_save_button: True untuk menampilkan tombol Simpan Data
        """
        # Header dan info pengguna
        st.header("📊 Hasil Analisis Kesehatan")
        st.subheader(f"Halo, {record.nama}!")
        st.write(f"Jenis Kelamin: {record.gender}")
        st.divider()

        # Metrik utama
        st.metric(label="Nilai BMI Anda", value=f"{record.skor_bmi:.2f}")

        # Info kategori dan saran
        st.info(
            f"Kategori BMI: **{record.kategori}**\n\n"
            f"**Saran**: {record.saran}"
        )

        # Progress bar
        ResultsView._render_progress_bar(record.skor_bmi)

        # Tombol reset, simpan, dan focus
        ResultsView._render_reset_section(show_save_button=show_save_button)

    @staticmethod
    def _render_progress_bar(nilai_bmi: float) -> None:
        """Render progress bar untukvisualisasi posisi BMI."""
        st.write("Posisi BMI Anda dalam skala umum (maksimal skala 40):")
        progress_value = min(nilai_bmi / BMICalculator.SCALE_MAX, 1.0)
        st.progress(progress_value)

        # Tampilkan label skala
        col_start, col_end = st.columns(2)
        with col_start:
            st.caption(0)
        with col_end:
            st.markdown(
                f"<p style='text-align: right; color: gray; font-size: small;'>"
                f"{BMICalculator.SCALE_MAX}+</p>",
                unsafe_allow_html=True
            )

    @staticmethod
    def _render_reset_section(show_save_button: bool = False) -> None:
        """Render tombol reset, simpan, dan script focus."""
        st.divider()

        if show_save_button:
            col_save, _, col_reset = st.columns([1, 1, 1])

            with col_save:
                if st.button("💾 Simpan ke Google Sheets", type="primary"):
                    st.session_state.tombol_simpan_ditekan = True
                    st.rerun()

            with col_reset:
                if st.button("🔄 Hitung BMI Baru", type="secondary"):
                    from controllers.bmi_controller import BMIController
                    BMIController.reset_form()
                    st.rerun()
        else:
            col_reset, _ = st.columns([1, 3])

            with col_reset:
                if st.button("🔄 Hitung BMI Baru", type="secondary"):
                    from controllers.bmi_controller import BMIController
                    BMIController.reset_form()
                    st.rerun()

        # Script focus ke input nama
        ResultsView._render_focus_script()

    @staticmethod
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

    @staticmethod
    def render_welcome() -> None:
        """Render halaman selamat datang."""
        st.title("🏃‍♂️ Kalkulator BMI")
        st.markdown("""
        ### Selamat Datang!

        Silakan isi data diri pada **panel di sebelah kiri**, lalu klik tombol **Hitung BMI**
        untuk mengetahui skor BMI dan kategori kesehatan Anda.
        """)
