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
            nama_barang = input('masukkan nama barang >>> ')
            jumlah_stok = int(input('masukkan jumlah stok >>> '))

            if nama_barang and jumlah_stok >= 0:
                print('berhasil memasukkan data:')
                print(f'nama barang: {nama_barang}')
                print(f'jumlah stok: {jumlah_stok}')
                return barang(nama_barang, jumlah_stok)
        except ValueError:
            print('harap isi dengan benar')
    
def update_stok():
    print('masih di develop')

def hapus_barang():
    print('masih di develop')

def tampilkan_daftar():
    print('masih di develop')

def simpan_file_lokal():
    print('masih di develop')