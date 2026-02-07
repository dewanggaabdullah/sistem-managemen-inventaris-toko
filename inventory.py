#class
class Barang:
    def __init__(self, barang, stok):
        self.barang = barang
        self.stok = stok

    def __str__(self):
        return f'Nama barang: {self.barang} - stok: {self.stok}'

    def __repr__(self):
        return self.__str__()

    def tambah_barang(self, jumlah):
        self.stok += jumlah

    def hapus_barang(self, jumlah):
        self.stok -= jumlah

#menu fitur

def fitur_tambah_barang():
    print('___fitur tambah barang___')  

    while True:
        try: 
            nama_barang = input('masukkan nama barang >>> ')
            jumlah_stok = int(input('masukkan jumlah stok >>> '))

            if nama_barang and jumlah_stok >= 0:
                print('berhasil memasukkan data:')
                print(f'nama barang: {nama_barang}')
                print(f'jumlah stok: {jumlah_stok}')
                return Barang(nama_barang, jumlah_stok)
        except ValueError:
            print('harap isi dengan benar')
    
def update_stok():
    print('masih di develop')

def fitur_hapus_barang(nama_barang):
    from storage import daftar_inventaris
    from storage import data

    if data in daftar_inventaris:
        daftar_inventaris.pop(nama_barang)
        print('berhasil hapus: ',nama_barang)
    else:
        print('barang tidak ditemukan...')

def tampilkan_daftar():
    from storage import daftar_inventaris
    
    if not daftar_inventaris:
        print('daftar kosong...')
    else:
        print(daftar_inventaris)

def simpan_file_lokal():
    print('masih di develop')