import multiprocessing
import random
import time

class officer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(15):
            item = random.randint(0, 100)
            self.queue.put(item) 
            print ("officer : Harap menunggu no antrian %d akan dilayani oleh %s"\
                   % (item,self.name))
            time.sleep(1)
            print ("No antrian %s"\
                   % self.queue.qsize())
       
class teller(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):
                print("No antrian sudah kosong")
                break
            else :
                time.sleep(2)
                item = self.queue.get()
                print ('Nasabah: Pelayanan %d sedang dilakukan oleh %s \n'\
                       % (item, self.name))
                time.sleep(1)


if __name__ == '__main__':
        queue = multiprocessing.Queue()
        process_producer = officer(queue)
        process_consumer = teller(queue)
        process_producer.start()
        process_consumer.start()
        process_producer.join()
        process_consumer.join()


        
        
         