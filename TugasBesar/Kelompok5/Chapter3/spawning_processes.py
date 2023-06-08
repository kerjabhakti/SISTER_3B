import multiprocessing

def process_order(order):
    print("Memproses pesanan:", order)
    # Lakukan proses pemrosesan pesanan makanan
    # ...

def main():
    orders = ["Burger", "Pizza", "Sushi", "Noodle"]

    processes = []
    for order in orders:
        process = multiprocessing.Process(target=process_order, args=(order,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == '__main__':
    main()
