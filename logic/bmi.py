"""Pure function for BMI calculation and categorization."""
def hitung_dan_kategorikan_bmi(berat_kg: float, tinggi_cm: float) -> tuple[float, str, str]:
    """
    Fungsi murni (Pure Function) untuk menghitung skor BMI, 
    menentukan kategori, dan memberikan saran kesehatan.
    """
    tinggi_m = tinggi_cm / 100
    skor_bmi = berat_kg / (tinggi_m ** 2)
    if skor_bmi < 18.5:
        kategori = "Berat Badan Kurang (Underweight)"
        saran = "Perbanyak asupan nutrisi dan kalori sehat."
    elif 18.5 <= skor_bmi < 24.9:
        kategori = "Berat Badan Ideal (Normal)"
        saran = "Pertahankan pola makan seimbang dan olahraga rutin."
    elif 25.0 <= skor_bmi < 29.9:
        kategori = "Berat Badan Berlebih (Overweight)"
        saran = "Cobalah untuk lebih aktif bergerak dan kurangi gula."
    else:
        kategori = "Obesitas"
        saran = "Disarankan berkonsultasi dengan tenaga medis."
    return skor_bmi, kategori, saran
