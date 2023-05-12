import concurrent.futures
import time

def calculate_salary(employee):
    # Simulasi perhitungan gaji guru honorer
    time.sleep(1)
    print(f"Salary calculated for {employee}")

if __name__ == '__main__':
    employee_list = ["Roni", "Nana", "Nisa", "Kamal", "Cahyo"]

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
