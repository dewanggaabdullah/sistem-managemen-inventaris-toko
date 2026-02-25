import inventory
import instance

def buka_menu():
    print('>>> SISTEM_MANAGEMEN_INVENTARIS_TOKO <<<')
    print('Silahkan masukkan angka yang sesuai dengan nomor pilihan menu:')
    print(' 1. Tambah barang ke inventaris')
    print(' 2. Update stok barang')
    print(' 3. Kurangi stok barang')
    print(' 4. Hapus barang')
    print(' 5. Tampilkan daftar barang')
    print(' 6. Simpan dan memuat data dari file lokal')
    print(' 0. Keluar')

def fitur_tambah_barang():
    print('___fitur tambah barang___')
    while True:
        try:
            barang_baru = 'beras' #input('masukkan nama barang \n >>> ')
            stok_awal = 14 #int(input('masukkan jumlah stok \n >>> '))
            break
        except ValueError:
            print('harap isi dengan benar')
    try:
        if barang_baru in instance._db.daftar_inventaris:
            raise NameError('barang sudah ada,silahkan lihat di menu tampilkan daftar barang')
    except NameError as e:
        print('barang sudah ada,silahkan lihat di menu tampilkan daftar barang')

    else:
        print()
        print('berhasil memasukkan data:')
        instance.tambah_barang_ke_sistem(barang_baru, stok_awal)
        print(f'nama barang: {barang_baru} \njumlah stok: {stok_awal}')
        print('--proses selesai--')

def fitur_update_stok():
    print('___fitur update stok___')
    while True:
        try:
            barang = 'beras' #input('masukkan nama barang buat update stok \n >>> ')
            stok_baru = 10 #int(input('masukkan jumlah stok baru \n >>> '))
            break
        except ValueError:
            print('harap isi dengan benar')       

    if not barang:
        raise FileNotFoundError(f"{Barang} tidak ditemukan")

    if stok_baru < 0:
        raise ValueError('jumlah stok tidak boleh minus')

    kelola = inventory.Kelola(barang, stok_baru)
    kelola.update_stok(barang, stok_baru)
    print()
    print(f'barang bernama: {barang}, berhasil diupdate dengan jumlah stok baru sebanyak: {stok_baru}.')
        
def fitur_kurangi_stok():
    print('___fitur kurangi stok___')
    while True:
        barang = 'beras' #input('masukkan nama barang yang sudah ada untuk dihapus \n >>> ')
        stok_berkurang = 3 #input('masukkan jumlah stok yang ingin dikurangi \n >>> ')
        break

    if not barang:
        raise FileNotFoundError(f"{Barang} tidak ditemukan")

    kelola = inventory.Kelola(barang, stok_berkurang)
    kelola.kurang_stok(stok_berkurang)
    print()
    print(f'stok dari barang: {barang}, telah dikurangi 3 dari jumlah totalnya,silahkan buka menu tampilan daftar barang untuk melihatnya.')
        
def fitur_hapus_barang():
    print("___fitur hapus barang___")
    while True:
        barang = 'beras' #input('silahkan masukkan nama barang yang ingin dihapus dari daftar inventaris')
        break

    if not barang:
        raise FileNotFoundError(f'{barang} tidak ditemukan')

    data = inventory.Data()
    data.hapus_barang(barang)
    
def fitur_tampilkan_daftar():
    print('___fitur tampilkan daftar inventaris toko___')
    data = instance.tampilkan_output()
    print()
    print(data)

def simpan_file_lokal():
    print('masih di develop')

#

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
        fitur_tambah_barang()
        
    elif pilih == 2:
        fitur_update_stok()
        
    elif pilih == 3:
        fitur_kurangi_stok()
    
    elif pilih == 4:
        fitur_hapus_barang()

    elif pilih == 5:
        fitur_tampilkan_daftar()
        
    elif pilih == 6:
        simpan_file_lokal()

    elif pilih == 0:
        print('keluar program') 
        break 

    else:
        print('Angka tidak ada di menu...!')

    try:
        input('\nTekan Enter untuk kembali ke menu...')
    except EOFError:
        break