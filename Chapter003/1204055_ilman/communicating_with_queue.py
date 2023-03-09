import multiprocessing
import random
import time

class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        movies = ["Avengers: Endgame", "Joker", "Frozen 2", "Parasite", "Toy Story 4"]
        for i in range(5):
            movie = random.choice(movies)
            self.queue.put(movie)
            print(f"Process Producer: Film '{movie}' ditambahkan ke antrian film oleh {self.name}")
            time.sleep(1)
            print(f"The size of the queue is {self.queue.qsize()}")

class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("The queue is empty")
                break
            else:
                time.sleep(2)
                movie = self.queue.get()
                print(f"Process Consumer: Movie '{movie}' di play oleh {self.name}\n")
                time.sleep(1)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
