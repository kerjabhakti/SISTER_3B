from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_students = 5
submission_box = Barrier(num_students)
students = ['Wangg', 'NtisAhoy', 'Vergil', 'Zizoy', 'STAY HALAL']

def student():
    name = students.pop()
    sleep(randrange(2, 10))
    print('%s telah menyerahkan tugas pada %s \n' % (name, ctime()))
    submission_box.wait()

def main():
    threads = []
    print('TUNGGU YA! SEDANG MENGUMPULKAN TUGAS...')
    for i in range(num_students):
        threads.append(Thread(target=student))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('SEMUA TUGAS TELAH DIKUMPULKAN!')

if __name__ == "__main__":
    main()
