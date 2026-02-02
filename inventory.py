#class

class Barang:
    def __init__(self, barang, stok):
        self.barang = barang
        self.stok = stok

    def tambah_barang(self, jumlah):
        self.stok += jumlah
       
#menu fitur

def menu_tambah_barang():
    print('>>> fitur tambah barang <<<')  
    while True:
        try:    
            nama_barang = int(input('masukkan nama barang >>> '))
            jumlah_stok = int(input('masukkan jumlah stok >>> '))
            return 'perintah berhasil...',{
                'nama_barang':nama_barang,
                'jumlah_stok':jumlah_stok
            }
        except ValueError:
            print('harap isi dengan benar')
    
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
        menu_tambah_barang()
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