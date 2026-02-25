import inventory

_db = inventory.Data()

def objek_tambah_barang(barang_baru, stok_awal):
    try:
        kelola = inventory.Kelola(barang_baru, stok_awal)
        _db.masukkan_data(kelola)
    except ValueError as e:
        print('barang sudah ada, atau ada kesalahan dalam input yang anda berikan ')
    except Exception as e:
        print('error tidak diketahui,silahkan beri tau developer buat diperbaiki')

def objek_update_stok(barang, stok):
    try:
        kelola = inventory.Kelola(barang_baru, stok_awal)
        _db.masukkan_data(kelola)
    except ValueError as e:
        print('barang sudah ada, atau ada kesalahan dalam input yang anda berikan ')
    except Exception as e:
        print('error tidak diketahui,silahkan beri tau developer buat diperbaiki')

def objek_kurangi_stok_barang(barang, stok):
    print('masih dalam develop')

def objek_hapus_barang(barang, stok):
    print('masih dalam develop')

def objek_tampilkan_daftar():
    return _db.tampilkan_daftar()

