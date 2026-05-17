# Mini Project Kalkulator BMI dengan Python dan Streamlit

## Tentang Streamlit

Streamlit adalah _framework_ Python yang memungkinkan kita mengubah script Python menjadi aplikasi web interaktif dalam hitungan menit. Kita tidak perlu menguasai HTML, CSS, atau JavaScript untuk membuat antarmuka yang menarik bagi proyek data atau alat bantu sederhana lainnya.

Untuk mempelajarinya secara bertahap, kita akan membuat mini project berupa **Kalkulator BMI (Body Mass Index)**. Proyek ini akan membantu kita memahami bagaimana Streamlit menangani input dari pengguna, melakukan perhitungan di balik layar, dan menampilkan hasilnya kembali ke layar secara _real-time_.

Yang akan kita pelajari adalah:

1. **Persiapan & Instalasi**: Cara membuat virtual environment dan memasang Streamlit di komputer serta menjalankan script "Hello World" pertama kita.
2. **Membangun Antarmuka (UI)**: Mengenal cara membuat _header_, kolom input angka, tombol, dan sidebar untuk menerima data dari pengguna.
3. **Logika Kalkulator & Output**: Menghubungkan input dengan rumus matematika dan menampilkan hasil serta kategori kesehatan.
4. **Arsitektur MVC**: Memahami pattern MVC (Model-View-Controller) untuk menulis kode yang terstruktur dan mudah dipelihara.

## Instalasi Streamlit

Panduan ini akan memandu Anda membuat lingkungan dengan venv dan menginstal Streamlit dengan pip yang direkomendasikan. Setelah streamlit terinstall, kita akan membuat aplikasi "Hello world" sederhana dan menjalankannya.

### Prasyarat

- Pastikan komputer Anda telah terinstall Python dengan versi yang sesuai (3.10 s.d. 3.14).
- Python package manager (pip)
- Code editor (VSCode, dll)

Untuk menyiapkan lingkungan Python dan menguji instalasi, jalankan perintah terminal berikut:

```bash
mkdir myproject
cd myproject
python --version
python -m venv .venv

# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate

pip install streamlit
streamlit hello
```

Setelah menjalankan perintah `streamlit hello` di terminal, browser akan terbuka secara otomatis dan menampilkan halaman sambutan interaktif yang berisi berbagai demo fitur.

## Struktur Proyek MVC

Proyek Kalkulator BMI yang kita bangun menggunakan arsitektur **MVC (Model-View-Controller)**:

```text
kalkulator-bmi/
├── app.py                    # Titik masuk utama aplikasi (Controller utama)
├── models/                   # MODEL - Data classes dan business logic
│   ├── __init__.py
│   ├── bmi_model.py         # BMIRecord, BMICalculator, BMICategory
│   └── storage_model.py     # StorageManager
├── controllers/              # CONTROLLER - Business logic orchestration
│   ├── __init__.py
│   └── bmi_controller.py   # BMIController
└── views/                   # VIEW - UI components
    ├── __init__.py
    ├── sidebar_view.py      # SidebarView
    └── results_view.py     # ResultsView
```

### Penjelasan Pattern MVC

| Layer          | Tanggung Jawab                    | Contoh                       |
| -------------- | --------------------------------- | ---------------------------- |
| **Model**      | Menyimpan data dan lógica bisnis  | `BMIRecord`, `BMICalculator` |
| **View**       | Menampilkan UI dan menerima input | `SidebarView`, `ResultsView` |
| **Controller** | Mengkoordinasikan Model dan View  | `BMIController`              |

Pemisahan ini mengikuti prinsip **Separation of Concerns**, yaitu memisahkan tanggung jawab agar kode lebih mudah diuji, dipelihara, dan dikembangkan.

## Buat Script Kalkulator Sederhana

Langkah selanjutnya adalah membuat file script Python untuk aplikasi Kalkulator BMI. Di tahap ini, kita akan fokus membangun tampilan agar pengguna bisa memasukkan data.

Silakan buat file baru bernama `app.py` di folder kerja, lalu masukkan kode berikut:

```python
# app.py
import streamlit as st

# Menampilkan judul aplikasi
st.title("Kalkulator BMI Interaktif")

# Membuat input nama pengguna
nama = st.text_input("Masukkan nama Anda:")

# Membuat input jenis kelamin pengguna
jenis_kelamin = st.selectbox("Pilih jenis kelamin Anda:", ["Laki-laki", "Perempuan"])

# Membuat input angka untuk berat badan
berat = st.number_input("Masukkan berat badan Anda (kg):", min_value=1.0, step=0.1)

# Membuat input angka untuk tinggi badan
tinggi = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=1.0, step=1.0)
```

Setelah menyimpan file tersebut, buka terminal di folder yang sama dan ketik perintah berikut:

```bash
streamlit run app.py
```

Setelah menjalankan perintah di atas, tab baru akan terbuka di browser dan menampilkan kotak-kotak input untuk nama, jenis kelamin, berat badan, dan tinggi badan.

### Penjelasan Komponen UI

| Komponen            | Fungsi                                                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `st.title()`        | Menampilkan judul besar di bagian atas aplikasi                                                                     |
| `st.text_input()`   | Membuat kotak input untuk teks (nama)                                                                               |
| `st.selectbox()`    | Membuat dropdown untuk memilih salah satu opsi (jenis kelamin)                                                      |
| `st.number_input()` | Membuat kotak input khusus angka. Parameter `min_value` memastikan pengguna tidak memasukkan angka nol atau negatif |

## Tambahkan Logika Perhitungan BMI

BMI dihitung dengan membagi berat badan (kg) dengan kuadrat tinggi badan dalam satuan meter:

```text
BMI = berat (kg) / tinggi (m)²
```

Karena pengguna memasukkan tinggi dalam satuan sentimeter (cm), maka kita harus mengkonversi variabel tinggi ke dalam meter terlebih dahulu (`tinggi_m = tinggi / 100`), baru kemudian menghitung BMI-nya.

```python
# 1. Konversi tinggi dari cm ke meter
tinggi_m = tinggi / 100

# 2. Hitung BMI (berat dibagi tinggi pangkat dua)
# Di Python, pangkat dua ditulis dengan simbol **2
bmi = berat / (tinggi_m ** 2)
```

Dengan kode di atas, setiap kali pengguna mengubah angka di aplikasi web, Streamlit akan otomatis menjalankan ulang script dan menghitung nilai BMI yang baru.

Sekarang kita sudah punya nilai BMI yang tersimpan di variabel `bmi`. Namun, nilai ini baru ada di "ingatan" komputer dan belum muncul di layar aplikasi web kita. Untuk menampilkan hasil di layar, kita bisa menggunakan `st.write` atau `st.success`.

Berikut cara kita menulisnya dalam kode:

```python
# Menampilkan hasil dengan 2 angka di belakang koma agar rapi
st.write(f"Nilai BMI Anda adalah: {bmi:.2f}")

# Atau jika ingin lebih cantik dengan warna hijau:
st.success(f"Hasil perhitungan BMI: {bmi:.2f}")
```

Simbol `:.2f` di dalam kode tersebut berfungsi untuk membatasi angka desimal agar tidak terlalu panjang (misalnya dari `22.4489...` menjadi `22.45`).

Sekarang, angka BMI sudah muncul di layar. Namun, pengguna mungkin tidak tahu apakah angka 22.5 itu termasuk sehat atau tidak.

Dalam Python, kita biasanya menggunakan `if-elif-else` untuk mengecek rentang nilai (seperti nilai BMI). Berikut adalah tabel kategori BMI secara umum:

| Rentang BMI      | Kategori BMI                      |
| ---------------- | --------------------------------- |
| Kurang dari 18.5 | Berat Badan Kurang (Underweight)  |
| 18.5 – 24.9      | Berat Badan Ideal (Normal)        |
| 25.0 – 29.9      | Berat Badan Berlebih (Overweight) |
| 30.0 atau lebih  | Obesitas                          |

Struktur `if-elif-else` di Python bekerja seperti percabangan jalan. Program akan memeriksa satu per satu kondisi dari atas ke bawah, dan berhenti begitu menemukan kondisi yang benar (True).

Berikut adalah cara kita menuliskan logika kategori BMI tersebut ke dalam kode:

```python
if bmi < 18.5:
    kategori = "Berat Badan Kurang (Underweight)"
    st.warning(kategori)
elif 18.5 <= bmi < 24.9:
    kategori = "Berat Badan Ideal (Normal)"
    st.success(kategori)
elif 25.0 <= bmi < 29.9:
    kategori = "Berat Badan Berlebih (Overweight)"
    st.warning(kategori)
else:
    kategori = "Obesitas"
    st.error(kategori)
```

### Penjelasan Kode

- `if`: Kondisi pertama yang diperiksa.
- `elif` (else if): Digunakan untuk memeriksa kondisi berikutnya jika kondisi sebelumnya salah. Kita bisa menggunakan `elif` sebanyak yang dibutuhkan.
- `else`: Pilihan terakhir jika tidak ada satupun kondisi di atas yang terpenuhi (dalam hal ini, jika BMI 30 atau lebih).
- `st.warning` / `st.success` / `st.error`: Cara Streamlit menampilkan pesan dengan warna berbeda (kuning, hijau, dan merah) agar tampilan lebih informatif.

## Menampilkan Hasil dengan Fungsi Terpisah

Untuk membuat tampilan hasil yang lebih rapi dan terorganisir, kita bisa memindahkan kode tampilan hasil ke dalam sebuah fungsi tersendiri.

```python
def tampilkan_hasil_bmi(nama, gender, nilai_bmi, kategori, saran):
    """Fungsi khusus untuk mengurus tampilan (render) hasil BMI ke layar utama."""
    st.header("📊 Hasil Analisis Kesehatan")
    st.subheader(f"Halo, {nama}!")
    st.write(f"Jenis Kelamin: {gender}")
    st.divider()
    # Menampilkan metrik utama
    st.metric(label="Nilai BMI Anda", value=f"{nilai_bmi:.2f}")
    st.info(f"Kategori BMI: **{kategori}**\n\n**Saran**: {saran}")
```

### Penjelasan Komponen Baru

| Komponen         | Fungsi                                                              |
| ---------------- | ------------------------------------------------------------------- |
| `st.header()`    | Menampilkan judul bagian (lebih kecil dari `st.title`)              |
| `st.subheader()` | Menampilkan sub-judul untuk memberi konteks                         |
| `st.metric()`    | Menampilkan angka dengan format yang lebih menonjol dan profesional |
| `st.divider()`   | Membuat garis horizontal untuk merapikan tampilan teks              |
| `st.info()`      | Menampilkan kotak informasi dengan warna biru                       |

## Menggunakan Sidebar

Menggunakan sidebar adalah cara efektif untuk memisahkan antara input/konfigurasi dengan hasil/konten utama. Di Streamlit, kita bisa memindahkan hampir semua elemen ke samping hanya dengan menambahkan kata `.sidebar` setelah `st`.

Bayangkan halaman web kita memiliki dua area:

- **Main Area**: Tempat untuk judul besar, grafik, atau hasil.
- **Sidebar**: Area di sebelah kiri (atau kanan) untuk kontrol atau input data.

Jika sebelumnya kita menulis:

```python
nama = st.text_input("Masukkan nama Anda:")
```

Maka untuk memindahkannya ke samping kiri, kodenya menjadi:

```python
nama = st.sidebar.text_input("Masukkan nama Anda:")
```

Berikut contoh lengkap bagaimana kita membuat input di sidebar:

```python
def render_sidebar():
    """Merender komponen input di sidebar dan mengembalikan data pengguna."""
    st.sidebar.title("Silakan isi data berikut")

    nama = st.sidebar.text_input("Nama:", placeholder="Masukkan nama Anda")
    jenis_kelamin = st.sidebar.radio("Jenis Kelamin:", ["Laki-laki", "Perempuan"])

    # Memberikan nilai default (value) yang logis agar aplikasi tidak langsung menghitung angka 1.0
    berat = st.sidebar.number_input("Masukkan Berat Badan (kg)",
                                    min_value=1.0, value=60.0, step=0.1)
    tinggi = st.sidebar.number_input("Masukkan Tinggi Badan (cm)",
                                    min_value=1.0, value=165.0, step=1.0)

    tombol_hitung = st.sidebar.button("Hitung BMI", type="primary")

    st.sidebar.divider()
    st.sidebar.markdown("""
    ### Tentang BMI 💡
    **Body Mass Index (BMI)** adalah cara sederhana untuk memantau status gizi orang dewasa.

    *   **Penting:** Skor ini tidak memperhitungkan massa otot, kepadatan tulang, dan komposisi tubuh secara keseluruhan.
    """)
    return nama, jenis_kelamin, berat, tinggi, tombol_hitung
```

### Penjelasan Komponen Sidebar

| Komponen                | Fungsi                                                                                             |
| ----------------------- | -------------------------------------------------------------------------------------------------- |
| `st.sidebar.title()`    | Memberikan judul di area sidebar                                                                   |
| `st.sidebar.radio()`    | Membuat pilihan berbentuk radio button (hanya bisa pilih satu)                                     |
| `st.sidebar.button()`   | Membuat tombol yang bisa diklik. Parameter `type="primary"` membuat tombol terlihat lebih menonjol |
| `st.sidebar.divider()`  | Garis pemisah di sidebar                                                                           |
| `st.sidebar.markdown()` | Menampilkan teks berformat markdown di sidebar                                                     |

## Tambahkan Progress Bar BMI

Menambahkan Progress Bar akan memberikan visualisasi instan mengenai posisi berat badan seseorang dalam skala kesehatan secara lebih intuitif.

Di Streamlit, kita bisa menggunakan fungsi `st.progress()`. Namun, ada satu aturan teknis yang penting: nilai yang dimasukkan ke dalam fungsi ini harus berupa angka desimal antara `0.0` (bar kosong) hingga `1.0` (bar penuh).

Masalahnya, angka BMI kita biasanya berkisar antara 10 hingga 40 atau lebih. Kita tidak bisa langsung memasukkan variabel `bmi` ke dalam progress bar karena nilainya pasti lebih besar dari `1.0`. Jadi, kita perlu melakukan sedikit perhitungan untuk memetakan angka BMI tersebut ke dalam skala 0 hingga 1.

Misalnya, kita tetapkan bahwa angka BMI 40 adalah batas maksimal (artinya bar akan terisi penuh atau `1.0`):

```python
nilai_aman = min(bmi / 40, 1.0)
st.progress(nilai_aman)
```

Fungsi `min(angka1, angka2)` akan mengambil angka yang paling kecil di antara keduanya. Ini memastikan bahwa jika ada pengguna dengan BMI lebih dari 40 (misalnya 45), maka nilai yang dimasukkan ke `st.progress()` tetap maksimal `1.0`, sehingga aplikasi tidak mengalami error.

## Menghubungkan Riwayat Perhitungan ke Google Sheets

Menghubungkan aplikasi kita ke Google Sheets memungkinkan kita menyimpan data secara permanen layaknya memiliki database sendiri.

Kita akan menggunakan library `st-gsheets-connection` yang dirancang khusus agar Streamlit bisa berinteraksi dengan Google Sheets dengan sangat mudah.

### Langkah 1: Siapkan Google Sheet

Buatlah sebuah Google Sheet baru dan beri nama, misalnya `BMI_History`. Di baris pertama (Header), buatlah kolom-kolom berikut:

- **Nama**
- **Gender**
- **Berat**
- **Tinggi**
- **BMI**
- **Kategori**
- **Saran**
- **Tanggal**

### Langkah 2: Dapatkan Kunci dari Google Cloud Console

1. Buka [Google Cloud Console](https://console.cloud.google.com/).
2. Buat **Project baru**.
3. Cari dan aktifkan (**Enable**) dua API ini: `Google Sheets API` dan `Google Drive API`.
4. Masuk ke menu **Credentials** > **Create Credentials** > **Service Account**.
5. Setelah akun dibuat, masuk ke tab **Keys** > **Add Key** > **Create New Key** > pilih **JSON**.
6. File JSON akan terunduh otomatis. **Simpan baik-baik file ini.**

### Langkah 3: Bagikan Akses

Buka file JSON tadi, cari bagian `"client_email"`. Salin alamat email tersebut (berakhiran `@project-id.iam.gserviceaccount.com`), lalu **Share** Google Sheet ke alamat email tersebut dengan akses sebagai **Editor**.

### Langkah 4: Konfigurasi Secrets

1. Buat folder `.streamlit` di dalam folder proyek.
2. Di dalam folder tersebut, buat file `secrets.toml`.
3. Salin isi file JSON ke dalam `secrets.toml` dengan format:

```toml
[connections.gsheets]
type = "service_account"
project_id = "id-proyek-anda"
private_key_id = "id-kunci-anda"
private_key = "-----BEGIN PRIVATE KEY-----\nISI_KUNCI_RAHASIA_ANDA\n-----END PRIVATE KEY-----\n"
client_email = "nama-akun@project-id.iam.gserviceaccount.com"
spreadsheet = "https://docs.google.com/spreadsheets/d/ID_SHEET_ANDA/edit"
```

### Langkah 5: Instalasi Library

```bash
pip install st-gsheets-connection pandas
```

## Refactoring: Pattern MVC (Model-View-Controller)

Seiring berkembangnya fitur aplikasi, kode dalam satu file (`app.py`) bisa menjadi sangat panjang dan sulit dikelola. Oleh karena itu, kita perlu melakukan **refactoring** dengan menggunakan pattern **MVC (Model-View-Controller)**.

### Masalah yang Dihadapi

Pada kode awal, kita meletakkan semua logika — mulai dari input, perhitungan, pencategorian, hingga tampilan — dalam satu file. Ini memiliki beberapa kekurangan:

1. **Sulit diuji**: Tidak bisa menguji fungsi logika perhitungan secara independen.
2. **Kode berantakan**: Semakin banyak fitur, semakin panjang file-nya.
3. **Violasi Separation of Concerns**: Logika bisnis bercampur dengan tampilan UI.

### Solusi: Pattern MVC

Kita memecah `app.py` menjadi tiga layer dengan tanggung jawab masing-masing:

```text
kalkulator-bmi/
├── app.py                    # Titik masuk utama (orchestrator)
├── models/                   # Model - Data classes dan business logic
│   ├── bmi_model.py         # BMIRecord, BMICalculator
│   └── storage_model.py     # StorageManager
├── controllers/              # Controller - Business logic orchestration
│   └── bmi_controller.py   # BMIController
└── views/                   # View - UI components
    ├── sidebar_view.py      # SidebarView
    └── results_view.py     # ResultsView
```

### File Model: `models/bmi_model.py`

File ini berisi **data class** dan **business logic** untuk BMI. Model tidak bergantung pada Streamlit sehingga mudah diuji.

```python
"""BMI Model - Data class and calculator logic."""
from dataclasses import dataclass
from enum import Enum


class BMICategory(Enum):
    """Enum untuk kategori BMI."""
    UNDERWEIGHT = "Berat Badan Kurang (Underweight)"
    NORMAL = "Berat Badan Ideal (Normal)"
    OVERWEIGHT = "Berat Badan Berlebih (Overweight)"
    OBESITY = "Obesitas"


@dataclass
class BMIRecord:
    """Data class untuk menyimpan record data BMI."""
    nama: str
    gender: str
    berat: float
    tinggi: float
    skor_bmi: float
    kategori: str
    saran: str


class BMICalculator:
    """Calculator class untuk menghitung BMI dan menentukan kategori."""

    CATEGORIES = [
        (18.5, BMICategory.UNDERWEIGHT, "Perbanyak asupan nutrisi dan kalori sehat."),
        (24.9, BMICategory.NORMAL, "Pertahankan pola makan seimbang dan olahraga rutin."),
        (29.9, BMICategory.OVERWEIGHT, "Cobalah untuk lebih aktif bergerak dan kurangi gula."),
    ]

    @classmethod
    def hitung_bmi(cls, berat_kg: float, tinggi_cm: float):
        tinggi_m = tinggi_cm / 100
        skor_bmi = berat_kg / (tinggi_m ** 2)

        for batas, enum_kategori, saran in cls.CATEGORIES:
            if skor_bmi < batas:
                return round(skor_bmi, 2), enum_kategori.value, saran

        return round(skor_bmi, 2), BMICategory.OBESITY.value, "Disarankan berkonsultasi dengan tenaga medis."
```

Kode di atas menunjukkan cara menulis program yang bersih (clean code) dengan memisahkan logika perhitungan dari tampilan visual. Ini disebut sebagai Domain Logic atau Business Logic.
Berikut adalah penjelasan tiap bagiannya dengan bahasa yang sederhana:

1. BMICategory (Daftar Pilihan Tetap)Bayangkan ini sebagai "Label Resmi". Di sini kita menggunakan Enum untuk mendefinisikan kategori BMI.Tujuannya: Agar kita tidak salah tulis teks (misal: "Obesitas" tertulis "Obessitas"). Dengan menggunakan Enum, pilihan kategori menjadi standar dan konsisten di seluruh aplikasi.
2. BMIRecord (Kotak Penyimpanan Data)Ini menggunakan fitur Python bernama @dataclass. Fungsinya adalah sebagai wadah untuk menyimpan informasi satu orang pengguna secara rapi.Di dalamnya terdapat nama, jenis kelamin, berat, tinggi, hingga skor BMI dan saran medisnya.Ibaratnya: Ini adalah formulir digital yang sudah terisi lengkap.
3. BMICalculator (Si Otak Perhitungan)Ini adalah bagian terpenting karena berisi instruksi cara menghitung.

- CATEGORIES: Ini adalah tabel referensi. Berisi batasan angka (18.5, 24.9, 29.9), kategori yang sesuai, dan saran kesehatan yang harus diberikan.
- Metode hitung_bmi:
  1. Konversi Tinggi: Mengubah tinggi dari centimeter (cm) ke meter (m) karena rumus BMI membutuhkan satuan meter.
  2. Rumus BMI: Menghitung berat dibagi tinggi pangkat dua ($BMI = \frac{berat}{tinggi^2}$).
  3. Pencarian Otomatis: Kode ini melakukan pengulangan (loop) untuk mencocokkan skor BMI kamu dengan tabel referensi. Jika skor kamu di bawah batas tertentu, aplikasi langsung tahu apa kategorimu dan saran apa yang cocok.
  4. Hasil Akhir: Mengembalikan angka BMI yang sudah dibulatkan (2 angka di belakang koma), nama kategorinya, dan saran kesehatannya.

Mengapa Kode Ini Sangat Bagus?

1. Mandiri: Kode ini tidak peduli apakah kamu menggunakan Streamlit, website biasa, atau aplikasi HP. Perhitungannya tetap sama dan bisa dipakai di mana saja.
2. Mudah Diuji: Karena tidak tercampur dengan urusan tampilan (tombol, warna, dsb), kita bisa mengetes apakah hitungannya benar dengan sangat mudah.
3. Rapi: Jika suatu saat standar kesehatan dunia (WHO) mengubah angka kategori BMI, kamu cukup mengubah angka di bagian CATEGORIES saja tanpa harus membongkar seluruh kode aplikasi.

### File Model: `models/storage_model.py`

File ini berisi logic untuk menyimpan data ke Google Sheets.

```python
"""Storage Model - Google Sheets storage management."""
import pandas as pd
from datetime import datetime
import streamlit as st
from streamlit_gsheets import GSheetsConnection

from models.bmi_model import BMIRecord


class StorageManager:
    """Manager class untuk operasi penyimpanan data ke Google Sheets."""

    WORKSHEET_NAME = "Sheet1"

    @staticmethod
    @st.cache_resource
    def _get_connection():
        """Mendapatkan koneksi Google Sheets dengan caching."""
        return st.connection("gsheets", type=GSheetsConnection)

    @classmethod
    def simpan_record(cls, record: BMIRecord) -> bool:
        """Simpan satu record BMI ke Google Sheets."""
        conn = cls._get_connection()
        data_lama = conn.read(worksheet=cls.WORKSHEET_NAME, ttl=0)

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

        if data_lama is not None:
            data_total = pd.concat([data_lama, data_baru], ignore_index=True)
        else:
            data_total = data_baru

        conn.clear(worksheet=cls.WORKSHEET_NAME)
        conn.update(worksheet=cls.WORKSHEET_NAME, data=data_total)
        return True
```

### File Controller: `controllers/bmi_controller.py`

Controller mengkoordinasikan antara Model dan View.

```python
"""BMI Controller - Orchestrates BMI business logic."""
import streamlit as st
from models.bmi_model import BMIRecord, BMICalculator
from models.storage_model import StorageManager


class BMIController:
    """Controller class yang mengkoordinasikan logika bisnis BMI."""

    @staticmethod
    def proses_hitung_bmi(nama: str, gender: str, berat: float, tinggi: float) -> BMIRecord:
        """Proses perhitungan BMI."""
        if not nama or len(nama.strip()) < 3:
            raise ValueError("Nama minimal 3 karakter")

        skor_bmi, kategori, saran = BMICalculator.hitung_bmi(berat, tinggi)
        return BMIRecord(
            nama=nama.strip(),
            gender=gender,
            berat=berat,
            tinggi=tinggi,
            skor_bmi=skor_bmi,
            kategori=kategori,
            saran=saran
        )

    @staticmethod
    def proses_simpan_data(record: BMIRecord) -> bool:
        """Proses penyimpanan data BMI ke Google Sheets."""
        return StorageManager.simpan_record(record)

    @staticmethod
    def inisialisasi_session_state() -> None:
        """Inisialisasi session state yang dibutuhkan aplikasi."""
        defaults = {
            'tombol_hitung_ditekan': False,
            'tombol_simpan_ditekan': False,
            'reset_form': False,
            'bmi_record': None,
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
        if 'nama_input' in st.session_state:
            del st.session_state['nama_input']
```

### File View: `views/sidebar_view.py`

View berisi komponen UI untuk input.

```python
"""Sidebar View - UI components for sidebar input."""
import streamlit as st
from typing import Tuple


class SidebarView:
    """View class untuk komponen sidebar input."""

    NAMA_PLACEHOLDER = "Masukkan nama Anda"
    BERAT_DEFAULT = 60.0
    TINGGI_DEFAULT = 165.0

    @staticmethod
    def render() -> Tuple[str, str, float, float, bool]:
        """Render komponen input di sidebar."""
        st.sidebar.title("Silakan isi data berikut")

        # Cek apakah form perlu di-reset
        should_reset = st.session_state.get('reset_form', False)
        if should_reset:
            if 'nama_input' in st.session_state:
                del st.session_state['nama_input']
            st.session_state.reset_form = False

        nama = SidebarView._render_nama_input(should_reset)
        jenis_kelamin = SidebarView._render_gender_input()
        berat = SidebarView._render_berat_input()
        tinggi = SidebarView._render_tinggi_input()
        tombol_hitung = SidebarView._render_hitut_button()

        SidebarView._render_info_bmi()

        return nama or "", jenis_kelamin, berat, tinggi, tombol_hitung

    @staticmethod
    def _render_nama_input(should_reset: bool = False) -> str:
        """Render input nama."""
        if should_reset:
            return st.sidebar.text_input("Nama:", value="", placeholder=SidebarView.NAMA_PLACEHOLDER, key="nama_input")

        nama_value = st.session_state.get('nama_input', "")
        return st.sidebar.text_input("Nama:", value=nama_value, placeholder=SidebarView.NAMA_PLACEHOLDER, key="nama_input")

    @staticmethod
    def _render_gender_input() -> str:
        return st.sidebar.radio("Jenis Kelamin:", ["Laki-laki", "Perempuan"])

    @staticmethod
    def _render_berat_input() -> float:
        return st.sidebar.number_input("Masukkan Berat Badan (kg)", min_value=1.0, value=SidebarView.BERAT_DEFAULT, step=0.1)

    @staticmethod
    def _render_tinggi_input() -> float:
        return st.sidebar.number_input("Masukkan Tinggi Badan (cm)", min_value=1.0, value=SidebarView.TINGGI_DEFAULT, step=1.0)

    @staticmethod
    def _render_hitut_button() -> bool:
        return st.sidebar.button("Hitung BMI", type="primary")

    @staticmethod
    def _render_info_bmi() -> None:
        st.sidebar.divider()
        st.sidebar.markdown("""
        ### Tentang BMI 💡
        **Body Mass Index (BMI)** adalah cara sederhana untuk memantau status gizi orang dewasa.
        """)
```

### File View: `views/results_view.py`

View berisi komponen UI untuk menampilkan hasil.

```python
"""Results View - UI components for displaying BMI results."""
import streamlit as st

from models.bmi_model import BMIRecord, BMICalculator


class ResultsView:
    """View class untuk komponen tampilan hasil BMI."""

    @staticmethod
    def render_hasil_bmi(record: BMIRecord) -> None:
        """Render komponen tampilan hasil BMI."""
        st.header("📊 Hasil Analisis Kesehatan")
        st.subheader(f"Halo, {record.nama}!")
        st.write(f"Jenis Kelamin: {record.gender}")
        st.divider()

        st.metric(label="Nilai BMI Anda", value=f"{record.skor_bmi:.2f}")
        st.info(f"Kategori BMI: **{record.kategori}**\n\n**Saran**: {record.saran}")

        # Progress bar
        st.write("Posisi BMI Anda dalam skala umum:")
        progress_value = min(record.skor_bmi / BMICalculator.SCALE_MAX, 1.0)
        st.progress(progress_value)

        # Tombol reset
        st.divider()
        if st.button("🔄 Hitung BMI Baru", type="secondary"):
            from controllers.bmi_controller import BMIController
            BMIController.reset_form()
            st.rerun()

    @staticmethod
    def render_welcome() -> None:
        """Render halaman selamat datang."""
        st.title("🏃‍♂️ Kalkulator BMI")
        st.markdown("""
        ### Selamat Datang!
        Silakan isi data diri pada **panel di sebelah kiri**, lalu klik tombol **Hitung BMI**
        untuk mengetahui skor BMI dan kategori kesehatan Anda.
        """)
```

### File Utama: `app.py`

File ini sekarang menjadi sangat rapi dan hanya berisi orchestrasi alur aplikasi.

```python
"""BMI Calculator Application - MVC Architecture."""
import streamlit as st

from controllers.bmi_controller import BMIController
from views.sidebar_view import SidebarView
from views.results_view import ResultsView


def main() -> None:
    """Main application entry point."""
    BMIController.inisialisasi_session_state()

    nama, jenis_kelamin, berat, tinggi, tombol_hitung = SidebarView.render()

    if tombol_hitung:
        _proses_hitung_bmi(nama, jenis_kelamin, berat, tinggi)
    elif st.session_state.tombol_hitung_ditekan and st.session_state.tombol_simpan_ditekan:
        _proses_simpan_data()
    elif st.session_state.tombol_hitung_ditekan:
        _tampilkan_hasil_dengan_tombol_simpan()
    else:
        ResultsView.render_welcome()


def _proses_hitung_bmi(nama: str, gender: str, berat: float, tinggi: float) -> None:
    if len(nama.strip()) < 3:
        st.sidebar.error("⚠️ Nama minimal 3 karakter.")
        ResultsView.render_welcome()
        return

    try:
        record = BMIController.proses_hitung_bmi(nama, gender, berat, tinggi)
        st.session_state.bmi_record = record
        st.session_state.tombol_hitung_ditekan = True
        st.session_state.tombol_simpan_ditekan = False
        ResultsView.render_hasil_bmi(record)
    except ValueError as e:
        st.sidebar.error(f"⚠️ {e}")
        ResultsView.render_welcome()


def _proses_simpan_data() -> None:
    record = st.session_state.bmi_record
    if record is None:
        st.error("❌ Data BMI tidak ditemukan")
        return

    try:
        BMIController.proses_simpan_data(record)
        st.session_state.tombol_simpan_ditekan = False
        st.success("Data berhasil disimpan ke riwayat! ✅")
    except Exception as e:
        st.error(f"❌ **Gagal menyimpan data:** {e}")

    ResultsView.render_hasil_bmi(record)


def _tampilkan_hasil_dengan_tombol_simpan() -> None:
    record = st.session_state.bmi_record
    if record:
        ResultsView.render_hasil_bmi(record)
        if st.button("Simpan Data ke Google Sheets", type="primary"):
            st.session_state.tombol_simpan_ditekan = True
            st.rerun()


if __name__ == "__main__":
    main()
```

### Manfaat Pattern MVC

1. **Separation of Concerns**: Pemisahan jelas antara data (Model), logika (Controller), dan UI (View)
2. **Mudah Diuji**: Model dan Controller bisa diuji tanpa harus menjalankan Streamlit
3. **Kode Bersih**: File utama (`app.py`) menjadi sangat ringkas dan mudah dibaca
4. **Dapat Digunakan Kembali**: View components bisa dipakai ulang di konteks berbeda

Dengan demikian, setiap kali pengguna mengklik tombol "Simpan Data ke Google Sheets", data akan otomatis tersimpan ke Google Sheet yang sudah kita konfigurasi.
