import threading


def game(level):
    return print('Kamu berhasil mencapai level {}'.format(level))


def main():
    threads = []
    for i in range(1, 11):
        t = threading.Thread(target=game, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()
