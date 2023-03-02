import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

semaphore = threading.Semaphore(0)
seats = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def customer(name):
    global seats
    logging.info('%s sedang menunggu tiket', name)
    if not seats:
        logging.info('Maaf %s, tiket sudah habis')
    else:
        semaphore.acquire()
        seat = random.choice(seats)
        seats.remove(seat)
        logging.info('%s memesan tiket untuk kursi nomor %s', name, seat)
        semaphore.release()


def ticket_seller():
    global seats
    time.sleep(3)
    if seats:
        logging.info('Notifikasi pemesanan masuk ke Penjual Tiket')
        semaphore.release()
    else:
        logging.info('Maaf, tiket sudah habis')


def main():
    customers = ["Balmond", "Unang", "Dandi", "Saep", "Angela"]

    threads = []
    for name in customers:
        t = threading.Thread(target=customer, args=(name,))
        threads.append(t)

    t = threading.Thread(target=ticket_seller)
    threads.append(t)

    random.shuffle(threads)

    for t in threads:
        t.start()
        time.sleep(0.1)

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()