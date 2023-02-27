import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

heal_potions = []
condition = threading.Condition()

class Player(threading.Thread):
    def __init__(self, name, health, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.health = health

    def use_heal_potion(self):
        with condition:
            if len(heal_potions) == 0:
                logging.info('Tidak ada heal potion yang tersedia')
                condition.wait()
            heal_potions.pop()
            self.health += 50
            logging.info('%s menggunakan heal potion dan kesehatannya bertambah menjadi %d', self.name, self.health)
            condition.notify()

    def run(self):
        for i in range(5):
            time.sleep(2)
            self.health -= 30
            logging.info('%s terkena serangan dan kesehatannya berkurang menjadi %d', self.name, self.health)
            if self.health <= 50:
                self.use_heal_potion()

class Healer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_heal_potion(self):
        with condition:
            if len(heal_potions) == 10:
                logging.info('Tidak dapat membuat lebih banyak heal potion')
                condition.wait()
            heal_potions.append(1)
            logging.info('Membuat 1 heal potion, total %d', len(heal_potions))
            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(1)
            self.create_heal_potion()

def main():
    player1 = Player(name='Pemain 1', health=100)
    player2 = Player(name='Pemain 2', health=100)
    healer = Healer(name='Penyembuh')

    player1.start()
    player2.start()
    healer.start()

    player1.join()
    player2.join()
    healer.join()

if __name__ == "__main__":
    main()