class Kelola:
    daftar_inventaris = {}

    def __init__(self, barang_baru, stok_awal):
        self.barang = barang_baru
        self.stok = stok_awal

    def tambah_barang(self):
        Kelola.daftar_inventaris[self.barang] = self.stok

    