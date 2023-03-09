import multiprocessing
from myFunc import iniFunction

if __name__ == '__main__':
    for i in range(3):
        process = multiprocessing.Process(target=iniFunction, args=(i,))
        process.start()
        process.join()

