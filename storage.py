import json
import os

FILE_NAME = "data.json"

def simpan_data(daftar_barang):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(daftar_barang, f, indent=4)
    return True

def muat_data():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

daftar_inventaris = []
