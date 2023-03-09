import multiprocessing
import time

def add_stock():
    name = multiprocessing.current_process().name
    print ("Starting process name = %s \n" %name)
    stock = 0
    time.sleep(3)
    stock += 1
    print ("Stock: %d" %stock)
    print ("Exiting process name = %s \n" %name)

if __name__ == '__main__':
    process_with_name = multiprocessing.Process\
                        (name='Add Stock Process',\
                         target=add_stock)

    #process_with_name.daemon = True

    process_with_default_name = multiprocessing.Process\
                                (target=add_stock)

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()
