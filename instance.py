import inventory

def fitur_tambah_barang():
    print('__fitur tambah barang__')
    while True:
        try:
            barang_baru = input('nama barang\n >>')
            stok_baru = int(input('jumlah stok\n >>'))
        
            if barang_baru in inventory.Kelola.daftar_inventaris:
                raise KeyError('barang sudah ada...')
            break
        except ValueError:
            print('harap masukkan input yang benar...')
            break
        except Exception:
            print('ada kesalahan tak terduga')
            break
    
    print('tambah barang berhasil, ada persediaan baru dengan...')
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
                print(f'barang bernama {barang} tidak ditemukan di dalam daftar...')
                break
            
            print(f'stok dari barang bernama {barang} berhasil diperbarui menjadi {stok_baru}')
            inventory.Kelola.daftar_inventaris[barang] = stok_baru
            break
        except ValueError:
            print('masukkan angka yang valid...')
            break
        except Exception:
            print('ada kesalahan tak terduga')
            break
            
def fitur_kurangi_stok():
    print('__fitur kurang stok__')
    while True:
        try:
            barang = input('masukkan nama barang yang ingin dikurangi\n>> ') 
            stok_berkurang = int(input('masukkan jumlah stok yang berkurang\n>> '))

            if barang not in inventory.Kelola.daftar_inventaris:
                print(f'barang bernama {barang} tidak ditemukan di dalam daftar...')
                break
            
            print(f'stok dari barang bernama {barang} berhasil dikurangi sebanyak {stok_berkurang}')
            inventory.Kelola.daftar_inventaris[barang] -= stok_berkurang
            break
        except ValueError:
            print('harap masukkan input dengan benar')
            break
        except Exception:
            print('ada kesalahan tak terduga')
            break

def fitur_hapus_barang():
    print('__fitur hapus barang__')
    while True:
        try:
            barang = input('masukkan nama barang yang ingin dihapus\n>> ')

            if barang not in inventory.Kelola.daftar_inventaris:
                print('barang tidak ada di dalam daftar...')
                break
            print(f'barang bernama {barang} berhasil dihapus, silahkan lihat fitur daftar inventaris untuk melihatnya')
            del inventory.Kelola.daftar_inventaris[barang]
            break
        except ValueError:
            print('harap masukkan input yang benar...')
            break
        except Exception:
            print('ada kesalahan tak terduga')
            break

def fitur_tampilkan_daftar():
    print('__fitur tampilkan daftar inventaris__')
    for barang, stok in inventory.Kelola.daftar_inventaris.items():
        print(f'nama barang: {barang}\njumlah stok: {stok}')
        print()