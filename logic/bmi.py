"""Pure function for BMI calculation and categorization."""
from typing import NamedTuple


class HasilBMI(NamedTuple):
    """Struktur data untuk hasil perhitungan BMI."""
    skor_bmi: float
    kategori: str
    saran: str


# Konstanta untuk kategori BMI
KATEGORI_BMI = [
    (18.5, "Berat Badan Kurang (Underweight)", "Perbanyak asupan nutrisi dan kalori sehat."),
    (24.9, "Berat Badan Ideal (Normal)", "Pertahankan pola makan seimbang dan olahraga rutin."),
    (29.9, "Berat Badan Berlebih (Overweight)", "Cobalah untuk lebih aktif bergerak dan kurangi gula."),
]

SKALA_MAX_BMI = 40  # Skala maksimal untuk progress bar


def hitung_dan_kategorikan_bmi(berat_kg: float, tinggi_cm: float) -> HasilBMI:
    """
    Fungsi murni (Pure Function) untuk menghitung skor BMI,
    menentukan kategori, dan memberikan saran kesehatan.

    Args:
        berat_kg: Berat badan dalam kilogram
        tinggi_cm: Tinggi badan dalam sentimeter

    Returns:
        NamedTuple berisi skor_bmi, kategori, dan saran
    """
    tinggi_m = tinggi_cm / 100
    skor_bmi = berat_kg / (tinggi_m ** 2)

    # Cari kategori berdasarkan rentang BMI
    for batas_atas, kategori, saran in KATEGORI_BMI:
        if skor_bmi < batas_atas:
            return HasilBMI(skor_bmi=round(skor_bmi, 2), kategori=kategori, saran=saran)

    # Jika BMI >= 29.9 (obesitas)
    return HasilBMI(
        skor_bmi=round(skor_bmi, 2),
        kategori="Obesitas",
        saran="Disarankan berkonsultasi dengan tenaga medis."
    )
