import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" %name)
    if name == 'Konsultasi nasabah':
        for i in range(0,5):
            print('Nota Pencatatan %d \n' %i)
        time.sleep(1)
    else:
        for i in range(5,10):
            print('Sukses transaksi %d \n' %i)
        time.sleep(1)
    print ("Exiting %s \n" %name)
    

if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='CS untuk keluhan nasabah',\
                          target=foo)
    background_process.daemon = False

    NO_background_process = multiprocessing.Process\
                            (name='mesin CS untuk keluhan nasabah',\
                             target=foo)
    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
    
