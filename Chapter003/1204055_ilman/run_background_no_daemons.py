import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" %name)
    if name == 'pemesanan tiket!':
        for i in range(1,6):
            print('Pemesanan tiket %d sedang di proses\n' %i)
        time.sleep(1)
    else:
        for i in range(1,6):
            print('Pemesanan tiket %d berhasil di proses\n' %i)
        time.sleep(1)
    print ("Exiting %s \n" %name)
    

if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='pemesanan tiket!',\
                          target=foo)
    background_process.daemon = False

    NO_background_process = multiprocessing.Process\
                            (name='approve tiket',\
                             target=foo)
    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
    
