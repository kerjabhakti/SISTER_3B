from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

reader = 7  # count of quran reader
finish_line = Barrier(reader)
readersName = ['John', 'Doe', 'Alexa', 'Sooho', 'Lee', 'Han', 'Mehmed']  # name of reader

def threadFunc():
    name = readersName.pop()  # take the reader from queue
    sleep(randrange(2, 5))  # simulation of read
    print('%s has read the Quran at: %s \n' % (name, ctime()))
    finish_line.wait()  # waiting for all readers to reach the same ayat

def main():
    threads = []
    print('Information of readers today:')
    for i in range(reader):
        threads.append(Thread(target=threadFunc))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('All readers have finished reading the Quran today.')

if __name__ == "__main__":
    main()
