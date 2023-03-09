import multiprocessing
import time

def stock():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" %name)
    if name == 'stock ditambah':
        for i in range(5,10):
            print('stock bertambah---> %d \n' %i)
        time.sleep(1)
    else:
        for i in range(1,6):
            print('stock berkurang---> %d \n' %i)
        time.sleep(1)
    print ("Exiting %s \n" %name)
    

if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='stock ditambah',\
                          target=stock)
    background_process.daemon = True

    NO_background_process = multiprocessing.Process\
                            (name='stock diambil',\
                             target=stock)
    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
    

