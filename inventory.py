import json
import os

FILE_PATH = 'data/storage.json'

# Pastikan folder 'data' ada agar tidak terjadi FileNotFoundError
os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

def muat_data():
    """Membaca data dari berkas JSON saat program pertama kali berjalan"""
    if not os.path.exists(FILE_PATH):
        simpan_data({})
        return {}

    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

def simpan_data(data):
    """Menyimpan dictionary inventaris terbaru ke dalam berkas JSON"""
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)