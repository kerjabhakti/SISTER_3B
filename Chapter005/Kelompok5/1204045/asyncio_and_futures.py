import asyncio
import sys


async def order_food(order_id):
    # Simulasi pemesanan makanan
    await asyncio.sleep(2)
    return f"Order {order_id} food ordered"


async def main():
    # Menentukan jumlah pesanan makanan
    num_orders = int(sys.argv[1])

    tasks = []
    for i in range(num_orders):
        order_id = i + 1
        tasks.append(order_food(order_id))

    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
