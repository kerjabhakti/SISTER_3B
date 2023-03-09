import multiprocessing
import time

def kasir(q):
    total_harga = 0
    while True:
        item = q.get()
        if item is None:
            break
        harga = item * 1000
        total_harga += harga
        print(f'Kasir memproses item {item} dengan harga {harga}')
    q.put(total_harga)

if __name__ == '__main__':
    q = multiprocessing.Queue()

    process_kasir = multiprocessing.Process(target=kasir, args=(q,))
    process_kasir.start()

    total_belanja = 0
    for item in [3, 4, 1, 5]:
        q.put(item)

    q.put(None)
    total_harga = q.get()
    print(f"Total belanja pelanggan adalah {total_harga}")

    process_kasir.join()


#Hasilnya sebagai berikut :
# Total belanja pelanggan adalah 3
# Kasir memproses item 4 dengan harga 4000
# Kasir memproses item 1 dengan harga 1000
# Kasir memproses item 5 dengan harga 5000
