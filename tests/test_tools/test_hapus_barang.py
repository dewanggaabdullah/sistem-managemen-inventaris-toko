import pytest
from unittest.mock import patch, MagicMock
import engine

# ==============================================================================
#  TEST HAPUS BARANG
# ==============================================================================


# SKENARIO 1: Sukses menghapus barang setelah konfirmasi 'ya' (y)
@patch('engine.inventory.simpan_data') # Mock fungsi simpan karena kita tidak ingin menulis ke file asli
@patch('engine.inventory.muat_data') # Mock fungsi muat agar mengembalikan data tiruan
@patch('builtins.input') # Mock builtins.input untuk menyuplai input pengguna
def test_hapus_barang_konfirmasi_ya(mock_input, mock_muat, mock_simpan, capsys):
    # Data awal simulasi sebelum penghapusan
    mock_muat.return_value = {"Apel": {"stok": 10}, "Jeruk": {"stok": 5}}
    
    # Simulasikan input pengguna secara berurutan:
    # 1. Ketik 'Apel' (barang yang ingin dihapus)
    # 2. Ketik 'y' (konfirmasi setuju untuk menghapus)
    mock_input.side_effect = ["Apel", "y"]  
    
    engine.hapus_barang()
    
    captured = capsys.readouterr()
    
    # Pastikan data yang disimpan diperbarui (Apel harus hilang dari kamus persediaan)
    mock_simpan.assert_called_once_with({"Jeruk": {"stok": 5}})