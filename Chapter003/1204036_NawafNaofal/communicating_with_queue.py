import multiprocessing
import time

class PotionProducer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(10):
            item = "Potion Penyembuh"
            self.queue.put(item) 
            print ("Produsen Potion: %s ditambahkan ke dalam antrian %s"\
                   % (item,self.name))
            time.sleep(2)
            print ("Ukuran antrian saat ini adalah %s"\
                   % self.queue.qsize())

class PotionConsumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):
                print("Antrian kosong")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print ("Konsumen Potion: %s dikonsumsi oleh %s \n"\
                       % (item, self.name))
                time.sleep(1)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    produsen = PotionProducer(queue)
    konsumen = PotionConsumer(queue)
    produsen.start()
    konsumen.start()
    produsen.join()
    konsumen.join()
