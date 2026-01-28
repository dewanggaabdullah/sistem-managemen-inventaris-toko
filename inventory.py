  #isi menu

def tambah_barang_ke_inventaris():
    print('masih tahap develop')

def mengupdate_stok_barang():
    print('masih tahap develop')

def menghapus_barang():
    print('masih tahap develop')

def menampilkan_daftar_barang():
    print('masih tahap develop')

def menyimpan_dan_memuat_data_dari_file_lokal():
    print('masih tahap develop')

#pengelola menu

def handle_menu(pilih):
    if pilih == 1:
        tambah_barang_ke_inventaris()
        return True

    elif pilih == 2:
        mengupdate_stok_barang()
        return True

    elif pilih == 3:
        menghapus_barang()
        return True

    elif pilih == 4:
        menampilkan_daftar_barang()
        return True

    elif pilih == 5:
        menyimpan_dan_memuat_data_dari_file_lokal()
        return True

    elif pilih == 0:
        print('keluar program') 
        return False 

    else:
        print('Angka tidak ada di menu...! \n masukkan ulang input >>> ')
        return False

    