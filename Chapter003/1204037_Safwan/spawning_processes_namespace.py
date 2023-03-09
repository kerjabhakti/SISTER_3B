# Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing


def myFunc(i):
    print('Mengerjakan proses joki akun nomor antrian: %s' % i)
    for j in range(0, i):
        print('Berhasil menjoki akun : nomor antrian %s' % j)
    return


if __name__ == '__main__':
    for i in range(10):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()
