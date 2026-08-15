import inventory

def tambah_barang():
    print('\n__TAMBAH BARANG BARU__')

    # 1. Ambil data inventaris terbaru dari berkas JSON
    persediaan = inventory.muat_data()

    barang_baru = input('nama barang\n >> ').strip()

    if barang_baru in persediaan:
        print('\nproses invalid...')
        print('barang sudah ada')
        return

    input_stok = input('jumlah stok\n >> ')

    if not input_stok.isdigit():
        print('\nproses invalid...')
        print('input harus berupa angka')
        return

    stok_baru = int(input_stok)

    persediaan[barang_baru] = {"stok": stok_baru}
    # nanti bisa nambah label lain ke depannya, misal: "harga": 5000 

    inventory.simpan_data(persediaan)

    print('\ntambah barang berhasil, ada persediaan baru dengan...')
    print(f'nama barang: {barang_baru}')
    print(f'jumlah stok: {stok_baru}')