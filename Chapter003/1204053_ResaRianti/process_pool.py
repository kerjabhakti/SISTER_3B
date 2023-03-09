#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing

def QueueNumbers(data):
    result = data*+1
    return result


if __name__ == '__main__':
    inputs = list(range(0,50))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(QueueNumbers, inputs)

    pool.close() 
    pool.join()  
    print ('Total antrian bank hari ini: ', pool_outputs)