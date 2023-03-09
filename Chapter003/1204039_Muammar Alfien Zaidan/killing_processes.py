import multiprocessing
import time

def foo():
    print ('Menjalankan Wahana')
    for i in range(0,10):
        print('-->%d\n' %i)
        time.sleep(1)
    print ('Memberhentikan Wahana')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print ('Wahana sebelum dinyalakan:', p, p.is_alive())
    p.start()
    print ('Wahana berjalan:', p, p.is_alive())
    p.terminate()
    print ('Wahana dimatikan:', p, p.is_alive())
    p.join()
    print ('Wahana dipantau:', p, p.is_alive())
    print ('Wahana exit code:', p.exitcode)