import inventory

def fitur_tambah_barang():
    print('__fitur tambah barang__')
    while True:
        try:
            barang_baru = 'dewa' #input('nama barang\n >>')
            stok_baru = 3 #int(input('jumlah stok\n >>'))
        
            if barang_baru in inventory.Kelola.daftar_inventaris:
                raise KeyError('barang sudah ada...')
            break
        except ValueError as e:
            print('input salah...')
        #except Exception as e:
            #print('ada kesalahan tak terduga')
    
    print('tambah barang berhasil...')
    print(f'nama barang: {barang_baru}')
    print(f'jumlah stok: {stok_baru}')
    d = inventory.Kelola(barang_baru, stok_baru)
    d.tambah_barang()

def fitur_update_stok():
    print('__fitur update stock__')
    while True:
        try:
            barang = input('masukkan nama barang yang ada buat di update stocknya\n>> ')
            stok_baru = int(input('masukkan jumlah stok baru\n>> '))
            if barang not in inventory.Kelola.daftar_inventaris:
                raise KeyError
            break
        except KeyError as e:
            print('barang tidak ada di dalam daftar...')
        except ValueError as e:
            print('masukkan angka yang valid...')
        
    if barang in inventory.Kelola.daftar_inventaris:
        inventory.Kelola.daftar_inventaris[barang] = stok_baru

















def fitur_tampilkan_daftar():
    print('__fitur tampilkan daftar inventaris__')
    for barang, stok in inventory.Kelola.daftar_inventaris.items():
        print(f'nama barang: {barang}\njumlah stok: {stok}')