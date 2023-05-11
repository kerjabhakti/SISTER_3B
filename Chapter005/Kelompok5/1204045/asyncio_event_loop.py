import asyncio
import time
import random

async def take_order(person):
    print(person, "mengambil pesanan")
    await asyncio.sleep(random.randint(0, 5))
    print(person, "memesan makanan")

async def task_1(end_time, loop):
    print("task_1 called")
    await take_order("Person A")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.ensure_future, task_2(end_time, loop))
    else:
        loop.stop()

async def task_2(end_time, loop):
    print("task_2 called ")
    await take_order("Person B")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.ensure_future, task_3(end_time, loop))
    else:
        loop.stop()

async def task_3(end_time, loop):
    print("task_3 called")
    await take_order("Person C")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.ensure_future, task_1(end_time, loop))
    else:
        loop.stop()


loop = asyncio.get_event_loop()
end_loop = loop.time() + 10
loop.call_soon(asyncio.ensure_future, task_1(end_loop, loop))  # Menjalankan task_1 sebagai Future
loop.run_forever()
loop.close()
