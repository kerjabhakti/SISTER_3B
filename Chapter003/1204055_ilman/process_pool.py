#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing

def function_square(data):
    result = data*data
    return result


if __name__ == '__main__':
    inputs = list(range(0,324))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)

    pool.close() 
    pool.join()  
    print ('Jumlah penonton film "Avanger: End Game" secara bertahap:', "\n", pool_outputs)
    print('Total penonton film "Avanger: End Game" selama 1 minggu :', sum(pool_outputs))