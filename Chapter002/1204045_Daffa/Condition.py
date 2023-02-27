import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

ayats = []
condition = threading.Condition()


class Reader(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def read(self):

        with condition:

            while len(ayats) == 0:
                logging.info('no ayats have been read')
                condition.wait()

            ayats.pop()  
            logging.info('have read 1 ayat')

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(4)
            self.read()


class Collector(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def collect(self):

        with condition:

            while len(ayats) == 10:
                logging.info('ayat collected {}. Stopped'.format(len(ayats)))
                condition.wait()

            ayats.append(1)
            logging.info('total ayats {}'.format(len(ayats)))

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(0.2)
            self.collect()


def main():
    collector = Collector(name='Collector')
    readers = [Reader(name=name) for name in ['John', 'Doe', 'Alexa', 'Sooho', 'Lee', 'Han', 'Mehmed']]

    collector.start()

    for reader in readers:
        reader.start()

    collector.join()

    for reader in readers:
        reader.join()

    print('All readers have read Quran today')


if __name__ == "__main__":
    main()
