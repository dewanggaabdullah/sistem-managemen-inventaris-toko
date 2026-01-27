import inventory
import logging

def buka_menu():
    while True:
        try:
            print('>>> SISTEM_MANAGEMEN_INVENTARIS_TOKO <<<')
            print('Silahkan masukkan angka yang sesuai dengan nomor pilihan menu:')
            print('1.Menambah barang ke inventaris')
            print('2.Mengupdate stok barang')
            print('3.Menghapus barang')
            print('4.Menampilkan daftar barang')
            print('5.Menyimpan dan memuat data dari file lokal')
            print('Angka selain dari nomor diatas untuk keluar')
            return int(input('Harap masukkan angka nomor pada menu: \n>>> '))

        except ValueError:
            logging.warning('user masukkan input selain angka')
            print('Harap masukkan angka yang valid.')

menu = buka_menu()
if menu == 1:
    print(inventory.tambah_barang_ke_inventaris())

elif menu == 2:
    print(inventory.mengupdate_stok_barang())

elif menu == 3:
    print(inventory.menghapus_barang())

elif menu == 4:
    print(inventory.menampilkan_daftar_barang())

elif menu == 5:
    print(inventory.menyimpan_dan_memuat_data_dari_file_lokal())

else:
    exit()