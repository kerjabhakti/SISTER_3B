import multiprocessing
import time

def cek_nilai_mahasiswa(mahasiswa):
    nama = mahasiswa["nama"]
    matkul = mahasiswa["matkul"]
    nilai = mahasiswa["nilai"]
    print(f"Mahasiswa {nama} mendapatkan nilai {nilai} pada mata kuliah {matkul}.")
    time.sleep(1)

if __name__ == "__main__":
    data_mahasiswa = [
        {"nama": "Andi", "matkul": "Matematika Diskrit", "nilai": 80},
        {"nama": "Budi", "matkul": "Basis Data", "nilai": 90},
        {"nama": "Caca", "matkul": "Pemrograman Web", "nilai": 85},
        {"nama": "Dedi", "matkul": "Sistem Operasi", "nilai": 75},
        {"nama": "Eka", "matkul": "Algoritma Pemrograman", "nilai": 95},
    ]
    proses_mahasiswa = []
    for mahasiswa in data_mahasiswa:
        proses = multiprocessing.Process(target=cek_nilai_mahasiswa, args=(mahasiswa,))
        proses_mahasiswa.append(proses)

    for proses in proses_mahasiswa:
        proses.start()
        time.sleep(1)

    for proses in proses_mahasiswa:
        proses.join()
