#isi menu
def tambah_barang():
    return 'masih tahap develop'

def update_stok():
    return 'masih tahap develop'

def hapus_barang():
    return 'masih tahap develop'

def tampilkan_daftar():
    return 'masih tahap develop'

def simpan_file_lokal():
    return 'masih tahap develop'

#pengelola menu

def handle_menu(pilih):
    if pilih == 1:
        tambah_barang()
        return True

    elif pilih == 2:
        update_stok()
        return True

    elif pilih == 3:
        hapus_barang()
        return True

    elif pilih == 4:
        tampilkan_daftar()
        return True

    elif pilih == 5:
        simpan_file_lokal()
        return True

    elif pilih == 0:
        print('keluar program') 
        return False 

    else:
        print('Angka tidak ada di menu...! \n masukkan ulang input >>> ')
        return True

#class

class barang:
    def __init__(self, nama, barang):
        self.nama = nama
        self.barang = barang

    def tambah_barang(self, barang_baru):
        self.barang += barang_baru

    def kurang_barang(self, barang_baru):
        self.barang -= barang_baru

daftar_inventory = []

