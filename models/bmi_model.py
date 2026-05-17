"""BMI Model - Data class and calculator logic."""
from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class BMICategory(Enum):
    """Enum untuk kategori BMI."""
    UNDERWEIGHT = "Berat Badan Kurang (Underweight)"
    NORMAL = "Berat Badan Ideal (Normal)"
    OVERWEIGHT = "Berat Badan Berlebih (Overweight)"
    OBESITY = "Obesitas"


@dataclass
class BMIRecord:
    """
    Data class untuk menyimpan record data BMI.

    Attributes:
        nama: Nama pengguna
        gender: Jenis kelamin
        berat: Berat badan (kg)
        tinggi: Tinggi badan (cm)
        skor_bmi: Nilai BMI hasil perhitungan
        kategori: Kategori BMI
        saran: Saran kesehatan
    """
    nama: str
    gender: str
    berat: float
    tinggi: float
    skor_bmi: float
    kategori: str
    saran: str


class BMICalculator:
    """
    Calculator class untuk menghitung BMI dan menentukan kategori.

    Menggunakan prinsip Single Responsibility Principle (SRP) -
    hanya bertanggung jawab untuk operasi perhitungan BMI.
    """

    # Konstanta skala
    SCALE_MAX: float = 40.0

    # Kategori BMI dengan batas atas
    CATEGORIES = [
        (18.5, BMICategory.UNDERWEIGHT, "Perbanyak asupan nutrisi dan kalori sehat."),
        (24.9, BMICategory.NORMAL, "Pertahankan pola makan seimbang dan olahraga rutin."),
        (29.9, BMICategory.OVERWEIGHT, "Cobalah untuk lebih aktif bergerak dan kurangi gula."),
    ]

    @classmethod
    def hitung_bmi(cls, berat_kg: float, tinggi_cm: float) -> Tuple[float, str, str]:
        """
        Hitung BMI dan kembalikan hasil.

        Args:
            berat_kg: Berat badan dalam kilogram
            tinggi_cm: Tinggi badan dalam sentimeter

        Returns:
            Tuple[float, str, str]: (skor_bmi, kategori, saran)
        """
        tinggi_m = tinggi_cm / 100
        skor_bmi = berat_kg / (tinggi_m ** 2)

        # Cari kategori berdasarkan rentang BMI
        for batas, enum_kategori, saran in cls.CATEGORIES:
            if skor_bmi < batas:
                return round(skor_bmi, 2), enum_kategori.value, saran

        # Jika BMI >= 29.9 (obesitas)
        return (
            round(skor_bmi, 2),
            BMICategory.OBESITY.value,
            "Disarankan berkonsultasi dengan tenaga medis."
        )

    @classmethod
    def buat_record(cls, nama: str, gender: str, berat_kg: float,
                    tinggi_cm: float) -> BMIRecord:
        """
        Buat instance BMIRecord dari input pengguna.

        Args:
            nama: Nama pengguna
            gender: Jenis kelamin
            berat_kg: Berat badan (kg)
            tinggi_cm: Tinggi badan (cm)

        Returns:
            BMIRecord: Objek record BMI
        """
        skor_bmi, kategori, saran = cls.hitung_bmi(berat_kg, tinggi_cm)
        return BMIRecord(
            nama=nama,
            gender=gender,
            berat=berat_kg,
            tinggi=tinggi_cm,
            skor_bmi=skor_bmi,
            kategori=kategori,
            saran=saran
        )
