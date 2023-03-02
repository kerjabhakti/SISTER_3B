from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_players = 5
finish_line = Barrier(num_players)
players = ['Wangg', 'NtisAhoy', 'Vergil', 'Zizoy', 'STAY HALAL']

def player():
    name = players.pop()
    sleep(randrange(2, 10))
    print('%s Bergabung pada %s \n' % (name, ctime()))
    finish_line.wait()

def main():
    threads = []
    print('TUNGGU TEMAN TEMAN YA!!!!')
    for i in range(num_players):
        
        threads.append(Thread(target=player))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('GAME DIMULAI!')

if __name__ == "__main__":
    main()