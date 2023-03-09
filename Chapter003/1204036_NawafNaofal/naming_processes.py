import multiprocessing
import time

def mySpell(element):
    name = multiprocessing.current_process().name
    print ("Menyihir sihir %s dengan elemen %s.." % (name, element))
    time.sleep(3)
    print ("Keluar dari sihir %s dengan elemen %s..." % (name, element))

if __name__ == '__main__':
    process_with_name = multiprocessing.Process\
        (name='Inferno Blast',\
        target=mySpell,\
        args=('Api',))

    process_with_default_name = multiprocessing.Process\
        (target=mySpell,\
        args=('Listrik',))

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()
