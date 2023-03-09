import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

def assemble_weapon(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("Proses %s perakitan senjata pada waktu %s" \
              %(name, datetime.fromtimestamp(now)))

def test_weapon():
    name = multiprocessing.current_process().name
    now = time()
    print("Proses %s pengujian senjata pada waktu %s" \
          %(name, datetime.fromtimestamp(now)))

if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(name='P1 - Perakitan Senjata',
            target=assemble_weapon,
            args=(synchronizer,serializer)).start()
    Process(name='P2 - Perakitan Senjata',
            target=assemble_weapon,
            args=(synchronizer,serializer)).start()
    Process(name='P3 - Pengujian Senjata',
            target=test_weapon).start()
    Process(name='P4 - Pengujian Senjata',
            target=test_weapon).start()
