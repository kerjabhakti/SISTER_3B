#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing
import time

def daily_quran_verse(name):
    print(f"{name} is reading today's Quran verse...")
    time.sleep(2)
    print(f"{name} finishes reading today's Quran verse.")

if __name__ == '__main__':
    process_names = ["Eltugrul", "Yahya", "Maryam", "Aisyah"]
    pool = multiprocessing.Pool(processes=4)
    pool.map(daily_quran_verse, process_names)

    pool.close()
    pool.join()

