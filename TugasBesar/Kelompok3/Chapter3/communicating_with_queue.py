import multiprocessing

# Fungsi untuk proses pencatatan penjualan
def record_sales(queue):
    while True:
        sale = queue.get()  # Mendapatkan data penjualan dari antrian
        if sale == 'done':
            break
        # Proses pencatatan penjualan
        print("Mencatat penjualan:", sale)

# Fungsi untuk proses pembaruan inventaris
def update_inventory(queue):
    while True:
        item = queue.get()  # Mendapatkan data pembaruan inventaris dari antrian
        if item == 'done':
            break
        # Proses pembaruan inventaris
        print("Memperbarui inventaris:", item)

if __name__ == '__main__':
    # Membuat antrian (queue) untuk komunikasi antara proses
    queue = multiprocessing.Queue()

    # Membuat dan memulai proses pencatatan penjualan
    sales_process = multiprocessing.Process(target=record_sales, args=(queue,))
    sales_process.start()

    # Membuat dan memulai proses pembaruan inventaris
    inventory_process = multiprocessing.Process(target=update_inventory, args=(queue,))
    inventory_process.start()

    # Menyimulasikan penjualan dan pembaruan inventaris
    sales = ['Produk A', 'Produk B', 'Produk C', 'done']
    for sale in sales:
        queue.put(sale)  # Memasukkan data penjualan ke antrian

    inventory_updates = ['Produk A', 'Produk C', 'Produk B', 'done']
    for item in inventory_updates:
        queue.put(item)  # Memasukkan data pembaruan inventaris ke antrian

    # Memberikan sinyal selesai ke proses pencatatan penjualan dan pembaruan inventaris
    queue.put('done')
    queue.put('done')

    # Menunggu proses selesai
    sales_process.join()
    inventory_process.join()

    # Hasilnya :
    # Memperbarui inventaris: Produk A
    # Memperbarui inventaris: Produk B
    # Memperbarui inventaris: Produk C
    # Mencatat penjualan: Produk A
    # Mencatat penjualan: Produk C
    # Mencatat penjualan: Produk B