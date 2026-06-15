import inventory

# 1
def tambah_barang():
    print('\n__TAMBAH BARANG BARU__')

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

    print('\ntambah barang berhasil, ada persediaan baru dengan...')
    print(f'nama barang: {barang_baru}')
    print(f'jumlah stok: {stok_baru}')


# 2
def ubah_stok():
    print('\n__UPDATE STOK__')
    persediaan = inventory.muat_data()

    while True:
        barang = input('Masukkan nama barang\n>> ').strip()

        if not barang:
            print('Error: Nama barang tidak boleh kosong.')
            continue

        if barang not in persediaan:
            print(f'Error: Barang "{barang}" tidak ditemukan.')
            continue
            
        # 1. Definisikan kembali stok saat ini agar tidak NameError
        stok_saat_ini = persediaan[barang]['stok']
        
        # 2. GUNAKAN LOOP BARU DI SINI UNTUK MENGUNCI INPUT STOK
        while True:
            try:
                stok_baru = int(input(f'Stok saat ini: {stok_saat_ini}. Masukkan stok baru\n>> '))
                
                if stok_baru < 0:
                    print('Jumlah stok tidak boleh negatif.')
                    continue # Mengulang loop internal ini (minta stok lagi)
                
                break # Keluar dari loop stok jika sukses memasukkan angka valid >= 0
            
            except ValueError:
                print('Error: Harap masukkan angka yang valid.')
                # Tidak ada break/continue di sini berarti otomatis mengulang loop stok ini lagi

        # 3. Proses update & simpan dilakukan DI LUAR loop stok, tapi DI DALAM loop utama
        persediaan[barang]['stok'] = stok_baru
        inventory.simpan_data(persediaan) 
        
        print(f'Sukses! Stok {barang} sekarang menjadi {persediaan[barang]["stok"]}.')
        break # Keluar dari loop utama karena semua proses dari awal sampai simpan sudah sukses


# 3
def tambah_stok():
    print('\n__TAMBAH PASOKAN STOK__')
    persediaan = inventory.muat_data()

    while True:
        barang = input('masukkan nama barang yang ingin ditambah\n>> ').strip() 

        if barang not in persediaan:
            print('\nproses invalid...')
            print(f'barang bernama {barang} tidak ditemukan di dalam daftar')
            break

        try:
            stok_saat_ini = persediaan[barang]['stok']
            stok_tambahan = int(input(f'Stok saat ini: {stok_saat_ini}. Masukkan jumlah barang yang ditambah\n>> '))

            if stok_tambahan < 1:
                print('Jumlah penambahan harus angka positif.')
                continue

            persediaan[barang]['stok'] += stok_tambahan
            inventory.simpan_data(persediaan)
            
            print(f'\nstok dari barang bernama {barang} berhasil ditambahkan {stok_tambahan} stok')
            break
            
        except ValueError:
            print('\nproses invalid...')
            print('harap masukkan input dengan benar')
            break


# 4
def kurangi_stok():
    print('\n__KURANG STOK__')
    persediaan = inventory.muat_data()
    
    while True:
        barang = input('Masukkan nama barang\n>> ').strip()

        if barang not in persediaan:
            print(f'Error: Barang "{barang}" tidak ditemukan. Silakan coba lagi.')
            continue
            
        stok_saat_ini = persediaan[barang]['stok']
        
        # --- BIKIN LOOP BARU UNTUK MENGUNCI INPUT ANGKA ---
        while True:
            try:
                stok_berkurang = int(input(f'Stok saat ini: {stok_saat_ini}. Masukkan jumlah pengurangan\n>> '))
                
                if stok_berkurang < 1:
                    print('Jumlah pengurangan harus angka positif.')
                    continue 
                
                if stok_berkurang > stok_saat_ini:
                    print(f'Gagal: Stok tidak cukup! Hanya tersedia {stok_saat_ini}.')
                    continue 

                # Jika lolos semua validasi angka, keluar dari loop kedua
                break
                
            except ValueError:
                print('Error: Harap masukkan angka yang valid.')
                # Otomatis mengulang loop kedua jika input bukan angka

        # --- PROSES UPDATE & SIMPAN (Di luar loop angka, di dalam loop utama) ---
        persediaan[barang]['stok'] -= stok_berkurang
        inventory.simpan_data(persediaan) 
        
        print(f'Sukses! Stok {barang} sekarang menjadi {persediaan[barang]["stok"]}.')
        break # Keluar dari loop utama karena semua proses sukses

# 5
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


# 6
def lihat_daftar():
    print('\n__DAFTAR INVENTARIS__')
    daftar_inventaris = inventory.muat_data()

    # Cek variabel lokal 'daftar_inventaris',  di modul inventory
    if daftar_inventaris:
        for barang, stok in daftar_inventaris.items():
            print(f'nama barang: {barang}\njumlah stok: {stok["stok"]}\n')
    else:
        print('daftar kosong...')