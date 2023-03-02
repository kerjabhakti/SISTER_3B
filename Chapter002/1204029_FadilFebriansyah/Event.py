import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

orders = []
event = threading.Event()


class Processor(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_order(self):
        while True:
            time.sleep(10)
            event.wait()
            order = orders.pop()
            logging.info('Processor notify: {} processed by {}'\
                         .format(order, self.name))

    def run(self):
        self.process_order()


class Customer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def place_order(self):
        for i in range(5):
            time.sleep(10)
            order = random.choice(['nasi goreng', 'mie ayam', 'sate', 'ayam goreng'])
            orders.append(order)
            logging.info('Customer notify: order {} placed by {}'\
                         .format(order, self.name))
            event.set()
            event.clear()

    def run(self):
        self.place_order()


if __name__ == "__main__":
    t1 = Processor()
    t2 = Customer()

    t1.start()
    t2.start()

    t1.join()
    t2.join()