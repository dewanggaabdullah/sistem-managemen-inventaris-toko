import inventory

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