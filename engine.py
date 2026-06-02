import inventory

# 1
def tambah_barang():
    print('__TAMBAH BARANG BARU__')

    # 1. Ambil data inventaris terbaru dari berkas JSON
    daftar_inventaris = inventory.muat_data()

    barang_baru = input('nama barang\n >> ').strip()

    if barang_baru in inventory.Kelola.daftar_inventaris:
        print('\nproses invalid...')
        print('barang sudah ada')
        return

    input_stok = input('jumlah stok\n >> ')

    if not input_stok.isdigit():
        print('\nproses invalid...')
        print('input harus berupa angka')
        return

    stok_baru = int(input_stok)

    daftar_inventaris[barang_baru] = {"stok": stok_baru}
    # nanti bisa nambah label lain ke depannya, misal: "harga": 5000 

    inventory.simpan_data(daftar_inventaris)

    print('tambah barang berhasil, ada persediaan baru dengan...')
    print(f'nama barang: {barang_baru}')
    print(f'jumlah stok: {stok_baru}')

# 2
def ubah_stok():
    print('__UPDATE STOK__')
    while True:
        try:
            barang = input('masukkan nama barang yang ada buat di update stocknya\n>> ')
            stok_baru = int(input('masukkan jumlah stok baru\n>> '))

            if barang not in inventory.Kelola.daftar_inventaris:
                print('\nproses invalid...')
                print(f'barang bernama {barang} tidak ditemukan di dalam daftar')
                break
            
            print(f'stok dari barang bernama {barang} berhasil diperbarui menjadi {stok_baru}')
            inventory.Kelola.daftar_inventaris[barang] = stok_baru
            break
        except ValueError:
            print('\nproses invalid...')
            print('harap masukkan angka')
            break

# 3
def tambah_stok():
    print('__TAMBAH STOK__')
    while True:
        try:
            barang = input('masukkan nama barang yang ingin ditambah\n>> ') 
            stok_tambahan = int(input('masukkan jumlah stok yang ditambahkan\n>> '))

            if barang not in inventory.Kelola.daftar_inventaris:
                print('\nproses invalid...')
                print(f'barang bernama {barang} tidak ditemukan di dalam daftar')
                break
            print(f'\nstok dari barang bernama {barang} berhasil ditambahkan {stok_tambahan} stok')
            inventory.Kelola.daftar_inventaris[barang] += stok_tambahan
            break
        except ValueError:
            print('\nproses invalid...')
            print('\nharap masukkan input dengan benar')
            break

# 4
def kurangi_stok():

    persediaan = inventory.muat_data()

    print('__KURANG STOK__')
    
    while True:
        try:
            barang = input('masukkan nama barang yang ingin dikurangi\n>> ').strip() 
            stok_berkurang = int(input('masukkan jumlah stok yang berkurang\n>> ')).strip()

            if barang not in inventory.Kelola.daftar_inventaris:
                print('\nproses invalid...')
                print(f'\nbarang bernama {barang} tidak ditemukan di dalam daftar')
                break
            
            print(f'\nstok dari barang bernama {barang} berhasil dikurangi sebanyak {stok_berkurang}')
            inventory.Kelola.daftar_inventaris[barang] -= stok_berkurang
            break
        except ValueError:
            print('\nproses invalid...')
            print('\nharap masukkan input dengan benar')
            break

# 5
def hapus_barang():

    persediaan = inventory.muat_data()

    print('__HAPUS BARANG__')

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
                print(f'\nbarang bernama {barang} berhasil dihapus, silahkan lihat fitur daftar inventaris untuk melihatnya')
                break

            elif validasi == 'n':
                print("\nbarang tidak dihapus, kembali ke menu.")
                return            
        else:
            # PENTING: Jika barang TIDAK ADA di persediaan, beri tahu user lalu keluar
            print('\nproses invalid...')
            print('barang tidak ada di dalam daftar')
            break

# 6
def lihat_daftar():
    print('__DAFTAR INVENTARIS__')
    daftar_inventaris = inventory.muat_data()

    # Cek variabel lokal 'daftar_inventaris', bukan yang ada di modul inventory
    if daftar_inventaris:
        for barang, stok in daftar_inventaris.items():
            print(f'nama barang: {barang}\njumlah stok: {stok["stok"]}')
            print()
    else:
        print('daftar kosong...')

    """
    Dengan menulis {stok["stok"]}, artinya: "Ambil nama barangnya, lalu dari paket data stok ini,
    preteli dan ambil angka di dalam label "stok"-nya saja." Hasil di terminal pun bakal bersih 
    tanpa kurung kurawal lagi
    """

    