import asyncio
import random

async def record_attendance(employee):
    print("Recording attendance for", employee)
    await asyncio.sleep(random.randint(0, 5))
    print("Attendance recorded for", employee)

async def calculate_salary(employee):
    print("Calculating salary for", employee)
    await asyncio.sleep(random.randint(0, 5))
    salary = random.randint(1000, 5000)
    print(f"{employee}'s salary is {salary}")
    return salary

async def task_A(end_time, loop):
    print("task_A called")
    salary_A = await calculate_salary("Employee A")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.ensure_future, task_B(end_time, loop, salary_A))
    else:
        loop.stop()

async def task_B(end_time, loop, salary_A):
    print("task_B called ")
    salary_B = await calculate_salary("Employee B")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.ensure_future, task_C(end_time, loop, salary_A, salary_B))
    else:
        loop.stop()

async def task_C(end_time, loop, salary_A, salary_B):
    print("task_C called")
    salary_C = await calculate_salary("Employee C")
    total_salary = salary_A + salary_B + salary_C
    print(f"Total salary for this period is {total_salary}")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.ensure_future, task_A(end_time, loop))
    else:
        loop.stop()


loop = asyncio.get_event_loop()
end_loop = loop.time() + 10
loop.call_soon(asyncio.ensure_future, task_A(end_loop, loop))  # Menjalankan task_A sebagai Future
loop.run_forever()
loop.close()
