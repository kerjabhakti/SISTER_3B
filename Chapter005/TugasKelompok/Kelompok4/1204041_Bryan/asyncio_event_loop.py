import asyncio
import time
import random

async def record_attendance(employee):
    print("Recording attendance for", employee)
    await asyncio.sleep(random.randint(0, 5))
    print("Attendance recorded for", employee)

async def task_A(end_time, loop):
    print("task_A called")
    await record_attendance("Employee A")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.ensure_future, task_B(end_time, loop))
    else:
        loop.stop()

async def task_B(end_time, loop):
    print("task_B called ")
    await record_attendance("Employee B")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.ensure_future, task_C(end_time, loop))
    else:
        loop.stop()

async def task_C(end_time, loop):
    print("task_C called")
    await record_attendance("Employee C")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.ensure_future, task_A(end_time, loop))
    else:
        loop.stop()


loop = asyncio.get_event_loop()
end_loop = loop.time() + 10
loop.call_soon(asyncio.ensure_future, task_A(end_loop, loop))  # Menjalankan task_A sebagai Future
loop.run_forever()
loop.close()
