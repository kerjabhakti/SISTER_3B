import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
item = 0


def anak():
    logging.info('Anak sedang menunggu')
    semaphore.acquire()
    logging.info('Anak menaiki kursi wahana nomor {}'.format(item))


def petugas():
    global item
    time.sleep(3)
    item = random.randint(0, 1000)
    logging.info('Petugas mengosongi kursi wahana nomor {}'.format(item))
    semaphore.release()


def main():
    for i in range(10):
        t1 = threading.Thread(target=anak)
        t2 = threading.Thread(target=petugas)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()

# from multiprocessing import Semaphore
# from threading import Thread
# from time import sleep
# import sys

# print = lambda x: sys.stdout.write("%s\n" % x)

# tamanBermain = Semaphore(5)

# def masuk_tamanBermain(urutan):
#     global tamanBermain

#     print(f"Anak {urutan} sedang menunggu giliran")
#     tamanBermain.acquire()

#     print(f"Anak {urutan} sedang bermain")
#     sleep(3)

#     print(f"Anak {urutan} telah meninggalkan taman bermain")
#     tamanBermain.release()

# anak = []

# for i in range(10):
#     anak.append(Thread(target = masuk_tamanBermain, args = (i,)))
#     anak[i].start()

# for i in range(10):
#     anak[i].join()