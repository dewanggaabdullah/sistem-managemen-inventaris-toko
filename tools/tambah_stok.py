import inventory

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