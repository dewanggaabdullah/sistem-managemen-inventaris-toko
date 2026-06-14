import pytest
from unittest.mock import patch, MagicMock
import engine

# ==============================================================================
# 2. TEST UBAH STOK (Uji coba loop 'while True')
# ==============================================================================

@patch('engine.inventory.muat_data')
@patch('engine.inventory.simpan_data')
@patch('builtins.input')
def test_ubah_stok_sukses(mock_input, mock_simpan, mock_muat):
    mock_muat.return_value = {"Apel": {"stok": 10}}
    
    # Simulasi user salah ketik dulu ("Mangga" -> tidak ada), baru ketik yang benar
    # "Mangga" (salah) -> "Apel" (benar) -> "15" (stok baru)
    mock_input.side_effect = ["Mangga", "Apel", "15"]
    
    engine.ubah_stok()
    
    # Memastikan stok Apel berhasil di-overwrite menjadi 15
    mock_simpan.assert_called_once_with({"Apel": {"stok": 15}})


@patch('engine.inventory.muat_data')
@patch('engine.inventory.simpan_data')
@patch('builtins.input')
def test_ubah_stok_memicu_value_error_lalu_berhasil(mock_input, mock_simpan, mock_muat):
    mock_muat.return_value = {"Apel": {"stok": 10}}
    
    # Loop 1: Pilih "Apel", ketik stok baru "dua_puluh" (Memicu ValueError!)
    # Loop 2: Loop berulang, pilih "Apel" lagi, ketik stok baru "20" (Sukses!)
    mock_input.side_effect = ["Apel", "dua_puluh", "Apel", "20"]
    
    engine.ubah_stok()
    
    # Memastikan program tidak crash di tengah jalan akibat ValueError,
    # dan pada akhirnya sukses menyimpan data yang benar (stok jadi 20)
    mock_simpan.assert_called_once_with({"Apel": {"stok": 20}})