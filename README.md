# 📖 AL-Quran API

Aplikasi web berbasis **Python Flask** yang dikembangkan untuk memudahkan pengguna menjelajahi dan mengakses informasi Al-Qur'an melalui integrasi API dari [EQuran.id](https://equran.id/).

Aplikasi ini menyediakan informasi surat dalam Al-Qur'an serta detail ayat berdasarkan nomor surat yang dipilih.

## ✨ Fitur Utama

- **Daftar Surat** – Menampilkan daftar surat dalam Al-Qur'an.
- **Detail Surat** – Menampilkan informasi surat berdasarkan nomor surat.
- **Integrasi API** – Mengambil data Al-Qur'an secara langsung melalui EQuran.id API.
- **Antarmuka Web** – Menyediakan tampilan berbasis web yang mudah digunakan.

## 🛠️ Teknologi yang Digunakan

- Python
- Flask
- HTML
- EQuran.id API

## 📁 Struktur Project

```text
AL-Quran_API/
│
├── app.py
├── templates/
│   └── index.html
├── .gitignore
└── README.md
```

## ⚙️ Instalasi dan Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/della436/AL-Quran_API.git
```

### 2. Masuk ke Folder Project

```bash
cd AL-Quran_API
```

### 3. Buat Virtual Environment

```bash
python -m venv .venv
```

Aktifkan virtual environment:

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Instal Dependencies

```bash
pip install flask requests
```

### 5. Jalankan Aplikasi

```bash
python app.py
```

Buka aplikasi melalui browser sesuai alamat lokal yang ditampilkan Flask, biasanya:

```text
http://127.0.0.1:5000
```

## 🌐 Sumber API

Data Al-Qur'an diperoleh melalui:

[EQuran.id API](https://equran.id/apidev)

## 🎯 Tujuan Project

Project ini bertujuan mengembangkan aplikasi web sederhana yang memanfaatkan teknologi API untuk menyediakan akses informasi Al-Qur'an secara praktis dan interaktif.

## 👩‍💻 Pengembang

**Adela Annur Aziiza**

GitHub: [@della436](https://github.com/della436)

---

*AL-Quran API – Menjelajahi Informasi Al-Qur'an melalui Integrasi API.*
