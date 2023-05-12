import asyncio
import time
import random


async def place_order(customer):
    print("Mencatat orderan dari", customer)
    await asyncio.sleep(random.randint(0, 5))
    print("Order telah disiapkan untuk", customer)


async def waiters_A(end_time, loop):
    print("waiters A Memanggil")
    await place_order("Customer meja A")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.ensure_future, waiters_B(end_time, loop))
    else:
        loop.stop()


async def waiters_B(end_time, loop):
    print("waiters B called ")
    await place_order("Customer meja B")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.ensure_future, waiters_C(end_time, loop))
    else:
        loop.stop()


async def waiters_C(end_time, loop):
    print("waiters C called")
    await place_order("Customer Meja C")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, asyncio.ensure_future, waiters_A(end_time, loop))
    else:
        loop.stop()


loop = asyncio.get_event_loop()
end_loop = loop.time() + 10
# Menjalankan task_A sebagai Future
loop.call_soon(asyncio.ensure_future, waiters_A(end_loop, loop))
loop.run_forever()
loop.close()
