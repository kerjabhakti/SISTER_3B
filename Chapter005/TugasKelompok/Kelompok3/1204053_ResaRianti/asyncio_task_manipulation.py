import asyncio

async def record_attendance(teacher):
    print("Recording attendance for", teacher)
    await asyncio.sleep(1)
    print("Attendance recorded for", teacher)

async def calculate_salary(teacher):
    print("Calculating salary for", teacher)
    await asyncio.sleep(1)
    print("Salary calculated for", teacher)

async def main():
    await asyncio.gather(
        record_attendance("Teacher A"),
        calculate_salary("Teacher A"),
        record_attendance("Teacher B"),
        calculate_salary("Teacher B"),
        record_attendance("Teacher C"),
        calculate_salary("Teacher C")
    )

asyncio.run(main())
