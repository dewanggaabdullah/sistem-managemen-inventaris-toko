import inventory

def lihat_daftar():
    print('\n__DAFTAR INVENTARIS__')
    daftar_inventaris = inventory.muat_data()

    # Cek variabel lokal 'daftar_inventaris',  di modul inventory
    if daftar_inventaris:
        for barang, stok in daftar_inventaris.items():
            print(f'nama barang: {barang}\njumlah stok: {stok["stok"]}\n')
    else:
        print('daftar kosong...')