import asyncio

# Contoh data waktu kerja
working_hours = {
    'karyawan1': [9, 17],
    'karyawan2': [8, 16],
    'karyawan3': [10, 18],
    # Dan seterusnya
}

# Hitung total jam kerja setiap karyawan
async def calculate_hours(employee):
    start, end = working_hours[employee]
    total_hours = end - start
    await asyncio.sleep(1) # Simulasi waktu komputasi
    return employee, total_hours

# Hitung gaji setiap karyawan berdasarkan total jam kerja
async def calculate_salary(employee, hourly_rate):
    _, total_hours = await calculate_hours(employee)
    salary = hourly_rate * total_hours
    await asyncio.sleep(1) # Simulasi waktu komputasi
    return employee, salary

# Catat kehadiran karyawan
async def register_attendance(employee_id):
    await asyncio.sleep(2) # Simulasi pencatatan kehadiran
    return f"Employee {employee_id} attendance recorded"

# Main function
async def main():
    hourly_rate = 10000
    num_employees = 3

    tasks = []
    for i in range(num_employees):
        employee_id = i + 1
        tasks.append(register_attendance(employee_id))
        tasks.append(calculate_salary(f'karyawan{i+1}', hourly_rate))

    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

# Jalankan program
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
