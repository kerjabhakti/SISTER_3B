import multiprocessing
import random
import time


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        # Bocil adalah nama akun pelanggan
        bocils = ["Zizoy", "Vergil", "StayHalal", "Wangg", "NtisAhoy"]
        for i in range(6):
            bocil = random.choice(bocils)
            self.queue.put(bocil)
            print(
                f"Process Producer: Akun '{bocil}' telah ditambahkan ke dalam antrian Joki oleh {self.name}")
            time.sleep(2)
            print(f"Nomor Antriannya adalah {self.queue.qsize()}")


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("Antrian Joki Selesai")
                break
            else:
                time.sleep(2)
                bocil = self.queue.get()
                print(
                    f"Process Consumer: Akun '{bocil}' telah diJoki oleh {self.name}\n")
                time.sleep(1)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
