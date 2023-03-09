# Studi kasus: Sistem Kasir Sederhana

# Sistem kasir sederhana yang melayani 
# pembelian barang dengan harga tertentu. 
# Terdapat dua jenis pengguna, yaitu pembeli dan kasir. 
# Pembeli akan memilih barang yang ingin dibeli dan 
# memberikan uang sesuai dengan total harga. 
# Kasir akan menerima uang dari pembeli dan 
# memberikan kembalian jika uang yang diberikan 
# lebih besar dari total harga. Sistem kasir ini menggunakan 
# satu thread untuk pembeli dan satu thread untuk kasir.

import logging
import threading
import time
import keyboard

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):

        with condition:

            if len(items) == 0:
                logging.info('no items to consume')
                condition.wait()

            items.pop()
            logging.info('consumed 1 item')

            condition.notify()

    def run(self):
        while True:
            time.sleep(2)
            self.consume()
            if keyboard.is_pressed('esc'):
                logging.info('Stopping Consumer')
                break


class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):

        with condition:

            if len(items) == 10:
                logging.info('items produced {}. Stopped'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('total items {}'.format(len(items)))

            condition.notify()

    def run(self):
        while True:
            time.sleep(0.5)
            self.produce()
            if keyboard.is_pressed('esc'):
                logging.info('Stopping Producer')
                break


def main():
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')

    producer.start()
    consumer.start()

    while True:
        if keyboard.is_pressed('esc'):
            logging.info('Stopping Program')
            break
        time.sleep(0.1)

    producer.join()
    consumer.join()


if __name__ == "__main__":
    main()

# 2023-03-02 23:22:33,498 Producer          INFO     total items 1
# 2023-03-02 23:22:34,292 Producer          INFO     total items 2
# 2023-03-02 23:22:34,807 Producer          INFO     total items 3
# 2023-03-02 23:22:35,008 Consumer          INFO     consumed 1 item
# 2023-03-02 23:22:35,317 Producer          INFO     total items 3
# 2023-03-02 23:22:35,826 Producer          INFO     total items 4
# 2023-03-02 23:22:36,338 Producer          INFO     total items 5
# 2023-03-02 23:22:36,855 Producer          INFO     total items 6
# 2023-03-02 23:22:37,023 Consumer          INFO     consumed 1 item
# 2023-03-02 23:22:37,373 Producer          INFO     total items 6
# 2023-03-02 23:22:37,894 Producer          INFO     total items 7
# 2023-03-02 23:22:38,402 Producer          INFO     total items 8
# 2023-03-02 23:22:38,913 Producer          INFO     total items 9
# 2023-03-02 23:22:39,037 Consumer          INFO     consumed 1 item
# 2023-03-02 23:22:39,427 Producer          INFO     total items 9
# 2023-03-02 23:22:39,943 Producer          INFO     total items 10
# 2023-03-02 23:22:40,454 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:22:41,044 Consumer          INFO     consumed 1 item
# 2023-03-02 23:22:41,046 Producer          INFO     total items 10
# 2023-03-02 23:22:41,556 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:22:43,047 Consumer          INFO     consumed 1 item
# 2023-03-02 23:22:43,049 Producer          INFO     total items 10
# 2023-03-02 23:22:43,564 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:22:45,054 Consumer          INFO     consumed 1 item
# 2023-03-02 23:22:45,056 Producer          INFO     total items 10
# 2023-03-02 23:22:45,566 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:22:47,062 Consumer          INFO     consumed 1 item
# 2023-03-02 23:22:47,063 Producer          INFO     total items 10
# 2023-03-02 23:22:47,575 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:22:49,078 Consumer          INFO     consumed 1 item
# 2023-03-02 23:22:49,080 Producer          INFO     total items 10
# 2023-03-02 23:22:49,591 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:22:51,083 Consumer          INFO     consumed 1 item
# 2023-03-02 23:22:51,085 Producer          INFO     total items 10
# 2023-03-02 23:22:51,596 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:22:53,087 Consumer          INFO     consumed 1 item
# 2023-03-02 23:22:53,092 Producer          INFO     total items 10
# 2023-03-02 23:22:53,601 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:22:55,107 Consumer          INFO     consumed 1 item
# 2023-03-02 23:22:55,110 Producer          INFO     total items 10
# 2023-03-02 23:22:55,618 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:22:57,122 Consumer          INFO     consumed 1 item
# 2023-03-02 23:22:57,125 Producer          INFO     total items 10
# 2023-03-02 23:22:57,631 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:22:59,125 Consumer          INFO     consumed 1 item
# 2023-03-02 23:22:59,127 Producer          INFO     total items 10
# 2023-03-02 23:22:59,636 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:23:01,130 Consumer          INFO     consumed 1 item
# 2023-03-02 23:23:01,132 Producer          INFO     total items 10
# 2023-03-02 23:23:01,642 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:23:03,147 Consumer          INFO     consumed 1 item
# 2023-03-02 23:23:03,149 Producer          INFO     total items 10
# 2023-03-02 23:23:03,657 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:23:05,164 Consumer          INFO     consumed 1 item
# 2023-03-02 23:23:05,166 Producer          INFO     total items 10
# 2023-03-02 23:23:05,676 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:23:07,179 Consumer          INFO     consumed 1 item
# 2023-03-02 23:23:07,181 Producer          INFO     total items 10
# 2023-03-02 23:23:07,257 MainThread        INFO     Stopping Program
# 2023-03-02 23:23:07,691 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:23:09,187 Consumer          INFO     consumed 1 item
# 2023-03-02 23:23:09,189 Producer          INFO     total items 10
# 2023-03-02 23:23:09,700 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:23:11,192 Consumer          INFO     consumed 1 item
# 2023-03-02 23:23:11,194 Producer          INFO     total items 10
# 2023-03-02 23:23:11,703 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:23:13,196 Consumer          INFO     consumed 1 item
# 2023-03-02 23:23:13,197 Producer          INFO     total items 10
# 2023-03-02 23:23:13,706 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:23:15,212 Consumer          INFO     consumed 1 item
# 2023-03-02 23:23:15,214 Producer          INFO     total items 10
# 2023-03-02 23:23:15,725 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:23:17,218 Consumer          INFO     consumed 1 item
# 2023-03-02 23:23:17,225 Producer          INFO     total items 10
# 2023-03-02 23:23:17,728 Producer          INFO     items produced 10. Stopped
# 2023-03-02 23:23:19,234 Consumer          INFO     consumed 1 item
# 2023-03-02 23:23:19,236 Consumer          INFO     Stopping Consumer
# 2023-03-02 23:23:19,237 Producer          INFO     total items 10
# 2023-03-02 23:23:19,243 Producer          INFO     Stopping Producer