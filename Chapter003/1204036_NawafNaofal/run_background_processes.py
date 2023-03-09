
import multiprocessing
import time

def melawan_musuh():
    name = multiprocessing.current_process().name
    print ("Memulai %s \n" %name)
    if name == 'serang_musuh':
        for i in range(0,5):
            print('Musuh yang dikalahkan ---> %d \n' %i)
        time.sleep(1)
    else:
        for i in range(5,10):
            print('Harta yang diambil---> %d \n' %i)
        time.sleep(1)
    print ("Keluar %s \n" %name)
    

if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='serang_musuh',\
                          target=melawan_musuh)
    background_process.daemon = True

    NO_background_process = multiprocessing.Process\
                            (name='pengumpulan_harta_rampasan',\
                             target=melawan_musuh)
    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
    

