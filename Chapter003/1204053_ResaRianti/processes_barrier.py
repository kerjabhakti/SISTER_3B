import multiprocessing
from multiprocessing import Barrier, Lock, Process
import time
import random

# fungsi untuk pelayanan
def Service(transaksi, barrier, lock):
    # mendapatkan nama proses
    name = multiprocessing.current_process().name

    # proses sinkronisasi menggunakan Barrier
    print(f"{name} menunggu no antrian")
    barrier.wait()
    
    with lock:
        print(f"{name} mulai melakukan {transaksi}...")
        time.sleep(random.randint(1, 7))

    print(f"{name} selesai transaksi {transaksi}.")

if __name__ == '__main__':
    # membuat Barrier dan Lock
    barrier = Barrier(4)
    lock = Lock()

    # membuat proses untuk membaca transaksi
    for i in range(1, 5):
        Process(name=f"Proses {i}", target=Service, args=(i, barrier, lock)).start()
