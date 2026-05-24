import json
import os

FILE_PATH = 'data/storage.json'

def muat_data():
    """Membaca data dari berkas JSON saat program pertama kali berjalan"""
    # Jika berkas belum ada, buat berkas baru dengan dictionary kosong
    if not os.path.exists(FILE_PATH):
        simpan_data({})
        return {}

    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        # Jika file JSON rusak/corrupt, kembalikan dictionary kosong
        return {}

def simpan_data(data):
    """Menyimpan dictionary inventaris terbaru ke dalam berkas JSON"""
    with open(FILE_PATH, 'w') as file:
        # indent=4 bikin format penulisan JSON di file jadi rapi (tidak sebaris)
        json.dump(data, file, indent=4)


class Kelola:
    daftar_inventaris = {}

    def __init__(self, barang_baru, stok_awal):
        self.barang = barang_baru
        self.stok = stok_awal

    def tambah_barang(self):
        Kelola.daftar_inventaris[self.barang] = self.stok
        