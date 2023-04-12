import multiprocessing
import time

# Fungsi untuk memproses data mahasiswa


def process_student_data(nama_mhs, dospem):
    print(f"Proses Pembagian Dosen Pembimbing TA mahasiswa {nama_mhs}...")
    time.sleep(2)
    for dosen in dospem:
        print(f"{nama_mhs} mendapatkan dosen pembimbing, Dosen {dosen}")


if __name__ == '__main__':
    # Data mahasiswa
    student_data = {
        'Naruto': ['Kakaashi', 'Kurenai'],
        'Sakura': ['Iruka', 'Chiyo'],
        'Sasuke': ['Minato', 'Kushina'],
        'Choji': ['Hiruzen', 'Tsunade'],
        'Ino': ['Asuma', 'Orochimaru']
    }

    # Proses induk
    print("Data mahasiswa sebelum diproses:")
    for nama_mhs, dospem in student_data.items():
        print(f"{nama_mhs} Mendapatkan {len(dospem)} Dosen Pembimbing")

    start_time = time.time()

    # Membuat proses baru untuk memproses setiap data mahasiswa
    processes = []
    for nama_mhs, dospem in student_data.items():
        process = multiprocessing.Process(
            target=process_student_data, args=(nama_mhs, dospem))
        processes.append(process)
        process.start()

    # Menunggu semua proses selesai
    for process in processes:
        process.join()

    end_time = time.time()

    print(f"Waktu eksekusi: {end_time - start_time} detik")
    print("Data mahasiswa setelah diproses:")
    for nama_mhs, dospem in student_data.items():
        print(f"Mahasiswa {nama_mhs} memperoleh {len(dospem)} Dosen")
