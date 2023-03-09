import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Starting %s \n" % name)
    if name == 'Klaim Promo':
        for i in range(1, 6):
            print('Klaim promo %d dalam tahap proses\n' % i)
        time.sleep(1)
    else:
        for i in range(1, 6):
            print('Klaim promo %d selesai, proses berhasil\n' % i)
        time.sleep(1)
    print("Exiting %s \n" % name)


if __name__ == '__main__':
    background_process = multiprocessing.Process(name='Klaim Promo',
                                                 target=foo)
    background_process.daemon = False

    NO_background_process = multiprocessing.Process(name='promo disetujui',
                                                    target=foo)

    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()
