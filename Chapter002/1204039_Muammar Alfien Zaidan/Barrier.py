from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

jml_anak = 4
akhir_permainan = Barrier(jml_anak)
anak = ['Anak 1', 'Anak 2', 'Anak 3', 'Anak 4']

def pemain():
    name = anak.pop()
    sleep(randrange(2, 5))
    print('%s menyelesaikan permainan pada: %s \n' % (name, ctime()))
    akhir_permainan.wait()

def main():
    threads = []
    print('---Permainan Dimulai---')
    for i in range(jml_anak):
        threads.append(Thread(target=pemain))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('---Permainan selesai---')

if __name__ == "__main__":
    main()

# import threading

# # create a Barrier object with a count of 2
# barrier = threading.Barrier(8)

# def thread_func(urutan):
#     print("Anak %s menunggu di gerbang wahana" % (urutan))
#     # wait at the barrier until all threads have reached this point
#     barrier.wait()
#     print("Anak %s keluar dari wahana" % (urutan))

# # create threads and start them
# thread1 = threading.Thread(target=thread_func, args=("Anak 1",))
# thread2 = threading.Thread(target=thread_func, args=("Anak 2",))
# thread3 = threading.Thread(target=thread_func, args=("Anak 3",))
# thread4 = threading.Thread(target=thread_func, args=("Anak 4",))
# thread5 = threading.Thread(target=thread_func, args=("Anak 5",))
# thread6 = threading.Thread(target=thread_func, args=("Anak 6",))
# thread7 = threading.Thread(target=thread_func, args=("Anak 7",))
# thread8 = threading.Thread(target=thread_func, args=("Anak 8",))

# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
# thread7.start()
# thread8.start()

# # wait for both threads to finish
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()
# thread6.join()
# thread7.join()
# thread8.join()
