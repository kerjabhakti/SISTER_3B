import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

Match = []
condition = threading.Condition()


class pemain(threading.Thread):
    def __init__(self, nickname, TargetLaga, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = nickname
        self.Target = TargetLaga

    def mainRank(self):
        with condition:
            if len(Match) == 0:
                logging.info('Tidak ada game yang dimainkan')
                condition.wait()
            Match.pop()
            self.Target += 1
            logging.info('%s Telah Main Rank, Game yang dimainkan %d',
                         self.name, self.Target)
            condition.notify()

    def run(self):
        for i in range(5):
            time.sleep(4)
            self.Target -= 1
            logging.info(
                '%s telah main rank, Target harian dikurangi %d', self.name, self.Target)
            if self.Target <= 5:
                self.mainRank()


class TargetHarian(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def createTargetHarian(self):
        with condition:
            if len(Match) == 10:
                logging.info('Target Main Rank')
                condition.wait()
            Match.append(1)
            logging.info('Menyelesaikan 1 target wajib rank hari ini, total %d',
                         len(Match))
            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(0.1)
            self.createTargetHarian()


def main():
    sPemain = [pemain(nickname=name, TargetLaga=20) for name in [
        'Wangg', 'Zizoy', 'NtisAhoy', 'Vergil',
        'StayHalal']]
    gTarget = TargetHarian(name='Target Creator')

    for player in sPemain:
        player.start()

    gTarget.start()

    for player in sPemain:
        player.join()

    gTarget.join()


if __name__ == "__main__":
    main()
