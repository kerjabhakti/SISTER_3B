import asyncio

async def save_sales_data_to_database(sales_data):
    await asyncio.sleep(1)
    print("Sales data saved to database:", sales_data)

async def main():
    sales_data = [("Item 1", 10), ("Item 2", 15), ("Item 3", 8)]

    tasks = []
    for data in sales_data:
        task = asyncio.create_task(save_sales_data_to_database(data))
        tasks.append(task)

    await asyncio.gather(*tasks)

asyncio.run(main())