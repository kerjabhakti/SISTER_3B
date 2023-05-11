import asyncio
import sys


async def register_attendance(employee_id):
    # Simulasi pencatatan kehadiran pegawai
    await asyncio.sleep(2)
    return f"Employee {employee_id} attendance recorded"


async def main():
    # Menentukan jumlah pegawai yang akan dicatat kehadirannya
    num_employees = int(sys.argv[1])

    tasks = []
    for i in range(num_employees):
        employee_id = i + 1
        tasks.append(register_attendance(employee_id))

    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
