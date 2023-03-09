import multiprocessing
from myFunc import myFunc

if __name__ == '__main__':
    for i in range(1, 5):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()
