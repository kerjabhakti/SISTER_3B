from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

jml_pemain = 4  # jumlah pemain dalam game
finish_line = Barrier(jml_pemain)  # batas antara level
players = ['Udin', 'Usep', 'Utin', 'Ujang']  # nama pemain

def player():
    name = players.pop()  # mengambil pemain dari antrian
    sleep(randrange(2, 5))  # simulasi bermain game
    print('%s mencapai level baru pada: %s \n' % (name, ctime()))
    finish_line.wait()  # menunggu pemain lain mencapai level yang sama

def main():
    threads = []
    print('Game dimulai!!!')
    for i in range(jml_pemain):
        threads.append(Thread(target=player))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Semua pemain telah mencapai level baru!')

if __name__ == "__main__":
    main()