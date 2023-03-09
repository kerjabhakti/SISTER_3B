# kelas Consumer berperan sebagai kasir, dan memiliki fungsi process_transaction() 
# untuk memasukkan transaksi ke dalam items dan mengeset event. 
# Kelas Producer akan menghasilkan transaksi secara acak 
# setiap 2 detik dan memanggil fungsi process_transaction() 
# dari objek consumer untuk memasukkan transaksi tersebut ke dalam items.

# Kelas Consumer akan terus memproses transaksi dari items setelah 
# event di-set oleh kelas Producer. Selain itu, 
# kelas Consumer juga akan mem-clear event setelah 
# memproses transaksi sehingga Producer dapat memasukkan 
# transaksi baru ke items di waktu berikutnya.

import logging
import threading
import time
import random
import keyboard

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
event = threading.Event()


class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            time.sleep(2)
            event.wait()
            item = items.pop()
            logging.info('Consumer notify: {} popped by {}'\
                         .format(item, self.name))

            if len(items) == 0:
                event.clear()

class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            time.sleep(2)
            item = random.randint(0, 100)
            items.append(item)
            logging.info('Producer notify: item {} appended by {}'\
                         .format(item, self.name))
            event.set()


if __name__ == "__main__":
    t1 = Producer()
    t2 = Consumer()

    t1.start()
    t2.start()

    while True:
        if keyboard.is_pressed('esc'):
            break

    t1.join()
    t2.join()

# 2023-03-02 23:38:47,040 Thread-6          INFO     Producer notify: item 57 appended by Thread-6
# 2023-03-02 23:38:47,057 Thread-7          INFO     Consumer notify: 57 popped by Thread-7
# 2023-03-02 23:38:49,084 Thread-6          INFO     Producer notify: item 25 appended by Thread-6
# 2023-03-02 23:38:49,129 Thread-7          INFO     Consumer notify: 25 popped by Thread-7
# 2023-03-02 23:38:51,126 Thread-6          INFO     Producer notify: item 71 appended by Thread-6
# 2023-03-02 23:38:51,189 Thread-7          INFO     Consumer notify: 71 popped by Thread-7
# 2023-03-02 23:38:53,146 Thread-6          INFO     Producer notify: item 34 appended by Thread-6
# 2023-03-02 23:38:53,239 Thread-7          INFO     Consumer notify: 34 popped by Thread-7
# 2023-03-02 23:38:55,189 Thread-6          INFO     Producer notify: item 93 appended by Thread-6
# 2023-03-02 23:38:55,282 Thread-7          INFO     Consumer notify: 93 popped by Thread-7
# 2023-03-02 23:38:57,233 Thread-6          INFO     Producer notify: item 74 appended by Thread-6
# 2023-03-02 23:38:57,342 Thread-7          INFO     Consumer notify: 74 popped by Thread-7
# 2023-03-02 23:38:59,272 Thread-6          INFO     Producer notify: item 72 appended by Thread-6
# 2023-03-02 23:38:59,366 Thread-7          INFO     Consumer notify: 72 popped by Thread-7
# 2023-03-02 23:39:01,291 Thread-6          INFO     Producer notify: item 60 appended by Thread-6
# 2023-03-02 23:39:01,400 Thread-7          INFO     Consumer notify: 60 popped by Thread-7
# 2023-03-02 23:39:03,323 Thread-6          INFO     Producer notify: item 34 appended by Thread-6
# 2023-03-02 23:39:03,478 Thread-7          INFO     Consumer notify: 34 popped by Thread-7
# 2023-03-02 23:39:05,384 Thread-6          INFO     Producer notify: item 81 appended by Thread-6
# 2023-03-02 23:39:05,510 Thread-7          INFO     Consumer notify: 81 popped by Thread-7
# 2023-03-02 23:39:07,421 Thread-6          INFO     Producer notify: item 85 appended by Thread-6
# 2023-03-02 23:39:07,546 Thread-7          INFO     Consumer notify: 85 popped by Thread-7
# 2023-03-02 23:39:09,460 Thread-6          INFO     Producer notify: item 49 appended by Thread-6
# 2023-03-02 23:39:09,588 Thread-7          INFO     Consumer notify: 49 popped by Thread-7