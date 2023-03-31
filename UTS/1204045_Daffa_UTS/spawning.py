# Program untuk memproses daftar pesanan makanan secara paralel menggunakan multiprocessing

import multiprocessing

# fungsi untuk memproses daftar pesanan makanan
def process_order(order):
    print(f"Memproses pesanan {order} di dalam proses {multiprocessing.current_process().name}")
    # lakukan pengolahan pesanan, misalnya memasak makanan atau mengirimkan pesanan
    print(f"Pesanan {order} telah selesai diproses")

if __name__ == '__main__':
    # daftar pesanan makanan
    orders = ['nasi goreng', 'ayam goreng', 'mie goreng', 'sate', 'rendang']

    # buat proses untuk memproses daftar pesanan
    processes = []
    for order in orders:
        process = multiprocessing.Process(target=process_order, args=(order,))
        process.start()
        processes.append(process)

    # tunggu semua proses selesai
    for process in processes:
        process.join()

    print("Semua pesanan telah diproses")

