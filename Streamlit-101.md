# Mini Project Kalkulator BMI dengan Python dan Streamlit

## Tentang Streamlit

Streamlit adalah _framework_ Python yang memungkinkan kita mengubah script Python menjadi aplikasi web interaktif dalam hitungan menit. Kita tidak perlu menguasai HTML, CSS, atau JavaScript untuk membuat antarmuka yang menarik bagi proyek data atau alat bantu sederhana lainnya.

Untuk mempelajarinya secara bertahap, kita akan membuat mini project berupa **Kalkulator BMI (Body Mass Index)**. Proyek ini akan membantu kita memahami bagaimana Streamlit menangani input dari pengguna, melakukan perhitungan di balik layar, dan menampilkan hasilnya kembali ke layar secara _real-time_.

Yang akan kita pelajari adalah:

1. **Persiapan & Instalasi**: Cara membuat virtual environment dan memasang Streamlit di komputer serta menjalankan script "Hello World" pertama kita.
2. **Membangun Antarmuka (UI)**: Mengenal cara membuat _header_, kolom input angka, dan tombol untuk menerima data dari pengguna.
3. **Logika Kalkulator & Output**: Menghubungkan input dengan rumus matematika dan menampilkan hasil serta kategori kesehatan (misal: "Normal" atau "Overweight").

## Instalasi Streamlit

Panduan ini akan memandu Anda membuat lingkungan dengan venv dan menginstal Streamlit dengan pip yang direkomendasikan. Setelah streamlit terinstall, kita akan membuat aplikasi "Hello world" sederhana dan menjalankannya.

### Prasyarat

- Pastikan komputer Anda telah terinstall python dengan versi yang sesuai (3.10 s.d. 3.14).
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

Setelah menjalankan perintah streamlit hello di terminal, Browser akan terbuka secara otomatis dan menampilkan halaman sambutan interaktif yang berisi berbagai demo fitur.

## Buat Script Kalkulator Sederhana

Langkah selanjutnya adalah membuat file script Python untuk aplikasi Kalkulator BMI. Di tahap ini, kita akan fokus membangun tampilan agar pengguna bisa memasukkan data.

Silakan buat file baru bernama app.py di folder kerja, lalu masukkan kode berikut:

```bash
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
`streamlit run app.py`

Setelah menjalankan perintah di atas, tab baru akan terbuka di browser dan menampilkan dua kotak input untuk berat badan dan tinggi badan.

### Penjelasan Script Komponen UI

- st.title(): Digunakan untuk membuat judul besar di bagian atas aplikasi.
- st.number_input(): Membuat kotak input khusus angka. Parameter min_value=1.0 memastikan pengguna tidak memasukkan angka nol atau negatif yang bisa merusak perhitungan matematika nanti.

### Tambahkan Logika Perhitungan BMI

BMI dihitung dengan membagi berat badan (kg) dengan kuadrat tinggi badan dalam satuan meter (berat (kg) / tinggi (m)^2).

Pada langkah sebelumnya kita meminta pengguna memasukkan tinggi dalam satuan sentimeter (cm), maka kita harus mengkonversi variabel tinggi ke dalam meter (tinggi_m = tinngi / 100) kemudian kita hitung bminya.

```bash
# 1. Konversi tinggi dari cm ke meter
tinggi_m = tinggi / 100

# 2. Hitung BMI (berat dibagi tinggi pangkat dua)
# Di Python, pangkat dua ditulis dengan simbol **2
bmi = berat / (tinggi_m ** 2)
```

Dengan kode di atas, setiap kali pengguna mengubah angka di aplikasi web, Streamlit akan otomatis menjalankan ulang script dan menghitung nilai bmi yang baru.

Sekarang kita sudah punya nilai BMI yang tersimpan di variabel bmi. Namun, nilai ini baru ada di "ingatan" komputer dan belum muncul di layar aplikasi web kita. Untuk menampilkan hasil di layar, kita punya beberapa pilihan menarik di Streamlit diantarnya st.write dan st.success.

Berikut cara kita menulisnya dalam kode:

```python
# Menampilkan hasil dengan 2 angka di belakang koma agar rapi
st.write(f"Nilai BMI Anda adalah: {bmi:.2f}")

# Atau jika ingin lebih cantik:
st.success(f"Hasil perhitungan BMI: {bmi:.2f}")
```

Simbol :.2f di dalam kode tersebut berfungsi untuk membatasi angka desimal agar tidak terlalu panjang (misalnya dari 22.4489... menjadi 22.45).

Sekarang, angka BMI sudah muncul di layar. Namun, pengguna mungkin tidak tahu apakah angka 22.5 itu termasuk sehat atau tidak.

Dalam Python, kita biasanya menggunakan if-elif-else untuk mengecek rentang nilai (seperti nilai BMI). Berikut adalah tabel kategori BMI secara umum:

|   Rentang BMI    | Kategori BMI                      |
| :--------------: | :-------------------------------- |
| Kurang dari 18.5 | Berat Badan Kurang (Underweight)  |
|   18.5 – 24.9    | Berat Badan Normal                |
|   25.0 – 29.9    | Berat Badan Berlebih (Overweight) |
| 30.0 atau lebih  | Obesitas                          |

Struktur if-elif-else di Python bekerja seperti percabangan jalan. Program akan memeriksa satu per satu kondisi dari atas ke bawah, dan berhenti begitu menemukan kondisi yang benar (True).
Berikut adalah cara kita menuliskan logika kategori BMI tersebut ke dalam kode:

```python
if bmi < 18.5:
    KATEGORI = "Berat Badan Kurang (Underweight)"
    st.warning(KATEGORI)
elif 18.5 <= bmi <= 24.9:
    KATEGORI = "Berat Badan Normal"
    st.success(kateKATEGORIgori)
elif 25.0 <= bmi <= 29.9:
    KATEGORI = "Berat Badan Berlebih (Overweight)"
    st.warning(KATEGORI)
else:
    KATEGORI = "Obesitas"
    st.error(KATEGORI)
```

Penjelasan Kode:

- if: Kondisi pertama yang diperiksa.
- elif (else if): Digunakan untuk memeriksa kondisi berikutnya jika kondisi sebelumnya salah. Kita bisa menggunakan elif sebanyak yang dibutuhkan.
- else: Pilihan terakhir jika tidak ada satupun kondisi di atas yang terpenuhi (dalam hal ini, jika BMI 30 atau lebih).
- st.warning / st.success / st.error: Ini adalah cara Streamlit menampilkan pesan dengan warna yang berbeda (kuning, hijau, dan merah) agar tampilan aplikasi lebih informatif.

## Buat hasil perhitungan lebioh informatif dengan popup dialog

Untuk membuat popup, kita akan menggunakan fitur bernama @st.dialog. Ini adalah "dekorator" yang mengubah sebuah fungsi menjadi jendela munculan (modal).

Berikut adalah cara menyusun kodenya:

```python
# 1. Kita siapkan fungsi untuk popup-nya
@st.dialog("Hasil Perhitungan BMI")
def tunjukkan_hasil(n, jk, nilai, kat):
    st.write(f"Halo, **{n}**! 👋")
    st.write(f"Jenis Kelamin: {jk}")
    st.divider() # Garis pemisah
    st.metric(label="BMI Anda", value=f"{nilai:.2f}")
    st.info(f"Kategori: **{kat}**")

# 2. Membuat tombol untuk memicu perhitungan
if st.button("Hitung BMI Sekarang"):
    # (Logika perhitungan kita yang sebelumnya diletakkan di sini)
    tinggi_m = tinggi / 100
    bmi = berat / (tinggi_m ** 2)

    # Menentukan kategori
    if bmi < 18.5:
        kategori = "Berat Badan Kurang"
    elif 18.5 <= bmi <= 24.9:
        kategori = "Normal"
    elif 25.0 <= bmi <= 29.9:
        kategori = "Overweight"
    else:
        kategori = "Obesitas"

    # 3. Memanggil fungsi popup
    tunjukkan_hasil(nama, jenis_kelamin, bmi, kategori)
```

### Penjelasan Komponen Baru

- @st.dialog("Judul"): Menandakan bahwa fungsi di bawahnya akan muncul sebagai jendela di tengah layar.
- st.metric(): Menampilkan angka dengan format yang lebih menonjol dan profesional.
- st.divider(): Membuat garis horizontal untuk merapikan tampilan teks. ➖

Sekarang aplikasi kita sudah memiliki alur yang lengkap: Input -> Proses (saat tombol diklik) -> Output (lewat popup).

## Merubah Tampilan agar lebih rapi dengan column

```python
# Membuat 2 Column agar lebih rapi
col_nama, col_gender = st.columns(2)
with col_nama:
    # Membuat input nama pengguna
    nama = st.text_input("Masukkan Nama Anda")
with col_gender:
    # Membuat input jenis kelamin (menggunakan st.selectbox atau st.radio)
    jenis_kelamin = st.selectbox("Pilih Jenis Kelamin", ["Laki-laki", "Perempuan"])

# Membuat 2 Column agar lehi rapi
col_berat, col_tinggi = st.columns(2)
with col_berat:
    # Membuat input angka untuk berat badan
    berat = st.number_input("Masukkan Berat Badan (kg)", min_value=1.0, step=0.1)
with col_tinggi:
    # Membuat input angka untuk tinggi badan
    tinggi = st.number_input("Masukkan Tinggi Badan (cm)", min_value=1.0, step=0.1)
```

## Tambah Sidebar

Menggunakan sidebar adalah cara efektif untuk memisahkan antara input/konfigurasi dengan hasil/konten utama. Di Streamlit, kita bisa memindahkan hampir semua elemen ke samping hanya dengan menambahkan kata .sidebar setelah st. 🧭

Bagaimana Sidebar Bekerja?
Bayangkan halaman web kita memiliki dua area:

- Main Area: Tempat untuk judul besar, grafik, atau hasil (seperti popup kita).
- Sidebar: Area di sebelah kiri untuk kontrol atau input data.

Jika sebelumnya kita menulis:
nama = st.text_input("Masukkan nama Anda:")

Maka untuk memindahkannya ke samping kiri, kodenya menjadi:
nama = st.sidebar.text_input("Masukkan nama Anda:")

## Penambahan Progress BMI

Menambahkan Progress Bar akan memberikan visualisasi instan mengenai posisi berat badan seseorang dalam skala kesehatan secara lebih intuitif.

Di Streamlit, kita bisa menggunakan fungsi st.progress(). Namun, ada satu aturan teknis yang penting: nilai yang dimasukkan ke dalam fungsi ini harus berupa angka desimal antara 0.0 (bar kosong) hingga 1.0 (bar penuh).

Masalahnya, angka BMI kita biasanya berkisar antara 10 hingga 40 atau lebih. Kita tidak bisa langsung memasukkan variabel bmi ke dalam progress bar karena nilainya pasti lebih besar dari 1.0. Jadi, kita perlu melakukan sedikit perhitungan untuk memetakan angka BMI tersebut ke dalam skala 0 hingga 1.

Misalnya, kita tetapkan bahwa angka BMI 40 adalah batas maksimal (artinya bar akan terisi penuh atau 1.0).

Namun, ada satu hal kecil yang perlu kita waspadai. Menurutmu, apa yang akan terjadi jika ada pengguna yang memiliki skor BMI sangat tinggi, misalnya 45, sehingga hasil pembagiannya menjadi 1.125?

Mengingat st.progress() hanya menerima angka maksimal 1.0, apa yang perlu kita tambahkan pada kode agar aplikasi tidak mengalami error? Agar aplikasi tidak error, kita harus memastikan bahwa nilai yang masuk ke st.progress() tidak pernah lebih dari 1.0. Kita bisa menggunakan fungsi bawaan Python yaitu min().

Fungsi min(angka1, angka2) akan mengambil angka yang paling kecil di antara keduanya. Jadi, codenya menjadi:
nilai_aman = min(bmi / 40, 1.0)
