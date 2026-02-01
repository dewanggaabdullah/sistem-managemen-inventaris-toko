import json
import os
import fitur_projek

#isi menu




def menampilkan_daftar_barang():
    return 'masih tahap develop'

def menyimpan_dan_memuat_data_dari_file_lokal():
    return 'masih tahap develop'

#pengelola menu

def handle_menu(pilih):
    if pilih == 1:
        fitur_projek.tambah_barang_ke_inventaris()
        return True

    elif pilih == 2:
        fitur_projek.mengupdate_stok_barang()
        return True

    elif pilih == 3:
        fitur_projek.menghapus_barang()
        return True

    elif pilih == 4:
        fitur_projek.menampilkan_daftar_barang()
        return True

    elif pilih == 5:
        fitur_projek.menyimpan_dan_memuat_data_dari_file_lokal()
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
