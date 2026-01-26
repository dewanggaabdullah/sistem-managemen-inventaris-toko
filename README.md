


# Sistem Manajemen Inventaris Toko

Project ini adalah aplikasi berbasis Python untuk mengelola inventaris toko sederhana, meliputi pencatatan barang, pengelolaan stok, dan penyimpanan data secara lokal.

Project ini dibuat sebagai latihan backend fundamental dengan fokus pada struktur kode, pemisahan tanggung jawab, dan praktik Git yang rapi.

---

## Fitur Utama

- Menambah barang ke inventaris
- Mengupdate stok barang
- Menghapus barang
- Menampilkan daftar barang
- Menyimpan dan memuat data dari file lokal

---

### Teknologi yang Digunakan

- Python 3
- File-based storage (JSON)
- Git & GitHub

---

#### struktur dan logika code

1. sistem_managemen_inventaris_toko/
    ├── main.py             # alur & menu
    ├── inventory.py        # logic bisnis
    ├── storage.py          # simpan / load data
    ├── utils.py            # helper & validasi
    ├── data.json           # data
    └── README.md

2. Pola pikir project:

   - main.py tidak boleh mikir

   - inventory.py tidak boleh input()

   - storage.py tidak tahu menu

   - Setiap file punya satu tanggung jawab

    Kalau ini dilanggar, project tetap jalan... tapi akan busuk di dalam.


3. Jenis kode yang dipakai:

   1. kontrol alur

   2. aturan bisnis

   3. model data

   4. penyimpanan

   5. validasi

   6. utilitas

---

##### Cara Menjalankan Program

1. Pastikan Python 3 sudah terinstall

2. Clone repository ini ke komputer lokal

3. masuk ke directori project
        ketik>>> "cd sistem_managemen_inventaris_toko"

4. jalankan program melalui file utama
        ketik>>> "python main.py"

---

###### Pertanyaan & Diskusi

Jika ada pertanyaan, kebingungan, atau saran perbaikan,silakan buka *Issues* di repository ini agar bisa dibahas secara terbuka.
