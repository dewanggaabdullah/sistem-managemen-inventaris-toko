import pytest
from unittest.mock import patch, MagicMock
import engine

# ==============================================================================
#  TEST TAMBAH BARANG
# ==============================================================================


# SKENARIO 1: Sukses menambah barang baru yang belum ada di daftar
@patch('engine.inventory.simpan_data') # Mock fungsi simpan karena kita tidak ingin menulis ke file asli
@patch('engine.inventory.muat_data') # Mock fungsi muat agar mengembalikan data tiruan
@patch('builtins.input') # Mock builtins.input untuk menyuplai input pengguna
def test_tambah_barang_sukses(mock_input, mock_simpan, mock_muat, capsys):
    # Data awal simulasi
    mock_muat.return_value = {"Apel": {"stok": 10}}
    
    # Simulasikan input pengguna secara berurutan:
    # 1. Ketik 'Jeruk' (nama barang baru)
    # 2. Ketik '5' (jumlah stok awal)
    mock_input.side_effect = ["Jeruk", "5"]
    
    engine.tambah_barang()
    
    captured = capsys.readouterr()
    
    # Pastikan data disimpan dengan tambahan barang baru (Apel tetap ada, Jeruk bertambah)
    mock_simpan.assert_called_once_with({
        "Apel": {"stok": 10},
        "Jeruk": {"stok": 5}
    })


# SKENARIO 2: Gagal menambah barang karena nama barang sudah terdaftar
@patch('engine.inventory.simpan_data')
@patch('engine.inventory.muat_data')
@patch('builtins.input')
def test_tambah_barang_gagal_karena_sudah_ada(mock_input, mock_simpan, mock_muat, capsys):
    # Data awal simulasi
    mock_muat.return_value = {"Apel": {"stok": 10}}
    
    # Pengguna memasukkan nama barang yang sudah ada, sistem harus menolak
    mock_input.side_effect = ["Apel"]  
    
    engine.tambah_barang()
    
    captured = capsys.readouterr()
    
    # Karena gagal, fungsi simpan_data tidak boleh terpanggil sama sekali
    mock_simpan.assert_not_called()


# SKENARIO 3: Gagal menambah barang karena input jumlah stok bukan angka (ValueError)
@patch('engine.inventory.simpan_data')
@patch('engine.inventory.muat_data')
@patch('builtins.input')
def test_tambah_barang_gagal_input_stok_bukan_angka(mock_input, mock_simpan, mock_muat, capsys):
    # Data awal simulasi
    mock_muat.return_value = {"Apel": {"stok": 10}}
    
    # Pengguna memasukkan nama barang benar, tapi memasukkan jumlah stok berupa teks/huruf
    mock_input.side_effect = ["Mangga", "sepuluh"]
    
    engine.tambah_barang()
    
    captured = capsys.readouterr()
    
    # Karena inputnya salah, data TIDAK BOLEH tersimpan ke JSON
    mock_simpan.assert_not_called()