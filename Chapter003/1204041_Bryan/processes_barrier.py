import multiprocessing
from multiprocessing import Barrier, Lock, Process, Queue
from time import time
from datetime import datetime


def test_with_barrier(synchronizer, serializer, name, output_queue):
    synchronizer.wait()
    now = time()
    with serializer:
        output_queue.put(f"Process {name} purchased item at {datetime.fromtimestamp(now)}\n")

def test_without_barrier(name, output_queue):
    now = time()
    output_queue.put(f"Process {name} purchased item at {datetime.fromtimestamp(now)}\n")

if __name__ == '__main__':
    synchronizer = Barrier(1)
    serializer = Lock()
    output_queue = Queue()

    # Input nama pembeli
    buyer_names = ["Rhea", "Laura", "Bryan", "Joseph"]

    # Memulai proses pembelian dengan barrier
    p1 = Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, buyer_names[0], output_queue))
    p2 = Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, buyer_names[1], output_queue))
    p3 = Process(name='p3 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, buyer_names[2], output_queue))
    p4 = Process(name='p4 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, buyer_names[3], output_queue))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    
    # Memulai proses pembelian tanpa barrier
    p5 = Process(name='p5 - test_without_barrier', target=test_without_barrier, args=(buyer_names[0], output_queue))
    p6 = Process(name='p6 - test_without_barrier', target=test_without_barrier, args=(buyer_names[1], output_queue))
    p7 = Process(name='p7 - test_without_barrier', target=test_without_barrier, args=(buyer_names[2], output_queue))
    p8 = Process(name='p8 - test_without_barrier', target=test_without_barrier, args=(buyer_names[3], output_queue))
    p5.start()
    p6.start()
    p7.start()
    p8.start()

    # Menunggu semua proses selesai
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()

    # Mengambil output dari semua proses
    output = ""
    while not output_queue.empty():
        output += output_queue.get()

    # Menampilkan output
    print(output)
