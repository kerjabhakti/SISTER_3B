import multiprocessing
import time

def process_order(order):
    print(f"Memproses pesanan {order} di dalam proses {multiprocessing.current_process().name} pada waktu {time.ctime()}")
    time.sleep(1)
    print(f"Pesanan {order} telah selesai diproses pada waktu {time.ctime()}")

if __name__ == '__main__':
    orders = ['nasi goreng', 'ayam goreng', 'mie goreng', 'sate', 'rendang']

    processes = []
    for order in orders:
        process = multiprocessing.Process(target=process_order, args=(order,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    print("Semua pesanan telah diproses pada waktu", time.ctime())
