import threading
import time
import random


class Pembelian_mobil:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)

def transaksi(pembelian_mobil, tersedia):
    print("Transaksi {} mobil \n".format(tersedia))
    while tersedia:
        pembelian_mobil.add()
        time.sleep(1)
        tersedia -= 1
        print("Transaksi satu Mobil --> {} Transaksi Sukses \n".format(tersedia))


def pelayanan(pembelian_mobil, tersedia):
    print("Melayani {} Pelanggan \n".format(tersedia))
    while tersedia:
        pembelian_mobil.remove()
        time.sleep(1)
        tersedia -= 1
        print("Melayani satu pelangan --> {} Pelayanan Sukses \n".format(tersedia))


def main():
    tersedia = random.randint(10, 20)
    pembelian_mobil = Pembelian_mobil()

    t1 = threading.Thread(target=transaksi, \
                          args=(pembelian_mobil, tersedia))
    t2 = threading.Thread(target=pelayanan, \
                          args=(pembelian_mobil, random.randint(1, tersedia)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    
    print('Transaksi dan Pelayanan Auto Luxury Selesai.')

if __name__ == "__main__":
    main()