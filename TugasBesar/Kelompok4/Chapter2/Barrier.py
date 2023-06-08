from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

pemesan_mobil = 5
mobil_habis = Barrier(pemesan_mobil)
users = ['John', 'Sarah', 'Michael', 'Emily', 'David']

def car_selector():
    name = users.pop()
    sleep(randrange(5, 8))
    print('%s berhasil mencari mobil yang cocok pada: %s \n' % (name, ctime()))
    mobil_habis.wait()

def main():
    threads = []
    print('PEMESANAN MOBIL DIBUKA!')
    for i in range(pemesan_mobil):
        threads.append(Thread(target=car_selector))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('MOBIL HABIS!, Silakan tunggu informasi selanjutnya.')

if __name__ == "__main__":
    main()
