import multiprocessing
import time

def mesan(customer_name):
    print(f"{customer_name} memesan GoRide pada {time.ctime()}.")
    time.sleep(3) 
    print(f"{customer_name} sudah dijemput oleh GoRide pada {time.ctime()}.")

def beres(customer_name):
    print(f"{customer_name} sudah diantar oleh GoRide pada {time.ctime()}.")
    time.sleep(3)  
    print(f"{customer_name} sudah tiba di tujuan pada {time.ctime()}.")

if __name__ == '__main__':
    customers = ['Ilman', 'Daffa', 'Nawaf', 'Fadil']

    processes = []
    for customer in customers:
        p1 = multiprocessing.Process(name=f'GoRide Mesan ({customer})', target=mesan, args=(customer,))
        processes.append(p1)
        p1.start()
        p1.join()
        
        p2 = multiprocessing.Process(name=f'GoRide Beres ({customer})', target=beres, args=(customer,))
        processes.append(p2)
        p2.start()

    for process in processes:
        process.join()

    print('Semua sudah beres diantar semua nya gaes.')
