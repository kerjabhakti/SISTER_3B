import asyncio

async def hitung_gaji_pokok(nama):
    print("Menghitung gaji pokok untuk", nama)
    await asyncio.sleep(2) # menunggu 2 detik
    gaji_pokok = 5000000 # anggap gaji pokok = 5 juta
    print("Gaji pokok untuk", nama, "adalah", gaji_pokok)
    return gaji_pokok

async def hitung_tunjangan(nama):
    print("Menghitung tunjangan untuk", nama)
    await asyncio.sleep(3) # menunggu 3 detik
    tunjangan = 1000000 # anggap tunjangan = 1 juta
    print("Tunjangan untuk", nama, "adalah", tunjangan)
    return tunjangan

async def hitung_potongan(nama):
    print("Menghitung potongan untuk", nama)
    await asyncio.sleep(1) # menunggu 1 detik
    potongan = 500000 # anggap potongan = 500 ribu
    print("Potongan untuk", nama, "adalah", potongan)
    return potongan

async def hitung_gaji_karyawan(nama):
    print("Menghitung gaji untuk", nama)
    gaji_pokok = await hitung_gaji_pokok(nama)
    tunjangan = await hitung_tunjangan(nama)
    potongan = await hitung_potongan(nama)
    gaji_total = gaji_pokok + tunjangan - potongan
    print("Gaji total untuk", nama, "adalah", gaji_total)

async def main():
    await asyncio.gather(
        hitung_gaji_karyawan("Karyawan A"),
        hitung_gaji_karyawan("Karyawan B"),
        hitung_gaji_karyawan("Karyawan C")
    )

asyncio.run(main())
