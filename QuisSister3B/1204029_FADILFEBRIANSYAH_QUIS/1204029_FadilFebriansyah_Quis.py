import threading
import time

# Membuat objek Barrier dengan jumlah thread yang akan dijalankan
barrier = threading.Barrier(4)

class Presensi:
    def __init__(self):
        self.absen = []

    def tambah(self, nama):
        self.absen.append(nama)
        print(f"{nama} sudah melakukan absensi ya gaes")

    def lihat(self):
        print("Daftar hadir kelas SISTER:")
        for nama in self.absen:
            print(f"- {nama}")

presensi = Presensi()

class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm

    def presensi(self):
        presensi.tambah(self.nama)
        print(f"{self.nama} dengan {self.npm} sudah melakukan presensi pada jam {time.ctime(time.time())}")
        # Thread menunggu di barrier
        barrier.wait()
        print(f"{self.nama} dengan {self.npm} sudah menyelesaikan presensinya\n")

# Data mahasiswa
mhs1 = Mahasiswa("Ilman", "1204055")
mhs2 = Mahasiswa("Nawaf", "1204036")
mhs3 = Mahasiswa("Daffa", "1204045")
mhs4 = Mahasiswa("Fadil", "1204029")

if __name__ == '__main__':
    # catat waktu mulai
    start_time = time.time()

    # membuat thread baru untuk setiap mahasiswa
    t1 = threading.Thread(target=mhs1.presensi)
    t2 = threading.Thread(target=mhs2.presensi)
    t3 = threading.Thread(target=mhs3.presensi)
    t4 = threading.Thread(target=mhs4.presensi)

    # menjalankan thread
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # menunggu thread selesai
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    # catat waktu selesai
    end_time = time.time()

    # menampilkan daftar hadir setelah semua mahasiswa melakukan presensi
    presensi.lihat()

    # menampilkan pesan ketika semua mahasiswa selesai presensi
    print("Semua mahasiswa telah menyelesaikan presensinya pada jam: ", time.ctime(time.time()))

    # menampilkan perbandingan waktu berjalan dan berhenti
    print("Perbandingan data berjalan dan berhenti = ", end_time - start_time)
