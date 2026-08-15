import inventory

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
