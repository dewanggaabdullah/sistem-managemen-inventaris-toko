import pytest
from unittest.mock import patch, MagicMock
import app  # <--- Sesuai dengan nama file kode inventaris kamu

# ==============================================================================
# 2. TEST UBAH STOK (Uji coba loop 'while True')
# ==============================================================================

@patch('app.inventory.muat_data')
@patch('app.inventory.simpan_data')
@patch('builtins.input')
def test_ubah_stok_sukses(mock_input, mock_simpan, mock_muat):
    mock_muat.return_value = {"Apel": {"stok": 10}}
    
    # Simulasi user salah ketik dulu ("Mangga" -> tidak ada), baru ketik yang benar
    # "Mangga" (salah) -> "Apel" (benar) -> "15" (stok baru)
    mock_input.side_effect = ["Mangga", "Apel", "15"]
    
    app.ubah_stok()
    
    # Memastikan stok Apel berhasil di-overwrite menjadi 15
    mock_simpan.assert_called_once_with({"Apel": {"stok": 15}})
