from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_customers = 3
order_line = Barrier(num_customers)
customers = ['Alice', 'Bob', 'Charlie']


def customer():
    name = customers.pop()
    sleep(randrange(2, 5))
    print('%s placed an order at: %s \n' % (name, ctime()))
    order_line.wait()


def main():
    threads = []
    print('START ORDERING!!!!')
    for i in range(num_customers):
        threads.append(Thread(target=customer))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('All orders have been placed!')


if __name__ == "__main__":
    main()
