import pytest
from unittest.mock import patch, MagicMock
import engine  


# ==============================================================================
#  TEST KURANGI STOK (Uji coba validasi logika)
# ==============================================================================


# SKENARIO 1: Gagal mengurangi stok karena jumlah yang diminta melebihi stok tersedia
@patch('engine.inventory.simpan_data') 
@patch('engine.inventory.muat_data') 
@patch('builtins.input') 
# PERBAIKAN 1: Mengubah urutan parameter menjadi (mock_input, mock_muat, mock_simpan)
def test_kurangi_stok_gagal_karena_melebihi_stok(mock_input, mock_muat, mock_simpan, capsys):
    # Data awal simulasi
    mock_muat.return_value = {"Apel": {"stok": 10}}
    
    # PERBAIKAN 2: Menghapus "Apel" kedua karena program sekarang mengunci input angka
    # 1. Pilih "Apel" (Nama barang)
    # 2. Kurangi "12" (Gagal, stok kurang -> loop khusus angka mengulang)
    # 3. Kurangi "5" (Sukses -> simpan & break)
    mock_input.side_effect = ["Apel", "12", "5"]
    
    engine.kurangi_stok()
    
    captured = capsys.readouterr()
    
    # Pastikan pesan gagal bawaan engine muncul di terminal
    assert 'Gagal: Stok tidak cukup!' in captured.out
    
    # Pastikan data tersimpan dengan benar setelah input yang valid (10 - 5 = 5)
    mock_simpan.assert_called_once_with({"Apel": {"stok": 5}})


# SKENARIO 2: Menolak jumlah pengurangan angka negatif (Validasi < 1)
@patch('engine.inventory.simpan_data')
@patch('engine.inventory.muat_data')
@patch('builtins.input')
# PERBAIKAN 1: Mengubah urutan parameter menjadi (mock_input, mock_muat, mock_simpan)
def test_kurangi_stok_menolak_angka_negatif(mock_input, mock_muat, mock_simpan, capsys):
    # Data awal simulasi
    mock_muat.return_value = {"Apel": {"stok": 10}}
    
    # PERBAIKAN 2: Menghapus "Apel" kedua karena program sekarang mengunci input angka
    # 1. Pilih "Apel" (Nama barang)
    # 2. Kurangi "-5" (Gagal, ditolak karena < 1 -> loop khusus angka mengulang)
    # 3. Kurangi "3" (Sukses -> simpan & break)
    mock_input.side_effect = ["Apel", "-5", "3"]
    
    engine.kurangi_stok()
    
    captured = capsys.readouterr()
    
    # Pastikan pesan error angka positif muncul di terminal
    assert 'Jumlah pengurangan harus angka positif.' in captured.out
    
    # Pastikan data akhir terpotong dengan benar berdasarkan input yang valid (10 - 3 = 7)
    mock_simpan.assert_called_once_with({"Apel": {"stok": 7}})