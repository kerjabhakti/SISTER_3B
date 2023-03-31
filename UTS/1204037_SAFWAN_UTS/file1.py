import multiprocessing
import time

# Fungsi untuk memproses bimbingan


def process_student_guidance(nama, npm, dosen, jumlah_revisi):
    print(f"Memproses bimbingan {nama} dengan npm {npm} oleh dosen {dosen}...")
    time.sleep(2)
    print(
        f"Mahasiswa dengan npm{npm} nama {nama} telah melakukan bimbingan dengan {dosen} jumlah revisi {jumlah_revisi}")


if __name__ == '__main__':
    # Data pelanggan
    data_bimbingan = [
        {'nama': 'Naruto', 'npm': 1, 'dosen': 'Kakashi', 'jumlah_revisi': 2},
        {'nama': 'Sasuke', 'npm': 2, 'dosen': 'Iruka', 'jumlah_revisi': 3},
        {'nama': 'Sakura', 'npm': 3, 'dosen': 'Minato', 'jumlah_revisi': 1},
        {'nama': 'Choji', 'npm': 4, 'dosen': 'Hiruzen', 'jumlah_revisi': 2},
        {'nama': 'Ino', 'npm': 5, 'dosen': 'Asuma', 'jumlah_revisi': 4},
    ]

    # Proses induk
    print("Data pelanggan sebelum diproses:")
    for dosen in data_bimbingan:
        print(dosen)

    start_time = time.time()

    # Membuat proses baru untuk memproses setiap data pelanggan
    processes = []
    for dosen in data_bimbingan:
        process = multiprocessing.Process(
            target=process_student_guidance, args=(dosen['nama'], dosen['npm'], dosen['dosen'], dosen['jumlah_revisi']))
        processes.append(process)
        process.start()

    # Menunggu semua proses selesai
    for process in processes:
        process.join()

    end_time = time.time()

    print(f"Waktu eksekusi: {end_time - start_time} detik")
    print("Data bimbingan setelah diproses:")
    for dosen in data_bimbingan:
        print(dosen)
