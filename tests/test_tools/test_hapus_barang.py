import pytest
from unittest.mock import patch, MagicMock
import engine

# ==============================================================================
# 4. TEST HAPUS BARANG
# ==============================================================================

@patch('engine.inventory.muat_data')
@patch('engine.inventory.simpan_data')
@patch('builtins.input')
def test_hapus_barang_konfirmasi_ya(mock_input, mock_simpan, mock_muat):
    mock_muat.return_value = {"Apel": {"stok": 10}, "Jeruk": {"stok": 5}}
    mock_input.side_effect = ["Apel", "y"]  # Pilih Apel, konfirmasi 'y'
    
    engine.hapus_barang()
    
    # Apel harus hilang dari kamus persediaan
    mock_simpan.assert_called_once_with({"Jeruk": {"stok": 5}})