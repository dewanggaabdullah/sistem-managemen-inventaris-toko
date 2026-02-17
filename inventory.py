import storage
class Kelola:
    daftar_inventaris = []

    def __init__(self, barang, stok):
        self.barang = barang
        self.stok = stok

    def __str__(self):
        return f'Nama barang: {self.barang} - stok: {self.stok}'

    def __repr__(self):
        return self.__str__()

    def tambah_barang(self, barang, stok):
        if stok > 0:
            self.daftar_inventaris[barang] = stok
            return f'berhasil menambahkan: {barang} dengan stok: {stok}.'
        else:
            return 'harap isi stok dengan benar(minimal 1).'

    def hapus_barang(self, barang):
        if barang in daftar_inventaris:
            del self.daftar_inventaris[barang]
            return f'[barang] berhasil di hapus...'
        else:
            return f'{barang} tidak ditemukan dalam daftar'

def fitur_tambah_barang():
    try:
        barang = input('masukkan nama barang >>> ')
        stok = int(input('masukkan jumlah stok >>> '))
    except ValueError:
        print('harap isi dengan benar')
            
    if barang and stok > 0:
        print('berhasil memasukkan data:')
        Kelola.tambah_barang(self, barang, stok)
        return f'[nama_baru] berhasil ditambahkan dengan jumlah stok [jumlah_stok].'
    else:
        print('harap isi nama dan stok dengan benar...!')
    
def update_stok(nama_barang, stok_baru):    
    if nama_barang in daftar_inventaris:
        print('abcd')
    else:
        return f'barang "{nama_barang}" tidak ditemukan'

def fitur_hapus_barang(barang_dihapus):
    if barang_dihapus in daftar_inventaris:
        Kelola.hapus_barang(nama_di_daftar, stok_baru)
    else:
        print('barang tidak ditemukan...')

def tampilkan_daftar():
    if not daftar_inventaris:
        print('daftar kosong...')
    else:
        print(daftar_inventaris)

def simpan_file_lokal():
    print('masih di develop')