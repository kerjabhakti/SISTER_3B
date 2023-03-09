import multiprocessing
import random
import time


class Pemilik(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(4):
            kostrakan = random.randrange(0, 20)
            self.queue.put(kostrakan) 
            print ("Proses Pemilik : User dengan ID %d Merequest Role sebagai Pemilik"\
                   % (kostrakan))
            time.sleep(1)
            print ("Jumlah User yang melakukan Request %s"\
                   % self.queue.qsize())
       
class Pencari(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):
                print("Tidak Ada User yang request Role :(")
                break
            else :
                time.sleep(2)
                item = self.queue.get()
                print ('Proses Pencari : Bangunan %d Tersedia \
                        dimiliki oleh %s \n'\
                       % (item, self.name))
                time.sleep(1)


if __name__ == '__main__':
        queue = multiprocessing.Queue()
        process_Pemilik = Pemilik(queue)
        process_pencari = Pencari(queue)
        process_Pemilik.start()
        process_pencari.start()
        process_Pemilik.join()
        process_pencari.join()
