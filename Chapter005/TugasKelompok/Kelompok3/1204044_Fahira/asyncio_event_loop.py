import asyncio
import random
import time

# Daftar pekerjaan yang ada di perusahaan
JOBS = {
    "manager": 10000000,  # gaji manager per bulan
    "developer": 5000000,  # gaji developer per bulan
    "designer": 3000000,  # gaji designer per bulan
}

async def manager(employee):
    print(f"{employee} sedang melakukan pekerjaan sebagai manager")
    await asyncio.sleep(random.randint(1, 5))
    print(f"{employee} selesai melakukan pekerjaan sebagai manager")
    return JOBS["manager"]

async def developer(employee):
    print(f"{employee} sedang melakukan pekerjaan sebagai developer")
    await asyncio.sleep(random.randint(1, 5))
    print(f"{employee} selesai melakukan pekerjaan sebagai developer")
    return JOBS["developer"]

async def designer(employee):
    print(f"{employee} sedang melakukan pekerjaan sebagai designer")
    await asyncio.sleep(random.randint(1, 5))
    print(f"{employee} selesai melakukan pekerjaan sebagai designer")
    return JOBS["designer"]

async def calculate_salary(employee, jobs):
    print(f"{employee} memulai perhitungan gaji")
    salary = 0
    for job in jobs:
        salary += await job(employee)
    print(f"{employee} selesai perhitungan gaji")
    return salary

async def employee_salary(employee, jobs):
    print(f"{employee} memulai pekerjaan")
    salary = await calculate_salary(employee, jobs)
    print(f"{employee} selesai pekerjaan, mendapatkan gaji sebesar {salary}")
    return salary

async def main(num_employees):
    employees = [f"Karyawan-{i}" for i in range(1, num_employees+1)]
    while True:
        tasks = []
        for employee in employees:
            jobs = random.sample(list(JOBS.keys()), k=random.randint(1, len(JOBS)))
            tasks.append(asyncio.ensure_future(employee_salary(employee, [globals()[job] for job in jobs])))
        salaries = await asyncio.gather(*tasks)
        total_salary = sum(salaries)
        print(f"Total gaji seluruh karyawan adalah {total_salary}")
        await asyncio.sleep(5)

if __name__ == "__main__":
    num_employees = 3
    asyncio.run(main(num_employees))
