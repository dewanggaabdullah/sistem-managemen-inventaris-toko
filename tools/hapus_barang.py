import inventory

def hapus_barang():
    print('\n__HAPUS BARANG__')
    persediaan = inventory.muat_data()

    while True:
        barang = input('masukkan nama barang yang ingin dihapus\n>> ').strip()

        if not barang:
            print('\nproses invalid... nama barang tidak boleh kosong.')
            continue

        if barang in persediaan:
            validasi = input(f'apakah anda benar benar ingin menghapus barang bernama "{barang}"?\n [y/n] >>> ').strip().lower()

            if not validasi or validasi not in ["y", "n"]:
                print('\ntolong jawab "y" untuk ya atau "n" untuk tidak.')
                continue

            elif validasi == 'y':
                del persediaan[barang]
                inventory.simpan_data(persediaan)
                print(f'\nbarang bernama {barang} berhasil dihapus, silahkan ke menu daftar inventaris untuk melihatnya')
                break

            elif validasi == 'n':
                print("\nbarang tidak dihapus, kembali ke menu.")
                return            
        else:
            print('\nproses invalid...')
            print('barang tidak ada di dalam daftar')
            break