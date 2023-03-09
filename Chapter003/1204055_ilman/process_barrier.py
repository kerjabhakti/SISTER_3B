import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time, sleep
from datetime import datetime


def book_ticket(user_id, synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    sleep(1)  # simulasi waktu untuk booking tiket
    now = time()
    with serializer:
        print("User %s berhasil memesan tiket pada %s. Proses %s berhasil" \
              % (user_id, datetime.fromtimestamp(now), name))


if __name__ == '__main__':
    synchronizer = Barrier(3)
    serializer = Lock()
    Process(name='Saep', target=book_ticket, args=('Saep', synchronizer, serializer)).start()
    Process(name='Mang Nana', target=book_ticket, args=('Mang Nana', synchronizer, serializer)).start()
    Process(name='Balmond', target=book_ticket, args=('Balmond', synchronizer, serializer)).start()
    
