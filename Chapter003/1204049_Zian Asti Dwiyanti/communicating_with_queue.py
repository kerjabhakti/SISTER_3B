import multiprocessing
import random
import time

class Supplier(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item) 
            print ("Supplier %s : item %d ditambahkan ke dalam antrian"\
                   % (self.name, item))
            time.sleep(1)
            print ("Ukuran antrian sekarang adalah %s"\
                   % self.queue.qsize())

class Customer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):
                print("Antrian kosong")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print('Customer %s : item %d diambil dari antrian\n' % (self.name, item))
                time.sleep(1)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    supplier = Supplier(queue)
    customer1 = Customer(queue)
    customer2 = Customer(queue)

    supplier.start()
    customer1.start()
    customer2.start()

    supplier.join()
    customer1.join()
    customer2.join()
