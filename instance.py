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
    print('__KURANG STOK__')
    while True:
        try:
            barang = input('masukkan nama barang yang ingin dikurangi\n>> ') 
            stok_berkurang = int(input('masukkan jumlah stok yang berkurang\n>> '))

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
    print('__HAPUS BARANG__')
    while True:
        try:
            barang = input('masukkan nama barang yang ingin dihapus\n>> ')

            if barang not in inventory.Kelola.daftar_inventaris:
                print('\nproses invalid...')
                print('barang tidak ada di dalam daftar')
                break
            print(f'\nbarang bernama {barang} berhasil dihapus, silahkan lihat fitur daftar inventaris untuk melihatnya')
            del inventory.Kelola.daftar_inventaris[barang]
            break
        except ValueError:
            print('\nproses invalid...')
            print('harap masukkan input yang benar')
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

    