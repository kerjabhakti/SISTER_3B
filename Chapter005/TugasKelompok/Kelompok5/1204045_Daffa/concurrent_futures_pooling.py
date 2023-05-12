import concurrent.futures
import time

order_list = ["Pizza", "Burger", "Fries", "Spaghetti", "Salad"]

def prepare_order(order):
    # Simulate order preparation process
    time.sleep(2)
    print(f"Prepared {order}")

if __name__ == '__main__':
    # Sequential Execution
    start_time = time.perf_counter()
    for order in order_list:
        prepare_order(order)
    print('Sequential Execution in %s seconds' % (time.perf_counter() - start_time))

    # Thread Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(prepare_order, order_list)
    print('Thread Pool Execution in %s seconds' % (time.perf_counter() - start_time))

    # Process Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(prepare_order, order_list)
    print('Process Pool Execution in %s seconds' % (time.perf_counter() - start_time))
