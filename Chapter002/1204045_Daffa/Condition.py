import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

quranAyat = []
condition = threading.Condition()

class Reader(threading.Thread):
    def __init__(self, name, dailyTarget, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.dailyTarget = dailyTarget

    def readAyat(self):
        with condition:
            if len(quranAyat) == 0:
                logging.info('no ayats have been read')
                condition.wait()
            quranAyat.pop()
            self.dailyTarget += 1
            logging.info('%s have read Quran, ayat read today added %d', self.name, self.dailyTarget)
            condition.notify()

    def run(self):
        for i in range(5):
            time.sleep(4)
            self.dailyTarget -= 1
            logging.info('%s have read Quran, the daily target is reduced %d', self.name, self.dailyTarget)
            if self.dailyTarget <= 5:
                self.readAyat()

class DailyTarget(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def createDailyTarget(self):
        with condition:
            if len(quranAyat) == 10:
                logging.info('Daily reading Quran target has been set')
                condition.wait()
            quranAyat.append(1)
            logging.info('Created 1 target for today, total %d', len(quranAyat))
            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(0.1)
            self.createDailyTarget()

def main():
    sReader = [Reader(name=name, dailyTarget=10) for name in ['John', 'Doe', 'Alexa', 'Sooho', 'Lee', 'Han', 'Mehmed']]
    dTarget = DailyTarget(name='Target Creator')

    for reader in sReader:
        reader.start()

    
    dTarget.start()

    for reader in sReader:
        reader.join()

    dTarget.join()

if __name__ == "__main__":
    main()