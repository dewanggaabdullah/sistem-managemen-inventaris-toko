import pytest
from unittest.mock import patch, MagicMock
import engine

# ==============================================================================
#  TEST UBAH STOK (Uji coba loop 'while True')
# ==============================================================================

# SKENARIO 1: Sukses mengubah stok setelah sebelumnya salah memasukkan nama barang
@patch('engine.inventory.simpan_data') 
@patch('engine.inventory.muat_data') 
@patch('builtins.input') 
def test_ubah_stok_sukses(mock_input, mock_muat, mock_simpan, capsys):
    # 1. Siapkan data tiruan (mock data) dan input pengguna
    mock_muat.return_value = {"Apel": {"stok": 10}}
    
    # Putaran 1: Ketik "Mangga" (Error: tidak ditemukan -> loop nama barang)
    # Putaran 2: Ketik "Apel" (Benar nama barang) -> Ketik "15" (Stok baru -> sukses & break)
    mock_input.side_effect = ["Mangga", "Apel", "15"]
    
    # 2. Jalankan fungsi yang mau dites
    engine.ubah_stok()
    
    # 3. Tangkap output yang dicetak (print) ke terminal
    captured = capsys.readouterr()
    
    # 4. Asersi (pembuktian)
    assert 'Error: Barang "Mangga" tidak ditemukan.' in captured.out
    assert 'Sukses! Stok Apel sekarang menjadi 15.' in captured.out
    mock_simpan.assert_called_once_with({"Apel": {"stok": 15}})


# SKENARIO 2: Menangani kesalahan input stok bukan angka (ValueError) lalu berhasil pada percobaan berikutnya
@patch('engine.inventory.simpan_data') 
@patch('engine.inventory.muat_data') 
@patch('builtins.input') 
def test_ubah_stok_memicu_value_error_lalu_berhasil(mock_input, mock_muat, mock_simpan, capsys):
    # 1. Siapkan data tiruan (mock data) dan input pengguna
    mock_muat.return_value = {"Apel": {"stok": 10}}
    
    # JIKA KODE ENGINE.PY SUDAH DIPERBAIKI MENGGUNAKAN NESTED LOOP:
    # 1. Input nama barang: "Apel"
    # 2. Input stok ke-1: "dua_puluh" (Gagal, mengulang loop khusus stok)
    # 3. Input stok ke-2: "20" (Sukses angka -> simpan & break)
    mock_input.side_effect = ["Apel", "dua_puluh", "20"]
    
    # 2. Jalankan fungsi yang mau dites
    engine.ubah_stok()
    
    # 3. Tangkap output yang dicetak (print) ke terminal
    captured = capsys.readouterr()
    
    # 4. Asersi (pembuktian)
    assert 'Error: Harap masukkan angka yang valid.' in captured.out
    assert 'Sukses! Stok Apel sekarang menjadi 20.' in captured.out
    mock_simpan.assert_called_once_with({"Apel": {"stok": 20}})