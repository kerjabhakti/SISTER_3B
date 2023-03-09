#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing

def penjualan(data):
    result = data+data
    return result


if __name__ == '__main__':
    inputs = list(range(0,20))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(penjualan, inputs)

    pool.close() 
    pool.join()  
    print ('Jumlah Pelangan    :', pool_outputs)
    print("Total Pelangan yang Transaksi di Auto's Luxury :", sum(pool_outputs))