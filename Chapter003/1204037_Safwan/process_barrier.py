import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time, sleep
from datetime import datetime

# mengklaim promo jasa joki akun


def claim_promo(user_id, synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    sleep(1)
    now = time()
    with serializer:
        print("Akun %s telah mengklaim promo pada %s. Klaim %s diterima"
              % (user_id, datetime.fromtimestamp(now), name))


if __name__ == '__main__':
    synchronizer = Barrier(5)
    serializer = Lock()
    Process(name='Zizoy', target=claim_promo, args=(
        'Zizoy', synchronizer, serializer)).start()
    Process(name='Wangg', target=claim_promo, args=(
        'Wangg', synchronizer, serializer)).start()
    Process(name='Vergil', target=claim_promo, args=(
        'Vergil', synchronizer, serializer)).start()
    Process(name='StayHalal', target=claim_promo, args=(
        'StayHalal', synchronizer, serializer)).start()
    Process(name='NtisAhoy', target=claim_promo, args=(
        'NtisAhoy', synchronizer, serializer)).start()
