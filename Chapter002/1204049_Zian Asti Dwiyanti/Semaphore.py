import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
item = 0


def supplier():
    logging.info('Supplier adds stock')
    semaphore.acquire()
    logging.info('Supplier notify: number of items {}'.format(item))


def customer():
    global item
    time.sleep(3)
    item = random.randint(0, 1000)
    logging.info('Customer buy items.')
    semaphore.release()


def main():
    for i in range(10):
        t1 = threading.Thread(target=supplier)
        t2 = threading.Thread(target=customer)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()