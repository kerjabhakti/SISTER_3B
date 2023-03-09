import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

stock = 0

def supplier(synchronizer, serializer):
    global stock
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        stock += 10
        print("Supplier %s -> supplied 10 items at %s. Stock: %s" \
              %(name, datetime.fromtimestamp(now), stock))

def customer():
    name = multiprocessing.current_process().name
    now = time()
    print("Customer %s -> stock diambil dari gudang pada %s" %(name, datetime.fromtimestamp(now)))
    
if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(name='supplier1'\
            ,target=supplier,\
            args=(synchronizer,serializer)).start()
    Process(name='supplier2'\
            ,target=supplier,\
            args=(synchronizer,serializer)).start()
    Process(name='customer1'\
            ,target=customer).start()
    Process(name='customer2'\
            ,target=customer).start()
    
