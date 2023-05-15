import asyncio
from random import randint


async def record_attendance(employee):
    print('Recording attendance for', employee)
    await asyncio.sleep(1)
    print('Attendance recorded for', employee)


async def calculate_salary(employee):
    print('Calculating salary for', employee)
    await asyncio.sleep(1)
    salary = randint(1000, 5000)
    print('Salary calculated for', employee, ':', salary)
    return salary


async def pay_employee(employee):
    salary = await calculate_salary(employee)
    print('Paying', employee, 'with salary', salary)
    await asyncio.sleep(1)
    print('Payment completed for', employee)


async def main():
    employees = ['John', 'Jane', 'Alice']
    for employee in employees:
        await record_attendance(employee)
        await pay_employee(employee)


if __name__ == '__main__':
    print('Asynchronous coroutine for payroll processing')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
