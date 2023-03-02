from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_client = 10 #no antrian nasabah 
finish_line = Barrier(num_client)
clientNumber = [ '001', '002', '003', '004', '005', '006', '007', '008', '009', '010' ] #no antrian nasabah

def client():
    name = clientNumber.pop()
    sleep(randrange(2, 5))
    print('%s Bergabung pada %s \n' % (name, ctime()))
    finish_line.wait()  # waiting for client 

def main():
    threads = []
    print("Silahkan menunggu nomor antrian anda dipanggil !")
    for i in range(num_client):    
        threads.append(Thread(target=client))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Pelayanan telah tersedia!')

if __name__ == "__main__":
    main()