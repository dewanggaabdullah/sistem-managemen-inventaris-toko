# Sistem Manajemen Inventaris Toko (CLI)

Proyek ini adalah aplikasi berbasis teks (**Command Line Interface / CLI**) menggunakan **Python 3** untuk mengelola inventaris toko secara efisien. Sistem ini mendukung pencatatan barang, pengelolaan stok, pengujian otomatis (*testing*), serta penyimpanan data berbasis file JSON yang *persistent*.

Proyek ini dirancang modular dengan memisahkan fungsi-fungsi logika bisnis ke dalam *tools* terpisah untuk menjaga kebersihan arsitektur kode (*Modular Architecture*) dan memfasilitasi *unit testing*.

---

## 🚀 Fitur Utama

Aplikasi ini mengimplementasikan operasi pengolahan inventaris interaktif lewat Terminal:
1. **Lihat Daftar Barang** - Menampilkan seluruh inventaris beserta jumlah stok yang tersimpan.
2. **Tambah Barang Baru** - Menambahkan produk baru ke dalam sistem inventaris.
3. **Tambah Stok** - Menambahkan jumlah stok pada barang yang sudah ada.
4. **Kurangi Stok** - Mengurangi stok barang ketika terjadi penjualan/keluar barang.
5. **Ubah Stok** - Memperbarui (*override*) nilai stok barang secara langsung.
6. **Hapus Barang** - Menghapus data barang tertentu dari inventaris.

---

## 🛠️ Teknologi Yang Digunakan

- **Python 3.10+** - Bahasa pemrograman utama.
- **Pytest** - Framework pengujian untuk pengujian unit (*unit testing*) fungsi-fungsi inventaris.
- **JSON** - Database berbasis file lokal (`storage.json`) untuk menyimpan status inventaris secara permanen.
- **Virtual Environment (`venv`)** - Untuk mengisolasi *dependency* dan environment proyek.
- **Git & GitHub** - Untuk manajemen versi kode.

---

## 📂 Struktur Proyek

Arsitektur kode disusun secara modular berdasarkan direktori dan tanggung jawab masing-masing file:

```text
sistem-managemen-inventaris-toko/
│
├── data/
│   ├── storage.json                     # Database lokal penyimpanan inventaris
│   └── storage.json.example             # Template/contoh struktur data awal
│
├── tests/
│   ├── test_tools/                      # Kumpulan pengujian unit (unit test) untuk modul tools
│   ├── conftest.py                      # Konfigurasi fixture pytest
│   ├── test_agent.py                    # Test runner / pengujian khusus
│   └── test_tools_regression.py         # Regression test suite
│
├── tools/                               # Modul modular fitur inventaris
│   ├── __init__.py
│   ├── hapus_barang.py
│   ├── kurangi_stok.py
│   ├── lihat_daftar.py
│   ├── tambah_barang.py
│   ├── tambah_stok.py
│   └── ubah_stok.py
│
├── inventory.py                         # Modul utama akses & manipulasi data inventaris (I/O)
├── main.py                              # Entry point program CLI (Menu Interaktif)
├── pytest.ini                           # Konfigurasi pengujian pytest
├── README.md                            # Dokumentasi proyek
└── requirements.txt                     # Daftar dependensi library Python