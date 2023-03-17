import threading
import time

class JadwalKuliah:
    def __init__(self):
        self.mutex = threading.Lock()
        self.jadwal = []

    def tambah_jadwal(self, jadwal):
        self.mutex.acquire()
        self.jadwal.append(jadwal)
        self.mutex.release()

    def lihat_jadwal(self):
        self.mutex.acquire()
        print("Jadwal kuliah Semester 6 Kelas 3B:")
        for jadwal in self.jadwal:
            print(jadwal)
        self.mutex.release()

def buat_jadwal(jadwal_kuliah, barrier):
    print("Perwalian akan segera dimulai....") 
    time.sleep(5) # simulasi pekerjaan yang membutuhkan waktu 5 detik
    jadwal_kuliah.tambah_jadwal("Senin, 09.00-12.00 - Kecerdasan Buatan")
    jadwal_kuliah.tambah_jadwal("Senin, 13.00-16.20 -  Sistem Multimedia")
    jadwal_kuliah.tambah_jadwal("Selasa, 08.40-12.00 - Bahasa Inggris")
    jadwal_kuliah.tambah_jadwal("Selasa, 13.00-16.00 - Data Mining")
    jadwal_kuliah.tambah_jadwal("Kamis, 08.40-12.00 -  Sistem Pakar")
    jadwal_kuliah.tambah_jadwal("Kamis, 13.00-14.40 -  Statistika")
    jadwal_kuliah.tambah_jadwal("Jumat, 08.40-12.00 -  Sistem Tersebar")
    jadwal_kuliah.tambah_jadwal("Sabtu, 09.00-12.00 -  Kapita Selekta")
    print("Kontrak Matakuliah Telah selesai !! ")
    barrier.wait() # tunggu sampai semua thread selesai

def perwalian(jadwal_kuliah, barrier):
    print("Membuat Kontrak Matakuliah!")
    barrier.wait() # tunggu sampai semua thread selesai
    time.sleep(3) # simulasi pekerjaan yang membutuhkan waktu 3 detik
    jadwal_kuliah.lihat_jadwal()
    print("Perwalian telah selesai !! ")

# inisiasi objek jadwal kuliah
jadwal_kuliah = JadwalKuliah()

# inisiasi objek barrier
barrier = threading.Barrier(2) # mengatur barrier untuk 2 thread

# inisiasi objek thread untuk buat_jadwal dan perwalian
t1 = threading.Thread(target=buat_jadwal, args=(jadwal_kuliah, barrier))
t2 = threading.Thread(target=perwalian, args=(jadwal_kuliah, barrier))

# catat waktu mulai
start_time = time.time()

# jalankan thread
t1.start()
t2.start()

# tunggu thread selesai
t1.join()
t2.join()

# catat waktu selesai
end_time = time.time()

# tampilkan waktu eksekusi
print("Waktu mulai:", start_time)
print("Waktu selesai:", end_time)
print("Waktu eksekusi:", end_time - start_time)
