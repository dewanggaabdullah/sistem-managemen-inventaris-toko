import pytest
from unittest.mock import patch
from engine import tambah_stok 

# ==============================================================================
#  TEST TAMBAH STOK
# ==============================================================================


# SKENARIO 1: Sukses menambah stok barang yang ada
@patch('engine.inventory.simpan_data') # Mock fungsi simpan karena kita tidak ingin menulis ke file asli
@patch('engine.inventory.muat_data') # Mock fungsi muat agar mengembalikan data tiruan
@patch('builtins.input') # Mock builtins.input untuk menyuplai input pengguna
def test_tambah_stok_sukses(mock_input, mock_muat_data, mock_simpan_data, capsys):
    # 1. Siapkan data tiruan (mock data) dan input pengguna
    mock_muat_data.return_value = {
        "Laptop": {"stok": 5}
    }
    
    # Simulasikan input pengguna secara berurutan:
    # 1. Ketik 'Laptop'
    # 2. Ketik '3' (jumlah stok tambahan)
    mock_input.side_effect = ['Laptop', '3']
    
    # 2. Jalankan fungsi yang mau dites
    tambah_stok()
    
    # 3. Tangkap output yang dicetak (print) ke terminal
    captured = capsys.readouterr()
    
    # 4. Asersi (pembuktian) apakah data diperbarui & disimpan dengan benar
    # Pastikan data yang disimpan diperbarui (5 + 3 = 8)
    mock_simpan_data.assert_called_once_with({"Laptop": {"stok": 8}})
    # Cek apakah pesan sukses tercetak
    assert "stok dari barang bernama Laptop berhasil ditambahkan 3 stok" in captured.out


# SKENARIO 2: Input barang yang TIDAK ada di daftar
@patch('engine.inventory.simpan_data') # Mock fungsi simpan karena kita tidak ingin menulis ke file asli
@patch('engine.inventory.muat_data') # Mock fungsi muat agar mengembalikan data tiruan
@patch('builtins.input') # Mock builtins.input untuk menyuplai input pengguna
def test_tambah_stok_barang_tidak_ditemukan(mock_input, mock_muat_data, mock_simpan_data, capsys):
    # 1. Siapkan data tiruan (mock data) dan input pengguna
    mock_muat_data.return_value = {
        "Laptop": {"stok": 5}
    }
    
    # Pengguna memasukkan barang yang salah, sistem harus langsung break
    mock_input.side_effect = ['Mouse']
    
    # 2. Jalankan fungsi yang mau dites
    tambah_stok()
    
    # 3. Tangkap output yang dicetak (print) ke terminal
    captured = capsys.readouterr()
    
    # 4. Asersi untuk memastikan fungsi simpan_data tidak pernah dipanggil karena gagal
    mock_simpan_data.assert_not_called()
    assert "proses invalid..." in captured.out
    assert "barang bernama Mouse tidak ditemukan di dalam daftar" in captured.out


# SKENARIO 3: Input jumlah stok salah (ValueError / bukan angka)
@patch('engine.inventory.simpan_data') # Mock fungsi simpan karena kita tidak ingin menulis ke file asli
@patch('engine.inventory.muat_data') # Mock fungsi muat agar mengembalikan data tiruan
@patch('builtins.input') # Mock builtins.input untuk menyuplai input pengguna
def test_tambah_stok_input_bukan_angka(mock_input, mock_muat_data, mock_simpan_data, capsys):
    # 1. Siapkan data tiruan (mock data) dan input pengguna
    mock_muat_data.return_value = {
        "Laptop": {"stok": 5}
    }
    
    # Pengguna memasukkan nama barang benar, tapi memasukkan jumlah stok berupa teks/huruf
    mock_input.side_effect = ['Laptop', 'banyak']
    
    # 2. Jalankan fungsi yang mau dites
    tambah_stok()
    
    # 3. Tangkap output yang dicetak (print) ke terminal
    captured = capsys.readouterr()
    
    # 4. Asersi untuk memastikan data TIDAK BOLEH tersimpan karena input rusak
    mock_simpan_data.assert_not_called()
    assert "proses invalid..." in captured.out
    assert "harap masukkan input dengan benar" in captured.out


# SKENARIO 4: Input jumlah stok negatif (Validasi < 1) -> memicu `continue` baru kemudian `break`
@patch('engine.inventory.simpan_data') # Mock fungsi simpan karena kita tidak ingin menulis ke file asli
@patch('engine.inventory.muat_data') # Mock fungsi muat agar mengembalikan data tiruan
@patch('builtins.input') # Mock builtins.input untuk menyuplai input pengguna
def test_tambah_stok_angka_negatif(mock_input, mock_muat_data, mock_simpan_data, capsys):
    # 1. Siapkan data tiruan (mock data) dan input pengguna
    mock_muat_data.return_value = {
        "Laptop": {"stok": 5}
    }
    
    # Perulangan while akan berputar kembali (continue) jika menginput angka negatif.
    # Putaran 1: Ketik Laptop -> Ketik -5 (gagal, muncul pesan, lalu continue)
    # Putaran 2: Ketik Laptop -> Ketik 2 (sukses, lalu break)
    mock_input.side_effect = ['Laptop', '-5', 'Laptop', '2']
    
    # 2. Jalankan fungsi yang mau dites
    tambah_stok()
    
    # 3. Tangkap output yang dicetak (print) ke terminal
    captured = capsys.readouterr()
    
    # 4. Asersi (pembuktian) apakah data diperbarui & disimpan dengan benar setelah lolos validasi
    # Pastikan pada akhirnya data tersimpan dengan benar (5 + 2 = 7)
    mock_simpan_data.assert_called_once_with({"Laptop": {"stok": 7}})
    assert "Jumlah penambahan harus angka positif." in captured.out
    assert "stok dari barang bernama Laptop berhasil ditambahkan 2 stok" in captured.out