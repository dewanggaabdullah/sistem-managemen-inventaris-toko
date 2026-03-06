import instance

def buka_menu():
    print('>>> SISTEM_MANAGEMEN_INVENTARIS_TOKO <<<')
    print('Silahkan masukkan angka yang sesuai dengan nomor pilihan menu:')
    print(' 1. Tambah barang ke inventaris')
    print(' 2. Update stok barang')
    print(' 3. Kurangi stok barang')
    print(' 4. Hapus barang')
    print(' 5. Tampilkan daftar barang')
    print(' 0. Keluar')

while True:
    buka_menu()
    try:  
        pilih = int(input('>>> '))
    except ValueError:
        print('input yang diberikan harus berupa angka')
    except NameError:
        print('tidak perlu mengetik huruf spesial, cukup angka saja')
    except EOFError:
        continue
    
    if pilih == 1: 
        instance.fitur_tambah_barang()
        
    elif pilih == 2:
        instance.fitur_update_stok()
        
    elif pilih == 3:
        instance.fitur_kurangi_stok()
    
    elif pilih == 4:
        instance.fitur_hapus_barang()

    elif pilih == 5:
        instance.fitur_tampilkan_daftar()

    elif pilih == 0:
        print('keluar program') 
        break 

    else:
        print('Angka tidak ada di menu...!')

    try:
        input('\nTekan Enter untuk kembali ke menu...')
    except EOFError:
        break