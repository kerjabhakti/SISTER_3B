from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

players = 5  # count of players
finish_line = Barrier(players)
playersNickname = ['Wangg', 'Zizoy', 'NtisAhoy', 'Vergil',
                   'StayHalal']  # name of players


def threadFunc():
    name = playersNickname.pop()  # take the players from queue
    sleep(randrange(8, 11))  # simulation of playing rank
    print('%s has reached the mythic glory rank at: %s \n' % (name, ctime()))
    finish_line.wait()  # waiting for all readers to reach the same rank


def main():
    threads = []
    print('Players Daily News:')
    for i in range(players):
        threads.append(Thread(target=threadFunc))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('All readers have finished the glory mythic today.')


if __name__ == "__main__":
    main()
