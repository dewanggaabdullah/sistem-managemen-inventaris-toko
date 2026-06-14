import pytest
from unittest.mock import patch, MagicMock
import engine  # <--- Sesuai dengan nama file kode inventaris kamu

# ==============================================================================
# 1. TEST TAMBAH BARANG
# ==============================================================================

@patch('engine.inventory.muat_data')
@patch('engine.inventory.simpan_data')
@patch('builtins.input')
def test_tambah_barang_sukses(mock_input, mock_simpan, mock_muat):
    # Simulasi data awal di file JSON
    mock_muat.return_value = {"Apel": {"stok": 10}}
    
    # Simulasi user mengetik nama barang baru: "Jeruk", lalu jumlah stok: "5"
    mock_input.side_effect = ["Jeruk", "5"]
    
    engine.tambah_barang()
    
    # Memastikan data disimpan dengan tambahan barang baru
    mock_simpan.assert_called_once_with({
        "Apel": {"stok": 10},
        "Jeruk": {"stok": 5}
    })

@patch('engine.inventory.muat_data')
@patch('engine.inventory.simpan_data')
@patch('builtins.input')
def test_tambah_barang_gagal_karena_sudah_ada(mock_input, mock_simpan, mock_muat):
    mock_muat.return_value = {"Apel": {"stok": 10}}
    mock_input.side_effect = ["Apel"]  # Ketik barang yang sudah ada
    
    engine.tambah_barang()
    
    # Karena gagal, fungsi simpan_data tidak boleh terpanggil sama sekali
    mock_simpan.assert_not_called()







