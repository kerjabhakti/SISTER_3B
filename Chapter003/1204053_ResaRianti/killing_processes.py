import multiprocessing
import time

def foo():
    print ('Proses Pelayanan sedang berjalan')
    for i in range(0,20):
        print('-->%d\n' %i)
        time.sleep(1)
    print ('Pelayanan sedang bermasalah')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print ('Transaksi sebelum dimulai :', p, p.is_alive())
    p.start()
    print ('Sedang dilakukan pelayanan:', p, p.is_alive())
    p.terminate()
    print ('Adanya kendala, sehingga proses pelayanan transaksi tertunda:', p, p.is_alive())
    p.join()
    print ('Sedang dalam perbaikan:', p, p.is_alive())
    print ('Keluar dari bank :', p.exitcode)