import threading
import time
import queue

# Inisialisasi RLock
rlock = threading.RLock()

# Inisialisasi antrian pesanan
order_queue = queue.Queue()

# Inisialisasi Semaphore
# Hanya 3 pesanan yang dapat diproses secara bersamaan
semaphore = threading.Semaphore(3)

# Fungsi untuk mendapatkan pesanan dari pelanggan
def get_order():
    while True:
        with rlock:
            # Menunggu pesanan masuk ke antrian
            if not order_queue.empty():
                order = order_queue.get()
                print("Mendapatkan pesanan:", order)
                # Proses pesanan
                process_order(order)
        time.sleep(1)

# Fungsi untuk memproses pesanan
def process_order(order):
    print("Memproses pesanan:", order)
    with semaphore:
        # Simulasi waktu pengiriman
        time.sleep(2)
        print("Pesanan", order, "selesai diproses.")

# Fungsi untuk mengirim pesanan ke gudang
def send_order(order):
    with rlock:
        print("Mengirim pesanan:", order)
        order_queue.put(order)

# Membuat beberapa thread untuk mendapatkan pesanan
get_order_thread1 = threading.Thread(target=get_order)
get_order_thread2 = threading.Thread(target=get_order)

# Membuat beberapa thread untuk mengirim pesanan
send_order_thread1 = threading.Thread(target=send_order, args=("Order 1",))
send_order_thread2 = threading.Thread(target=send_order, args=("Order 2",))
send_order_thread3 = threading.Thread(target=send_order, args=("Order 3",))

# Memulai thread-thread yang ada
get_order_thread1.start()
get_order_thread2.start()
send_order_thread1.start()
send_order_thread2.start()
send_order_thread3.start()

# Menunggu thread-thread yang ada selesai
get_order_thread1.join()
get_order_thread2.join()
send_order_thread1.join()
send_order_thread2.join()
send_order_thread3.join()
