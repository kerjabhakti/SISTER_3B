import multiprocessing
import time

def startprocess():
    print ('Start')
    time.sleep(0.1)
    print ('Finish')

if __name__ == '__main__':
    process = multiprocessing.Process(target=startprocess)
    print ('Sebelum Eksekusi:', process, process.is_alive())
    
    process.start()
    print ('Check saat proses Berjalan:', process, process.is_alive())
    
    process.terminate()
    print ('Check saat proses Dihentikan:', process, process.is_alive())

    process.join()
    print ('Proses join:', process, process.is_alive())