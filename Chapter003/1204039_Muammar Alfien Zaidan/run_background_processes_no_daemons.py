import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" %name)
    if name == 'wahana komidi putar':
        for i in range(0,5):
            print('Kursi wahana %d \n' %i)
        time.sleep(1)
    else:
        for i in range(5,10):
            print('Mesin wahana %d \n' %i)
        time.sleep(1)
    print ("Exiting %s \n" %name)
    

if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='wahana komidi putar',\
                          target=foo)
    background_process.daemon = False

    NO_background_process = multiprocessing.Process\
                            (name='mesin wahana komidi putar',\
                             target=foo)
    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
    
