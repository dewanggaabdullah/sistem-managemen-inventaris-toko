import pytest
from unittest.mock import patch, MagicMock
import engine  


# ==============================================================================
# 3. TEST KURANGI STOK (Uji coba validasi logika)
# ==============================================================================

@patch('engine.inventory.muat_data')
@patch('engine.inventory.simpan_data')
@patch('builtins.input')
def test_kurangi_stok_gagal_karena_melebihi_stok(mock_input, mock_simpan, mock_muat):
    mock_muat.return_value = {"Apel": {"stok": 10}}
    
    # Input: Pilih "Apel", lalu coba kurangi "12" (stok tidak cukup!)
    # Karena loop while True akan berulang, kita beri input kedua "Apel" lalu kurangi "5" (sukses)
    mock_input.side_effect = ["Apel", "12", "Apel", "5"]
    
    engine.kurangi_stok()
    
    # Data akhirnya harus berkurang 5 (10 - 5 = 5)
    mock_simpan.assert_called_once_with({"Apel": {"stok": 5}})


@patch('engine.inventory.muat_data')
@patch('engine.inventory.simpan_data')
@patch('builtins.input')
def test_kurangi_stok_menolak_angka_negatif(mock_input, mock_simpan, mock_muat):
    mock_muat.return_value = {"Apel": {"stok": 10}}
    
    # Loop 1: Pilih "Apel", kurangi sebanyak "-5" (Ditolak karena < 1!)
    # Loop 2: Pilih "Apel", kurangi sebanyak "3" (Diterima!)
    mock_input.side_effect = ["Apel", "-5", "Apel", "3"]
    
    engine.kurangi_stok()
    
    # Pastikan data akhir terpotong dengan benar (10 - 3 = 7)
    mock_simpan.assert_called_once_with({"Apel": {"stok": 7}})
