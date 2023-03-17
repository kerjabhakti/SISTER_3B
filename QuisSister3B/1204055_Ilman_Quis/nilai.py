import threading
import queue
import time

def nilai_mahasiswa(mahasiswa, nilai):
    print("Proses penilaian mahasiswa", mahasiswa, "dimulai")
    time.sleep(2)
    print("Mahasiswa", mahasiswa, "telah dinilai dengan nilai", nilai, "\n")

def jalankan_thread(queue, lock):
    while not queue.empty():
        mahasiswa, nilai = queue.get()
        with lock:
            nilai_mahasiswa(mahasiswa, nilai)
        queue.task_done()

q = queue.Queue()
lock = threading.Lock()

q.put(('Saep', 90))
q.put(('Balmond', 85))
q.put(('Warudani', 92))
q.put(('Ica', 87))
q.put(('Surya', 95))

print("Proses penilaian mahasiswa dimulai\n")
threads = []
for i in range(3):
    t = threading.Thread(target=jalankan_thread, args=(q, lock))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Proses penilaian selesai pada waktu", time.strftime('%Y-%m-%d %H:%M:%S'))
