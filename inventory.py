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
    from main import barang_ditambah
    from main import jumlah_stok 

    if barang_ditambah and jumlah_stok >= 0:
        print('berhasil memasukkan data:')
        print(f'nama barang: {barang_ditambah}')
        print(f'jumlah stok: {jumlah_stok}')
        return Barang(barang_ditambah, jumlah_stok)
    else:
        print('harap isi nama dan stok dengan benar...!')
    
def update_stok():
    from storage import daftar_inventaris

    while True:
        try:
            nama_barang = input('masukkan nama barang yang ingin di upgrade \n>>> ')
            stok = int(input('masukkan jumlah stok yang baru \n>>> '))
        except ValueError:
            print ('harap isi dengan benar')
        if daftar_inventaris == nama_barang and stok:
            print('berhasil memperbarui stok barang')
            print(inventory.update_stok())
            daftar = daftar_inventaris['nama_barang'] == stok
            print (daftar)
            return daftar_inventaris['nama_barang'] == stok

        else:
            print('barang atau stok tidak ada.')
            return 

def fitur_hapus_barang(barang_dihapus):
    from storage import daftar_inventaris

    if not daftar_inventaris:
        print('daftar kosong...')
        return

    if not barang_dihapus:
        print('nama barang tidak boleh kosong...')
        return

    if barang_dihapus in daftar_inventaris:
        try:
            daftar_inventaris.remove(barang_dihapus)
            print('berhasil hapus: ',barang_dihapus)
        except ValueError:
            print('barang tidak ditemukan...')
    else:
        print('barang tidak ditemukan...')

def tampilkan_daftar():
    from storage import daftar_inventaris
    
    if not daftar_inventaris:
        print('daftar kosong...')
        return
    else:
        print(daftar_inventaris)

def simpan_file_lokal():
    print('masih di develop')