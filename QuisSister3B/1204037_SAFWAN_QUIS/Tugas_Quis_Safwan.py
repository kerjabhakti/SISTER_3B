import threading
import datetime
import time

# Inisiasi barrier dengan jumlah thread yang akan dijalankan
barrier = threading.Barrier(3)

# Inisiasi objek threading dengan fungsi yang akan dijalankan pada setiap thread

print("\nSidang Tugas Akhir Mahasiswa\n")


def mhs1():
    start_time = datetime.datetime.now()
    print("Mahasiswa 1 memulai sidang TA pada", start_time)
    # lakukan sesuatu pada mhs 1
    time.sleep(15)  # jalankan tugas selama 15 detik
    end_time = datetime.datetime.now()
    print("Mahasiswa 1 Telah Selesai Sidang TA pada", end_time,
          "Waktu Sidangnya Adalah:", end_time - start_time)
    # tampilkan pesan pada saat mhs 1 selesai
    barrier.wait()


def mhs2():
    start_time = datetime.datetime.now()
    print("Mahasiswa 2 memulai sidang TA pada", start_time)
    # lakukan sesuatu pada mhs 2
    time.sleep(15)  # jalankan tugas selama 15 detik
    end_time = datetime.datetime.now()
    print("Mahasiswa 2 Telah Selesai Sidang TA pada", end_time,
          "Waktu Sidangnya Adalah:", end_time - start_time)
   # tampilkan pesan pada saat mhs 2 selesai
    barrier.wait()


def mhs3():
    start_time = datetime.datetime.now()
    print("Mahasiswa 3 memulai sidang TA pada", start_time)
    # lakukan sesuatu pada mhs 3
    time.sleep(15)  # jalankan tugas selama 15 detik
    end_time = datetime.datetime.now()
    print("Mahasiswa 3 Telah Selesai Sidang TA pada", end_time,
          "Waktu Sidangnya Adalah:", end_time - start_time)
   # tampilkan pesan pada saat mhs 3 selesai
    barrier.wait()


# inisiasi thread dengan fungsi yang telah dibuat
t1 = threading.Thread(target=mhs1)
t2 = threading.Thread(target=mhs2)
t3 = threading.Thread(target=mhs3)

# jalankan thread
t1.start()
t2.start()
t3.start()

# tunggu thread selesai
t1.join()
t2.join()
t3.join()


# tampilkan pesan ketika semua thread selesai
print("\nAntrian Sidang Mahasiswa Telah Selesai")
