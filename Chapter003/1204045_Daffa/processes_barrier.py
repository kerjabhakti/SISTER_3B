import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime


def read_quran(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("Hari ini %s membaca Al-Quran pada %s" \
              %(name,datetime.fromtimestamp(now).strftime("%H:%M:%S")))

if __name__ == '__main__':
    synchronizer = Barrier(4)  # 4 proses, sesuai dengan jumlah target harian
    serializer = Lock()
    Process(name='Musa', target=read_quran, args=(synchronizer, serializer)).start()
    Process(name='Aisha', target=read_quran, args=(synchronizer, serializer)).start()
    Process(name='Umar', target=read_quran, args=(synchronizer, serializer)).start()
    Process(name='Khadijah', target=read_quran, args=(synchronizer, serializer)).start()
