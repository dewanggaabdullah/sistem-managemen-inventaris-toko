def buka_menu():
    print('>>> SISTEM_MANAGEMEN_INVENTARIS_TOKO <<<')
    print('Silahkan masukkan angka yang sesuai dengan nomor pilihan menu:')
    print(' 1. Menambah barang ke inventaris')
    print(' 2. Mengupdate stok barang')
    print(' 3. Menghapus barang')
    print(' 4. Menampilkan daftar barang')
    print(' 5. Menyimpan dan memuat data dari file lokal')
    print(' 0. keluar')

while True:
    buka_menu()

    try:  
        pilih = int(input('>>> '))
    except ValueError:
        print('angka yang diberikan harus berupa angka!')
        continue
    
    if pilih == 1:
        hasil_tambah = menu_tambah_barang()
        daftar_inventaris.append(hasil_tambah)
        
    elif pilih == 2:
        update_stok()

    elif pilih == 3:
        hapus_barang()
        
    elif pilih == 4:
        tampilkan_daftar()
        
    elif pilih == 5:
        simpan_file_lokal()

    elif pilih == 0:
        print('keluar program') 
        break 

    else:
        print('Angka tidak ada di menu...!')
        

    input('\nTekan Enter untuk kembali ke menu...')