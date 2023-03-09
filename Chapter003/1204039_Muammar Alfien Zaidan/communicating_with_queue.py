import multiprocessing
import random
import time

class petugas(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item) 
            print ("Petugas : nomor antri wahana %d dipanggil ke antrian oleh %s"\
                   % (item,self.name))
            time.sleep(1)
            print ("Jumlah Antrian %s"\
                   % self.queue.qsize())
       
class anak(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):
                print("Antrian kosong")
                break
            else :
                time.sleep(2)
                item = self.queue.get()
                print ('Anak: Wahana %d diguanakan oleh %s \n'\
                       % (item, self.name))
                time.sleep(1)


if __name__ == '__main__':
        queue = multiprocessing.Queue()
        process_producer = petugas(queue)
        process_consumer = anak(queue)
        process_producer.start()
        process_consumer.start()
        process_producer.join()
        process_consumer.join()


        
        
         