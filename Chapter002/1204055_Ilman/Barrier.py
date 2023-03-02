from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

pemesan_tiket = 5
tiket_habis = Barrier(pemesan_tiket)
runners = ['Balmond', 'Unang', 'Dandi', 'Saep', 'Angela']

def runner():
    name = runners.pop()
    sleep(randrange(5, 8))
    print('%s Berhasil memesan tiket pada: %s \n' % (name, ctime()))
    tiket_habis.wait()

def main():
    threads = []
    print('PEMESANAN TIKET DIBUKA!')
    for i in range(pemesan_tiket):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('TIKET HABIS!, Yang belum beruntung sabar ya! hehe.')

if __name__ == "__main__":
    main()