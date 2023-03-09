#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing

def generateNomorAntri(data):
    result = data*+1
    return result


if __name__ == '__main__':
    inputs = list(range(0,100))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(generateNomorAntri, inputs)

    pool.close() 
    pool.join()  
    print ('Hasil Generate Nomor Antri Wahana: ', pool_outputs)