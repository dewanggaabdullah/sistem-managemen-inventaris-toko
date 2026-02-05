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
        konversi = jumlah == 0
        self.barang == konversi
        self.stok == konversi


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

def fitur_hapus_barang():
    from storage import daftar_inventaris
    print('___fitur hapus barang___')

    while True:
        try: 
            input_user = input('masukkan nama barang yang ingin dihapus >>> ')
            hapus_barang_user = input_user

            if daftar_inventaris <= 0:
                print('tidak ada yang bisa dihapus')
            elif daftar_inventaris >= 0:
                if daftar_inventaris == hapus_barang_user:
                    print('berhasil menghapus data:')
                    print(Barang(hapus_barang_user) == 0)
        except ValueError:
            print('data tidak ada di daftar...')


def tampilkan_daftar():
    from storage import daftar_inventaris
    print('___tampilan daftar barang___')
    
    if not daftar_inventaris:
        print('daftar kosong...')
    else:
        print(daftar_inventaris)

def simpan_file_lokal():
    print('masih di develop')