import inventory
import logging

def buka_menu():
            print('>>> SISTEM_MANAGEMEN_INVENTARIS_TOKO <<<')
            print('Silahkan masukkan angka yang sesuai dengan nomor pilihan menu:')
            print('1. Menambah barang ke inventaris')
            print('2. Mengupdate stok barang')
            print('3. Menghapus barang')
            print('4. Menampilkan daftar barang')
            print('5. Menyimpan dan memuat data dari file lokal')
            print('0. keluar')

while True:
    buka_menu()    
    pilih = int(input('>>> '))

    perintah = inventory.handle_menu(pilih)

    if perintah == False:
        break

    input('\nTekan Enter untuk kembali ke menu...')
