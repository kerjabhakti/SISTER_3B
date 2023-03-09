import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import sleep
from datetime import datetime
import time

# catat waktu mulai
start = time.time()

def kasir_with_barrier(counter, synchronizer, serializer):
    name = multiprocessing.current_process().name
    print(f"{name} siap melayani pelanggan!")
    try:
        synchronizer.wait(timeout=2) # menunggu semua kasir siap
    except multiprocessing.TimeoutError:
        print(f"{name} tidak dapat menunggu semua kasir siap dan keluar dari wait.")
        return
    now = time.time()
    while counter.value > 0: # selama masih ada pelanggan
        with serializer: 
            counter.value -= 1 # mengurangi jumlah pelanggan
            print(f"{name} melayani pelanggan. Pelanggan sekarang: {counter.value}", datetime.fromtimestamp(now))
        sleep(1) # simulasi pelayanan

def kasir_without_barrier(counter):
    name = multiprocessing.current_process().name
    print(f"{name} siap melayani pelanggan!")
    now = time.time()
    while counter.value > 0: # selama masih ada pelanggan
            counter.value -= 1 # mengurangi jumlah pelanggan
            print(f"{name} melayani pelanggan. Pelanggan sekarang: {counter.value}", datetime.fromtimestamp(now))
    sleep(1) # simulasi pelayanan

    
if __name__ == '__main__':
    counter = multiprocessing.Value('i', 5) # jumlah pelanggan
    synchronizer = Barrier(1) # menunggu semua kasir siap
    serializer = Lock() # menghindari race condition

    kasir1 = Process(target=kasir_with_barrier, args=(counter, synchronizer, serializer))
    kasir2 = Process(target=kasir_without_barrier, args=(counter,))
   
    kasir1.start()
    kasir2.start()
   
    kasir1.join()
    kasir2.join()
   
    print("Semua pelanggan telah dilayani!")

    # catat waktu selesai
    end = time.time()

    # hitung selisih waktu
    duration = end - start
    print("Proses selesai dalam waktu %f detik"%duration)

# Hasilnya sebagai berikut :
# Process-1 siap melayani pelanggan!
# Process-1 melayani pelanggan. Pelanggan sekarang: 4 2023-03-09 22:39:42.236334
# Process-2 siap melayani pelanggan!
# Process-2 melayani pelanggan. Pelanggan sekarang: 3 2023-03-09 22:39:42.264257
# Process-2 melayani pelanggan. Pelanggan sekarang: 2 2023-03-09 22:39:42.264257
# Process-2 melayani pelanggan. Pelanggan sekarang: 1 2023-03-09 22:39:42.264257
# Process-2 melayani pelanggan. Pelanggan sekarang: 0 2023-03-09 22:39:42.264257
# Semua pelanggan telah dilayani!
# Proses selesai dalam waktu 3.453815 detik