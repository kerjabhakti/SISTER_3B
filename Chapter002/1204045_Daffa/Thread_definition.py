import threading

def haveRead(ayat):
    print('Kamu telah membaca ayat {}'.format(ayat))

def main():
    threads = []
    for i in range(1, 11):
        t = threading.Thread(target=haveRead, args=(i,))
        threads.append(t)
        t.start()
        t.join()

    # Menunggu semua thread selesai sebelum melanjutkan eksekusi
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
