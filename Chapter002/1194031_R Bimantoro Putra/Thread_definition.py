import threading


def kontrakan(bayar):
    return print('Tagihan ke - {}'.format(bayar), 'Telah di bayar')


def main():
    threads = []
    for i in range(1, 10):
        t = threading.Thread(target=kontrakan, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()
