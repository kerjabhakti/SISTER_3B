import multiprocessing
import time

def purchase_process():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" %name)
    if name == 'Pengajuan Proses':
        for i in range(1,6):
            print('Pengajuan Dilakukan %d\n' %i)
        time.sleep(1)
    else:
        for i in range(1,6):
            print('Pengajuan Antrian %d, telah di approve\n' %i)
        time.sleep(1)
    print ("Close untuk Pengajuan %s \n" %name)
    
if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='Pengajuan Pembelian',\
                          target=purchase_process)
    background_process.daemon = False

    NO_background_process = multiprocessing.Process\
                            (name="Antrian Pembelian Mobil di Auto's Luxury",\
                             target=purchase_process)
    
    NO_background_process.daemon = True
    
    background_process.start()
    NO_background_process.start()
