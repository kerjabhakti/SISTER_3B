import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime


def test_with_barrier(synchronizer, serializer, task):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("process %s ----> %s" %(name,datetime.fromtimestamp(now)))
        print("Task for process %s: %s" %(name, task))

def test_without_barrier(task):
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" %(name ,datetime.fromtimestamp(now)))
    print("Task for process %s: %s" %(name, task))

if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()
    task_list = ["Task 1", "Task 2", "Task 3", "Task 4"]
    Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer,serializer,task_list[0])).start()
    Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer,serializer,task_list[1])).start()
    Process(name='p3 - test_without_barrier', target=test_without_barrier, args=(task_list[2],)).start()
    Process(name='p4 - test_without_barrier', target=test_without_barrier, args=(task_list[3],)).start()
