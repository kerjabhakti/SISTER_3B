from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_antrian = 3
finish_line = Barrier(num_antrian)
antrian = ['Rojak', 'Bobi', 'Pepo']

def runner():
    name = antrian.pop()
    sleep(randrange(5, 10))
    print('%s dapat antrian : %s \n' % (name, ctime()))
    finish_line.wait()

def main():
    threads = []
    print('List Antrian')
    for i in range(num_antrian):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Masuk sesuai Antrian ya Adek-adek ')

if __name__ == "__main__":
    main()
