import pytest
from unittest.mock import patch
from engine import lihat_daftar 

# ==============================================================================
#  TEST LIAT DAFTAR
# ==============================================================================


# SKENARIO 1: Mengetes ketika ada barang di inventaris
@patch('engine.inventory.muat_data') # Mock fungsi muat agar mengembalikan data tiruan
def test_lihat_daftar_ada_barang(mock_muat_data, capsys):
    # 1. Siapkan data tiruan (mock data)
    mock_muat_data.return_value = {
        "Laptop": {"stok": 5},
        "Mouse": {"stok": 10}
    }
    
    # 2. Jalankan fungsi yang mau dites
    lihat_daftar()
    
    # 3. Tangkap output yang dicetak (print) ke terminal
    captured = capsys.readouterr()
    
    # 4. Asersi (pembuktian) apakah outputnya sesuai ekspektasi
    assert "__DAFTAR INVENTARIS__" in captured.out
    assert "nama barang: Laptop" in captured.out
    assert "jumlah stok: 5" in captured.out
    assert "nama barang: Mouse" in captured.out
    assert "jumlah stok: 10" in captured.out


# SKENARIO 2: Mengetes ketika inventaris kosong
@patch('engine.inventory.muat_data') # Mock fungsi muat agar mengembalikan data tiruan
def test_lihat_daftar_kosong(mock_muat_data, capsys):
    # 1. Siapkan data tiruan berupa dictionary kosong atau None
    mock_muat_data.return_value = {}
    
    # 2. Jalankan fungsi yang mau dites
    lihat_daftar()
    
    # 3. Tangkap output yang dicetak (print) ke terminal
    captured = capsys.readouterr()
    
    # 4. Asersi (pembuktian) untuk memastikan pesan 'daftar kosong...' muncul
    assert "__DAFTAR INVENTARIS__" in captured.out
    assert "daftar kosong..." in captured.out