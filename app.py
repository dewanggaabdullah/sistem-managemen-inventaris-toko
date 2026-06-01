from fastapi import FastAPI, HTTPException
import inventory  # Mengimpor helper JSON milikmu (muat_data & simpan_data)

# Inisialisasi FastAPI
app = FastAPI(title="Sistem Manajemen Inventaris Toko API")

# 1. LIHAT DAFTAR BARANG (GET)
@app.get("/inventaris")
def api_lihat_daftar():
    daftar_inventaris = inventory.muat_data()
    return daftar_inventaris  # FastAPI otomatis mengubah dictionary jadi format JSON API

# 2. TAMBAH BARANG BARU (POST)
@app.post("/inventaris")
def api_tambah_barang(nama: str, stok: int):
    daftar_inventaris = inventory.muat_data()
    
    # Validasi: jika barang sudah ada
    if nama in daftar_inventaris:
        raise HTTPException(status_code=400, detail="Barang sudah ada di dalam sistem!")
        
    # Masukkan data baru ke dictionary dan simpan ke JSON
    daftar_inventaris[nama] = {"stok": stok}
    inventory.simpan_data(daftar_inventaris)
    
    return {"status": "sukses", "pesan": f"Berhasil menambahkan {nama} dengan stok {stok}"}

# 3. ATUR ULANG STOK / OVERRIDE (PUT)
@app.put("/inventaris/{nama}")
def api_update_stok(nama: str, stok_baru: int):
    daftar_inventaris = inventory.muat_data()
    
    # Validasi: Pastikan barangnya ada dulu di JSON sebelum di-update
    if nama not in daftar_inventaris:
        raise HTTPException(status_code=404, detail="Barang tidak ditemukan!")
        
    # Timpa stok lama dengan stok baru
    daftar_inventaris[nama]["stok"] = stok_baru
    inventory.simpan_data(daftar_inventaris)
    
    return {"status": "sukses", "pesan": f"Stok {nama} berhasil diubah menjadi {stok_baru}"}

# 4. HAPUS BARANG (DELETE)
@app.delete("/inventaris/{nama}")
def api_hapus_barang(nama: str):
    daftar_inventaris = inventory.muat_data()
    
    # Validasi: Pastikan barangnya ada sebelum dihapus
    if nama not in daftar_inventaris:
        raise HTTPException(status_code=404, detail="Barang tidak ditemukan!")
        
    # Hapus key barang dari dictionary
    del daftar_inventaris[nama]
    inventory.simpan_data(daftar_inventaris)
    
    return {"status": "sukses", "pesan": f"Berhasil menghapus {nama} dari inventaris"}