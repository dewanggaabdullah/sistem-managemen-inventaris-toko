import os
import json


FILE_NAME = 'data.json'

def simpan_data(daftar_barang):
    data_to_save = []
    for item in daftar_barang:
        data_to_save.append({
            "nama": item.nama,
            "stok": item.stok
        })

    with open(FILE_NAME, "w") as f:
        json.dump(data_to_save, f, indent=4)

        print('data berhasil disimpan ke data.json...')

def muat_data():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as f:
        try:
            data_mentah = json.load(f)
            return data_mentah
        except json.JSONDecodeError:
            return []

daftar_inventaris = []