import asyncio
import sys


async def register_order(order_id):
    # Simulasi pencatatan pemesanan makanan
    await asyncio.sleep(2)
    return f"Order pelanggan meja {order_id} telah dicatat"


async def main():
    # Menentukan jumlah pesanan makanan yang akan dicatat
    num_orders = int(sys.argv[1])

    tasks = []
    for i in range(num_orders):
        order_id = i + 1
        tasks.append(register_order(order_id))

    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
