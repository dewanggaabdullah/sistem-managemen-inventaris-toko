from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
import inventory  # Mengimpor helper JSON (muat_data & simpan_data)

# Inisialisasi FastAPI
app = FastAPI(title="Sistem Manajemen Inventaris Toko API")

#============================================================================================
#                                  DATA SCHEMA (PYNDANTIC)
#============================================================================================

# pakai pydantic untuk validasi tipe data badan request
class BarangSchema(BaseModel):
    nama: str = Field(..., min_length=1, description="Nama barang tidak boleh kosong")
    stok: int = Field(..., ge=0,description='stok baru tidak boleh negatif')

class UpdateStockSchema(BaseModel):
    stock_baru: int = Field(..., ge=0, description='Stok baru tidak boleh bernilai negatif')

#============================================================================================
#                                ENDPOINTS (CONTROLLER LAYER)
#============================================================================================

# LIHAT SEMUA DAFTAR BARANG (GET)
@app.get("/inventaris")
def api_lihat_daftar():
    daftar_inventaris = inventory.muat_data()
    return daftar_inventaris  # FastAPI otomatis mengubah dictionary jadi format JSON API

# TAMBAH BARANG BARU (POST)
@app.post("/inventaris", status_code=status.HTTP_201_CREATED)
def api_tambah_barang(payload: BarangSchema):
    daftar_inventaris = inventory.muat_data()

    nama_barang = payload.nama.strip()
    
    # Validasi: jika barang sudah ada
    if nama_barang in daftar_inventaris:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Barang sudah ada di dalam sistem!"
        )
        
    # Masukkan data baru ke nama barang
    daftar_inventaris[nama_barang] = {"stok": payload.stok}
    inventory.simpan_data(daftar_inventaris)
    
    return {
        "status": "sukses",
        "pesan": f"Berhasil menambahkan {nama_barang}"
     }

# ATUR ULANG STOK / OVERRIDE (PUT)
@app.put("/inventaris/{nama}", status_code=status.HTTP_200_OK)
def api_update_stok(nama: str, payload: UpdateStockSchema):
    daftar_inventaris = inventory.muat_data()
    
    # Validasi: Pastikan barangnya ada dulu di JSON sebelum di-update
    if nama not in daftar_inventaris:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Barang tidak ditemukan!"
        )
        
    # Mengupdate stok berdasarkan data dari request body
    daftar_inventaris[nama]["stok"] = payload.stok_baru
    inventory.simpan_data(daftar_inventaris)
    
    return {
        "status": "sukses",
        "pesan": f"Stok {nama} berhasil diubah menjadi {payload.stok_baru}"
    }

# HAPUS BARANG (DELETE)
@app.delete("/inventaris/{nama}", status_code=status.HTTP_200_OK)
def api_hapus_barang(nama: str):
    daftar_inventaris = inventory.muat_data()
    
    # Validasi: Pastikan barangnya ada sebelum dihapus
    if nama not in daftar_inventaris:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Barang tidak ditemukan!"
        )
        
    # Hapus key barang dari dictionary
    del daftar_inventaris[nama]
    inventory.simpan_data(daftar_inventaris)
    
    return {
        "status": "sukses",
        "pesan": f"Berhasil menghapus {nama} dari inventaris"
    }