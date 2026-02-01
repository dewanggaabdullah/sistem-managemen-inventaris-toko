import inventory

def tambah_barang_ke_inventaris():
    print('\n>>> tambah barang baru <<<')
    nama = input('masukkan nama barang')
    try:
        stok = int(input('isi stok awal'))

        persediaan = inventory.barang(nama,stok)
        inventory.daftar_inventory.append(inventory.barang_baru)

        print(f'berhasil menambahkan {nama} ke inventaris...')
    
    except ValueError:
        print('input salah,stok harus berupa angka..!')

