import threading
import time
import random


class Deposit:
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

def transaction(deposit, available):
    print("Transaksi {} deposit tersimpan \n".format(available))
    while available:
        deposit.add()
        time.sleep(1)
        available -= 1
        print("Transaksi satu antrian --> {} Transaksi Sukses \n".format(available))


def service(deposit, available):
    print("Pelayanan {} Nasabah \n".format(available))
    while available:
        deposit.remove()
        time.sleep(1)
        available -= 1
        print("Melayani satu nasabah --> {} Pelayanan Sukses \n".format(available))


def main():
    available = random.randint(10, 15)
    deposit = Deposit()

    t1 = threading.Thread(target=transaction, \
                          args=(deposit, available))
    t2 = threading.Thread(target=service, \
                          args=(deposit, random.randint(1, available)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    
    print('Proses deposit dan layanan terkait telah selesai dilakukan ! ')

if __name__ == "__main__":
    main()