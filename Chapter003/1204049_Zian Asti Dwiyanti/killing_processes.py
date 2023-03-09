import multiprocessing
import time

def check_stock():
    print('Checking stock...')
    # simulasikan pengecekan stock dengan sleep selama 3 detik
    time.sleep(3)
    stock = 100
    return stock

if __name__ == '__main__':
    p = multiprocessing.Process(target=check_stock)
    print('Process before execution:', p, p.is_alive())
    p.start()
    print('Process running:', p, p.is_alive())
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)
    stock = p.exitcode
    if stock > 0:
        print('Stock available:', stock)
    else:
        print('Out of stock!')
