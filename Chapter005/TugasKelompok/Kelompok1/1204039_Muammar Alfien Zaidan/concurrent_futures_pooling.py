import concurrent.futures
import time

children_list = ["Alfien", "Nawaf", "Safwan", "Bryan", "Fadil", "Ilman", "Daffa", "Ressa", "Zian", "Fahira"]

def play_at_playground(child):
    # Simulate playing process
    time.sleep(1)
    print(f"{child} is playing at the playground.")

if __name__ == '__main__':
    # Sequential Execution
    start_time = time.perf_counter()
    for child in children_list:
        play_at_playground(child)
    print('Sequential Execution in %s seconds' % (time.perf_counter() - start_time))

    # Thread Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(play_at_playground, children_list)
    print('Thread Pool Execution in %s seconds' % (time.perf_counter() - start_time))

    # Process Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(play_at_playground, children_list)
    print('Process Pool Execution in %s seconds' % (time.perf_counter() - start_time))
