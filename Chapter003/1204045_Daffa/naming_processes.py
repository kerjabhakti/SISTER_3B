import multiprocessing
import time

def read_quran():
    for i in range(1, 31):
        print(f"{multiprocessing.current_process().name} is reading Surah Al-Mulk, Ayat {i}")
        time.sleep(1)

def myFunc():
    name = multiprocessing.current_process().name
    print (f"Starting process name = {name}")
    read_quran()
    print (f"Exiting process name = {name}")

if __name__ == '__main__':
    process_1 = multiprocessing.Process(name='Ali', target=myFunc)
    process_2 = multiprocessing.Process(name='Budi', target=myFunc)

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()
