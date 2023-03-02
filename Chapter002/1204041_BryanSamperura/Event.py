import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

pembelians = []
event = threading.Event()


class Processor(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_pembelian(self):
        while True:
            time.sleep(10)
            event.wait()
            pembelian = pembelians.pop()
            logging.info('Processor notify: {} processed by {}'\
                         .format(pembelian, self.name))

    def run(self):
        self.process_pembelian()


class Customer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def place_pembelian(self):
        for i in range(5):
            time.sleep(10)
            pembelian = random.choice(['Elgy', 'Supra J2Z', 'Silvia S15', 'Lamborgini Urus', 'BMW M4'])
            pembelians.append(pembelian)
            logging.info('Customer notify: pembelian {} placed by {}'\
                         .format(pembelian, self.name))
            event.set()
            event.clear()

    def run(self):
        self.place_pembelian()


if __name__ == "__main__":
    t1 = Processor()
    t2 = Customer()

    t1.start()
    t2.start()

    t1.join()
    t2.join()