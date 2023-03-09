import multiprocessing
import time

def service():
    for i in range(1, 20):
        print(f"{multiprocessing.current_process().name} Teller melayani customer dengan nomor antrian {i}")
        time.sleep(1)

def myFunc():
    name = multiprocessing.current_process().name
    print (f"Starting process name = {name}")
    service()
    print (f"Exiting process name = {name}")

if __name__ == '__main__':
    process_1 = multiprocessing.Process(name='Sarah', target=myFunc)
    process_2 = multiprocessing.Process(name='Amel', target=myFunc)

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()
