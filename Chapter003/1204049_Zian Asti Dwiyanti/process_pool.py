import multiprocessing

def add_stock(stock):
    print(f'Current stock: {stock}')
    stock += 1
    print(f'Added 1 stock, now stock: {stock}')
    return stock

if __name__ == '__main__':
    inputs = list(range(0,100))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(add_stock, inputs)

    pool.close() 
    pool.join()  
    print ('Stock after adding: ', pool_outputs)
