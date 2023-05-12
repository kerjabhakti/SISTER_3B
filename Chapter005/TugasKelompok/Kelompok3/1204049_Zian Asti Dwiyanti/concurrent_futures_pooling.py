import concurrent.futures
import time
import random

employee_list = ["John", "Jane", "Alice", "Bob", "Eve"]

def calculate_salary(employee):
    # Simulate salary calculation process
    time.sleep(random.randint(1, 5))
    print(f"Calculated salary for {employee}")

if __name__ == '__main__':
    # Sequential Execution
    start_time = time.perf_counter()
    for employee in employee_list:
        calculate_salary(employee)
    print('Sequential Execution in %s seconds' % (time.perf_counter() - start_time))

    # Thread Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(calculate_salary, employee_list)
    print('Thread Pool Execution in %s seconds' % (time.perf_counter() - start_time))

    # Process Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(calculate_salary, employee_list)
    print('Process Pool Execution in %s seconds' % (time.perf_counter() - start_time))
