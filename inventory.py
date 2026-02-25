import storage
class Kelola:
    def __init__(self, barang, stok):
        self.barang = barang
        self.stok = stok

    def data_ringkas(self):
        return [self.barang, self.stok]

    def tambah_barang(self, barang_baru, stok_awal):
        self.barang += barang_baru
        self.stok += stok_awal

    def update_stok(self, barang, stok_baru):
        if barang in self.barang:
            self.stok = stok_baru
        else:
            raise ValueError("Barang tidak ditemukan")

    def kurang_stok(self, stok_berkurang):
        self.stok -= stok_berkurang

    def __str__(self):
        return f'barang: {self.barang} \nstok: {self.stok}'

class Data:
    def __init__(self):
        self.daftar_inventaris = {}
        
    def masukkan_data(self, instance):
        if instance.barang in self.daftar_inventaris:
            raise ValueError('barang sudah ada')
        if instance.stok < 0:
            raise ValueError('stok tidak boleh mines')

        self.daftar_inventaris[instance.barang] = instance
            
    def hapus_barang(self, barang):
        try:
            if barang in self.daftar_inventaris:
                del self.daftar_inventaris[barang]
                print(f'barang bernama "{barang}" berhasil dihapus,silahkan cek menu tampilkan daftar barang untuk melihatnya')
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print(f'kata kunci {barang} tidak ditemukan dalam daftar,coba lihat ___menu tampilkan daftar barang___')


    def tampilkan_daftar(self, daftar_inventaris = None):
        if not self.daftar_inventaris:
            return 'daftar kosong...'
        else:
            hasil = ""
            for barang in self.daftar_inventaris.values():
                hasil += str(barang) + "\n\n"
            return hasil

    #develop

    def simpan_file_lokal():
        print('masih di develop')

