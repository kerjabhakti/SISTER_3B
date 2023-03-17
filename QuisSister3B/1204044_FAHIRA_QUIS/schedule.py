# Studi kasus penggunaan script ini untuk mengatur jadwal kuliah. 
# Misalnya, ada 4 kelas yang akan diadakan pada hari Senin dan Rabu dengan durasi 2 jam setiap kelasnya.
# Kita ingin menentukan jadwal waktu yang tepat untuk mengadakan kelas-kelas ini.

import threading
import queue
import time

class Kelas:
    def __init__(self, nama, hari, jam_mulai):
        self.nama = nama
        self.hari = hari
        self.jam_mulai = jam_mulai
    
    def jadwal(self):
        print(f"{self.nama} akan diadakan pada hari {self.hari} mulai pukul {self.jam_mulai} \n")
        time.sleep(2)

# membuat objek Kelas
kelas1 = Kelas("Kelas 1", "Senin", "08:00")
kelas2 = Kelas("Kelas 2", "Senin", "10:00")
kelas3 = Kelas("Kelas 3", "Rabu", "08:00")
kelas4 = Kelas("Kelas 4", "Rabu", "10:00")

# definisi fungsi untuk menjalankan thread
def worker(q, stop_event):
    while not stop_event.is_set():
        try:
            kelas = q.get(timeout=1)
            kelas.jadwal()
            q.task_done()
        except queue.Empty:
            pass


# menjalankan proses utama dengan menggunakan thread dan queue
if __name__ == '__main__':
    print("Proses pengeksekusian beberapa kelas dalam 1 waktu dimulai...\n")
    q = queue.Queue()
    num_threads = 4
    threads = []
    stop_event = threading.Event()
    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(q, stop_event))
        t.start()
        threads.append(t)
    for kelas in [kelas1, kelas2, kelas3, kelas4]:
        q.put(kelas)
    q.join()
    stop_event.set()
    for t in threads:
        t.join()
    print("\nProses pengeksekusian beberapa kelas dalam 1 waktu selesai.")

