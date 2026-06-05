import inventory

# 1
def tambah_barang():
    print('__TAMBAH BARANG BARU__')

    # 1. Ambil data inventaris terbaru dari berkas JSON
    persediaan = inventory.muat_data()

    barang_baru = input('nama barang\n >> ').strip()

    if barang_baru in persediaan:
        print('\nproses invalid...')
        print('barang sudah ada')
        return

    input_stok = input('jumlah stok\n >> ')

    if not input_stok.isdigit():
        print('\nproses invalid...')
        print('input harus berupa angka')
        return

    stok_baru = int(input_stok)

    persediaan[barang_baru] = {"stok": stok_baru}
    # nanti bisa nambah label lain ke depannya, misal: "harga": 5000 

    inventory.simpan_data(persediaan)

    print('tambah barang berhasil, ada persediaan baru dengan...')
    print(f'nama barang: {barang_baru}')
    print(f'jumlah stok: {stok_baru}')

# 2
def ubah_stok():
    print('__UPDATE STOK__')

    persediaan = inventory.muat_data()

    while True:
        barang = input('Masukkan nama barang\n>> ').strip()

        if not barang:
            print('Error: Nama barang tidak boleh kosong.')
            continue

        if barang not in persediaan:
            print(f'Error: Barang "{barang}" tidak ditemukan.')
            continue
            
        try:
            # Mengambil angka stok dari dalam dictionary barang
            stok_saat_ini = persediaan[barang]['stok']
            
            stok_baru = int(input(f'Stok saat ini: {stok_saat_ini}. Masukkan stok baru\n>> '))
            
            if stok_baru < 0:
                print('Jumlah stok tidak boleh negatif.')
                continue

            # Update nilai di dalam nested dictionary
            persediaan[barang]['stok'] = stok_baru
            
            inventory.simpan_data(persediaan) 
            
            print(f'Sukses! Stok {barang} sekarang menjadi {persediaan[barang]["stok"]}.')
            break
        
        except ValueError:
            print('Error: Harap masukkan angka yang valid.')

# 3
def tambah_stok():

    persediaan = inventory.muat_data()

    print('__TAMBAH STOK__')
    while True:
        try:
            barang = input('masukkan nama barang yang ingin ditambah\n>> ') 
            stok_tambahan = int(input('masukkan jumlah stok yang ditambahkan\n>> '))

            if barang not in persediaan:
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

    print('\n__KURANG STOK__')
    
    while True:
        barang = input('Masukkan nama barang\n>> ').strip()

        if barang not in persediaan:
            print(f'Error: Barang "{barang}" tidak ditemukan. Silakan coba lagi.')
            continue # Kembali ke awal loop untuk input ulang
            
        try:
            stok_berkurang = int(input(f'Stok saat ini: {persediaan[barang]}. Masukkan jumlah pengurangan\n>> '))
            
            if stok_berkurang <= 0:
                print('Jumlah pengurangan harus angka positif.')
                continue
            
            if stok_berkurang > persediaan[barang]['stok']:
                print(f'Gagal: Stok tidak cukup! Hanya tersedia {persediaan[barang]}.')
                continue

            persediaan[barang] -= stok_berkurang
            
            inventory.simpan_data(persediaan) 
            
            print(f'Sukses! Stok {barang} sekarang menjadi {persediaan[barang]}.')
            break
            
        except ValueError:
            print('Error: Harap masukkan angka yang valid.')

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
                print(f'\nbarang bernama {barang} berhasil dihapus, silahkan ke menu daftar inventaris untuk melihatnya')
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

    