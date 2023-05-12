import asyncio
import sys


async def calculate_salary(employee_id, hours_worked):
    # Simulasi perhitungan gaji berdasarkan jam kerja
    rate_per_hour = 10  # Gaji per jam untuk pegawai honorer
    total_salary = rate_per_hour * hours_worked
    await asyncio.sleep(2)
    return f"Employee {employee_id} salary calculated: ${total_salary}"


async def main():
    # Menentukan jumlah pegawai yang akan dihitung gajinya
    num_employees = int(sys.argv[3])

    tasks = []
    for i in range(num_employees):
        employee_id = i + 1
        hours_worked = 160  # Jam kerja pegawai honorer
        tasks.append(calculate_salary(employee_id, hours_worked))

    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
