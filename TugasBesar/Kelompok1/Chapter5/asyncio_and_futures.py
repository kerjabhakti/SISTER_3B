import asyncio
import sys


async def submit_tugas(student_id):
    # Simulasi waktu pengumpulan tugas
    await asyncio.sleep(2)
    return f"Mahasiswa {student_id} telah mengumpulkan tugasnya"


async def main():
    # Menentukan jumlah mahasiswa yang akan mengumpulkan tugas
    jml_mahasiswa = int(input("Masukan jumlah mahasiswa yang akan mengumpulkan tugas: "))

    tugas = [submit_tugas(i+1) for i in range(jml_mahasiswa)]

    hasils = await asyncio.gather(*tugas)
    for hasil in hasils:
        print(hasil)


if __name__ == '__main__':
    asyncio.run(main())
