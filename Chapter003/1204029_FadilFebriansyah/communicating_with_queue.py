import multiprocessing
import random
import time

class InputData(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(10):
            nomor_induk = random.randint(1000, 9999)
            nama = 'Peserta Didik ' + str(nomor_induk)
            nilai_ujian = random.randint(60, 100)
            self.queue.put((nomor_induk, nama, nilai_ujian)) 
            print ("Data peserta didik %s dengan nilai ujian %s telah dimasukkan ke dalam antrian oleh %s"\
                   % (nama, nilai_ujian, self.name))
            time.sleep(1)
            print ("Jumlah data peserta didik dalam antrian: %s"\
                   % self.queue.qsize())

class ProcessData(multiprocessing.Process):
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
                nomor_induk, nama, nilai_ujian = self.queue.get()
                rata_rata = (nilai_ujian + random.randint(70, 100))/2
                lulus = "Lulus" if rata_rata >= 75 else "Tidak Lulus"
                print ('Data peserta didik %s dengan nomor induk %s, nilai ujian %s, rata-rata nilai %s, dan status %s telah diproses oleh %s\n'\
                       % (nama, nomor_induk, nilai_ujian, rata_rata, lulus, self.name))
                time.sleep(1)

if __name__ == '__main__':
        queue = multiprocessing.Queue()
        input_data = InputData(queue)
        process_data = ProcessData(queue)
        input_data.start()
        process_data.start()
        input_data.join()
        process_data.join()