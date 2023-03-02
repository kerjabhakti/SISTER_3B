from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_players = 8
finish_line = Barrier(num_players)
calon_pembeli = ['Tsuna Young', 'Ming Khems', 'Tokio', 'Joseph', 'Shen Long', 'EL', 'Daniel', 'Sonya']

def player():
    name = calon_pembeli.pop()
    sleep(randrange(2, 10))
    print('%s Bergabung pada %s \n' % (name, ctime()))
    finish_line.wait()

def main():
    threads = []
    print("MENUNGGU DI AUTO LUXURY'S !")
    for i in range(num_players):
        
        threads.append(Thread(target=player))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('TRANSAKSI DIMULAI !')

if __name__ == "__main__":
    main()