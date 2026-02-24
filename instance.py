import inventory

_db = inventory.Data()

def tambah_barang_ke_sistem(barang_baru, stok_awal):
    try:
        kelola = inventory.Kelola(barang_baru, stok_awal)
        _db.masukkan_data(kelola)
    except ValueError as e:
        print('barang sudah ada, atau ada kesalahan dalam input yang anda berikan ')
    except Exception as e:
        print('error tidak diketahui,silahkan beri tau developer buat diperbaiki')
    
def kurangi_barang():
    print('develop')

def tampilkan_output():
    return _db.tampilkan_daftar()

