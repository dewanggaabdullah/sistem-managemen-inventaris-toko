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
                print('berhasil memasukkan:')
                print(f'nama barang: {nama_barang}')
                print(f'jumlah stok: {jumlah_stok}')

                return {
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