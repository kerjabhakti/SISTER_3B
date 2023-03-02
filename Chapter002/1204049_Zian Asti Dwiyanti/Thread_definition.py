import threading


def stock(thread_number):
    return print('The remaining stock is {} items'.format(thread_number))


def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=stock, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()