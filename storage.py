import os
import json

FILE_NAME = 'data.json'

def simpan_data(daftar_barang):

    data_to_save = []

    for item in daftar_barang:

        if isinstance(item, dict):
            name = item.get('nama') or item.get('nama_barang')
            stok = item.get('stok') or item.get('jumlah_stok')

        else:
            name = getattr(item, 'barang', getattr(item, 'nama', None))
            stok = getattr(item, 'stok', getattr(item, 'jumlah_stok', None))

        data_to_save.append({"nama": name, "stok": stok})

    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4, ensure_ascii=False)
    except TypeError as e:
        print('ada tipe data yang salah selagi mengisi JSON: {e}')
        return False
    except (OSError, IOError) as e:
        print('os dan io error selagi menambahkan ke JSON: {e}')
        return False
    except Exception as e:
        print('ada kesalahan yang belum diketahui,hubungi developer buat memberi saran lewat komentar:), {e}')
        return False

    print('data berhasil disimpan ke ->', FILE_NAME)
    return True

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