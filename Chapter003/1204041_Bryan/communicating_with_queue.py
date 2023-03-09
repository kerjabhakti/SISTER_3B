import multiprocessing
import random
import time

class barang_baru(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item) 
            print ("Sisa Suku Cadang Mobil Import : %d yang tersedia  %s"\
                   % (item,self.name))
            time.sleep(1)
            print ("Suku Cadang Mobil Import Baru yang baru datang: %s"\
                   % self.queue.qsize())
       
class suku_cadang(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):
                print("Mohon Maaf barangnya sudah Sold Out")
                break
            else :
                time.sleep(2)
                item = self.queue.get()
                print ('Suku Cadang Sudah Terjual : %d  \
                        dari  %s \n'\
                       % (item, self.name))
                time.sleep(1)


if __name__ == '__main__':
        queue = multiprocessing.Queue()
        proses_sm = barang_baru(queue)
        proses_sc = suku_cadang(queue)
        proses_sm.start()
        proses_sc.start()
        proses_sm.join()
        proses_sc.join()
