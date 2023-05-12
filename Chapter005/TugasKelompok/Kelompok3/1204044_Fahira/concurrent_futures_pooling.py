import concurrent.futures
import time

# Data of employees, each tuple contains (name, hours_worked, hourly_rate)
employees = [
    ('John', 160, 15),
    ('Jane', 120, 20),
    ('Bob', 180, 10),
    ('Alice', 200, 25),
    ('Mike', 150, 18)
]

def calculate_payroll(employee):
    name, hours_worked, hourly_rate = employee
    salary = hours_worked * hourly_rate
    return (name, salary)

def calculate_honor(employee):
    name, hours_worked, hourly_rate = employee
    honorarium = 0
    if hours_worked > 160:
        honorarium = (hours_worked - 160) * hourly_rate * 1.5
    return (name, honorarium)

if __name__ == '__main__':
    # Sequential Execution
    start_time = time.perf_counter()
    for employee in employees:
        name, salary = calculate_payroll(employee)
        print(f"{name} earned ${salary} for this month")
    print('Sequential Execution in %s seconds' % (time.perf_counter() - start_time))

    # Thread Pool Execution for Payroll
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = [executor.submit(calculate_payroll, employee) for employee in employees]
        for future in concurrent.futures.as_completed(results):
            name, salary = future.result()
            print(f"{name} earned ${salary} for this month")
    print('Thread Pool Execution for Payroll in %s seconds' % (time.perf_counter() - start_time))

    # Process Pool Execution for Honorarium
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        results = [executor.submit(calculate_honor, employee) for employee in employees]
        for future in concurrent.futures.as_completed(results):
            name, honorarium = future.result()
            if honorarium > 0:
                print(f"{name} earned ${honorarium} as honorarium for this month")
    print('Process Pool Execution for Honorarium in %s seconds' % (time.perf_counter() - start_time))
