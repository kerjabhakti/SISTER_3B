import threading
import time
import queue

# Fungsi untuk mendapatkan pesanan dari pelanggan
def get_order(order_queue):
    while True:
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
    # Simulasi waktu pengiriman
    time.sleep(2)
    print("Pesanan", order, "selesai diproses.")

# Fungsi untuk mengirim pesanan ke gudang
def send_order(order_queue, order):
    print("Mengirim pesanan:", order)
    order_queue.put(order)

# Fungsi untuk membaca data penjualan dari file
def read_sales_data(filename):
    with open(filename, 'r') as file:
        sales_data = file.readlines()
    return [data.strip() for data in sales_data]

# Fungsi untuk menulis data penjualan ke file
def write_sales_data(filename, sales_data):
    with open(filename, 'w') as file:
        file.write('\n'.join(sales_data))

# Fungsi untuk membaca data inventaris dari file
def read_inventory_data(filename):
    with open(filename, 'r') as file:
        inventory_data = file.readlines()
    return [data.strip() for data in inventory_data]

# Fungsi untuk menulis data inventaris ke file
def write_inventory_data(filename, inventory_data):
    with open(filename, 'w') as file:
        file.write('\n'.join(inventory_data))

# Inisialisasi antrian pesanan
order_queue = queue.Queue()

# Membuat thread untuk mendapatkan pesanan
get_order_thread = threading.Thread(target=get_order, args=(order_queue,))
get_order_thread.start()

# Membuat beberapa thread untuk mengirim pesanan
send_order_thread1 = threading.Thread(
    target=send_order, args=(order_queue, "Order 1"))
send_order_thread2 = threading.Thread(
    target=send_order, args=(order_queue, "Order 2"))
send_order_thread3 = threading.Thread(
    target=send_order, args=(order_queue, "Order 3"))

# Memulai thread pengiriman pesanan
send_order_thread1.start()
send_order_thread2.start()
send_order_thread3.start()

# Menunggu thread pengiriman pesanan selesai
send_order_thread1.join()
send_order_thread2.join()
send_order_thread3.join()

# Menunggu thread mendapatkan pesanan selesai
get_order_thread.join()

# Membaca data penjualan dari file
sales_data = read_sales_data("sales_data.txt")
print("Data Penjualan:", sales_data)

# Menulis data penjualan ke file
new_sales_data = sales_data + ["New Sale"]
write_sales_data("sales_data.txt", new_sales_data)
print("Data Penjualan baru ditulis ke file.")

# Membaca data inventaris dari file
inventory_data = read_inventory_data("inventory_data.txt")
print("Data Inventaris:", inventory_data)

# Menulis data inventaris ke file
new_inventory_data = inventory_data + ["New Item"]
write_inventory_data("inventory_data.txt", new_inventory_data)
print("Data Inventaris baru ditulis ke file.")
