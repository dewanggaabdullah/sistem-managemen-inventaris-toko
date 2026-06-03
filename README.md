# Sistem Manajemen Inventaris Toko API

Project ini adalah aplikasi backend berbasis RESTful API menggunakan **FastAPI** untuk mengelola inventaris toko secara efisien. Sistem ini menangani pencatatan barang, pengelolaan stok secara dinamis, validasi data yang ketat, dan penyimpanan data lokal yang *persistent*.

Project ini dirancang sebagai portfolio backend dengan fokus pada arsitektur kode yang bersih (*Clean Architecture*), pemisahan tanggung jawab (*Separation of Concerns*), dan penerapan praktik Git yang profesional (*Conventional Commits*).

---

## 🚀 Fitur Utama (RESTful Endpoints)

Aplikasi ini mengimplementasikan operasi **CRUD** standar industri melalui HTTP Methods:
1. **`GET /inventaris`** - Melihat seluruh daftar barang beserta jumlah stoknya.
2. **`POST /inventaris`** - Menambahkan produk baru ke sistem menggunakan validasi *Request Body*.
3. **`PUT /inventaris/{nama}`** - Memperbarui atau melakukan *override* stok barang yang sudah terdaftar.
4. **`DELETE /inventaris/{nama}`** - Menghapus data barang secara permanen dari sistem penyimpanan.

---

## 🛠️ Teknologi Yang Digunakan

- **Python 3.10+** - Bahasa pemrograman utama.
- **FastAPI** - Framework modern dan cepat untuk membangun performant web API.
- **Pydantic** - Library untuk validasi data tipe data dan manajemen skema request body.
- **Uvicorn** - Server ASGI kilat untuk menjalankan aplikasi FastAPI.
- **JSON** - Sebagai database lokal sederhana untuk persistensi data.
- **Git & GitHub** - Untuk manajemen versi kode.

---

## 📂 Struktur & Arsitektur Kode

Proyek ini menerapkan konsep pemisahan lapisan tanggung jawab (*Layered Architecture*) untuk memastikan kode mudah dirawat dan dikembangkan:

1. **Schema Layer (`pydantic.BaseModel`)**: Menangani validasi tipe data badan request sebelum masuk ke logic utama (misal: mencegah stok bernilai negatif lewat `Field(ge=0)`).
2. **Controller/Routing Layer (`FastAPI Endpoints`)**: Menangani kontrol alur HTTP request, manajemen status code (`200 OK`, `201 Created`), dan penanganan error (`HTTPException`).
3. **Data Access Layer (`inventory.py`)**: Bertindak sebagai modul I/O terpusat (*Source of Truth*) untuk memuat (*deserialize*) dan menyimpan (*serialize*) data ke file lokal `storage.json`.

---

## 🗺️ Roadmap Pengembangan (Future Plans)

Agar pengembangan proyek tetap terarah dan terukur, berikut adalah tahapan pengembangan (*roadmap*) backend yang akan diimplementasikan ke depannya:

### 📌 Fase 1: Konfigurasi Lingkungan & Keamanan Dasar
- **Isolasi Environment:** Menggunakan Virtual Environment (`venv`) untuk mengisolasi semua dependencies proyek.
- **Dependency Management:** Mengunci versi library menggunakan file `requirements.txt`.
- **Environment Variables:** Mengamankan konfigurasi sensitif (seperti port atau database URL) ke dalam file `.env` menggunakan `python-dotenv`.

### 📌 Fase 2: Migrasi ke SQL Database (Persistence Layer)
- **Integrasi ORM:** Mengintegrasikan **SQLite** sebagai database lokal awal bersama **SQLModel** atau **SQLAlchemy**.
- **Refactor Data Layer:** Mengubah fungsi I/O JSON menjadi *Database Session* yang aman (ACID Compliance).
- **Database Migration:** Menerapkan **Alembic** untuk melacak dan mengelola perubahan struktur tabel database tanpa merusak data lama.

### 📌 Fase 3: Fitur Relasional & Logika Bisnis Tambahan
- **Histori Transaksi (Stock Log):** Membuat tabel `Transaksi` untuk mencatat otomatis setiap aktivitas stok masuk dan keluar beserta waktunya (*timestamp*).
- **Kategori Barang:** Membuat tabel `Kategori` yang berelasi dengan tabel `Barang` (*One-to-Many*).

### 📌 Fase 4: Otomatisasi Uji Coba & Kualitas Kode (QA)
- **Automated Testing:** Menulis unit test menggunakan **`pytest`** dan `TestClient` FastAPI untuk menguji fungsionalitas API secara otomatis.
- **Code Linter & Formatter:** Menerapkan **Ruff** atau **Black** untuk menjaga kerapian kode sesuai standar PEP 8 Python.

---

## 💻 Cara Menjalankan Program

### 1. Prasyarat
Pastikan Python 3.10+ sudah terinstal di sistem kamu.

### 2. Kloning Repository & Masuk Direktori
```bash
git clone [https://github.com/username/sistem_managemen_inventaris_toko.git](https://github.com/username/sistem_managemen_inventaris_toko.git)
cd sistem_managemen_inventaris_toko