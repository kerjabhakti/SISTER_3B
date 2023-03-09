import multiprocessing
import time
import random

def approveRole():
    name = multiprocessing.current_process().name
    userId = random.randrange(0, 20)
    print ("Admin %s \n" %name)
    time.sleep(3)
    print ("Bapak kos melantik anggota dengan ID %s sebagai aggota baru kontrakan  \n" %userId)
    
if __name__ == '__main__':
    process_with_name = multiprocessing.Process\
                        (name='Terima anggota ',\
                         target=approveRole)

    process_with_default_name = multiprocessing.Process\
                                (target=approveRole)

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()