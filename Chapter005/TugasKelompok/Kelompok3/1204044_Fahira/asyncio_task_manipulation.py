import asyncio

async def hitung_gaji(nama, gaji_per_jam, jam_kerja):
    print(f"Menghitung gaji {nama}...")
    await asyncio.sleep(2)
    total_gaji = gaji_per_jam * jam_kerja
    print(f"{nama} mendapatkan gaji sebesar {total_gaji}.")

async def hitung_honor(nama, honor_per_proyek, jumlah_proyek):
    print(f"Menghitung honor {nama}...")
    await asyncio.sleep(3)
    total_honor = honor_per_proyek * jumlah_proyek
    print(f"{nama} mendapatkan honor sebesar {total_honor}.")

async def proses_penggajian_dan_honor():
    await asyncio.gather(
        hitung_gaji("Andi", 5000, 8),
        hitung_gaji("Budi", 6000, 6),
        hitung_honor("Cici", 3000000, 2),
        hitung_honor("Dedi", 2500000, 3),
    )

asyncio.run(proses_penggajian_dan_honor())
