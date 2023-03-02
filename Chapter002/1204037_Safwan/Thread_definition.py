import threading


def rankPlayed(Laga):
    print('Kamu sudah memainkan Match Rank Sebanyak {}'.format(Laga))


def main():
    threads = []
    for i in range(1, 21):
        t = threading.Thread(target=rankPlayed, args=(i,))
        threads.append(t)
        t.start()
        t.join()

    # Menunggu semua thread selesai sebelum melanjutkan eksekusi
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
