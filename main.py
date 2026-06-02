import engine
import traceback

def buka_menu():
    print('>>> SISTEM_MANAGEMEN_INVENTARIS_TOKO <<<')
    print('Silahkan masukkan angka yang sesuai dengan nomor pilihan menu:')
    print(' 1. Tambah Barang')
    print(' 2. Ubah Stok')
    print(' 3. tambah pasokan stok')
    print(' 4. Kurangi Stok')
    print(' 5. Hapus Barang')
    print(' 6. Lihat Daftar Barang')
    print(' 0. Keluar Aplikasi')

while True:
    buka_menu()

    try:
        input_user = input('>>> ')
        if not input_user.isdigit(): # pakai build in method python, kalau isi variabel bukan angka
            print('Input harus berupa angka! Harap masukkan nomor menu...')
            input('\nTekan Enter untuk kembali ke menu...')
            continue

        pilih = input_user

        pilihan_user = {
            '1' : engine.tambah_barang,
            '2' : engine.ubah_stok,
            '3' : engine.tambah_stok,
            '4' : engine.kurangi_stok,
            '5' : engine.hapus_barang,
            '6' : engine.lihat_daftar
        }

        if pilih in pilihan_user:
            eksekusi = pilihan_user[pilih]
            eksekusi()
        elif pilih == '0':
            print('keluar program') 
            break
        else:
            print('Nomor menu tidak tersedia! Harap masukkan nomor yang benar...')

    except NameError:
        print('Terjadi kesalahan NameError di internal kode.')
        traceback.print_exc()
    except Exception as e:
        print(f'ada kesalahan yang tak terduga... \npesan buat developer\n')
        traceback.print_exc() # ini bakal nampilin tulisan error traceback buat mempermudah debug

    try:
        input('\nTekan Enter untuk kembali ke menu...')
    except (EOFError, KeyboardInterrupt):
        break
