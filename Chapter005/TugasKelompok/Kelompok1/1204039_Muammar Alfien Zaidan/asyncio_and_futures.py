import asyncio
import sys


async def play(child_id):
    # Simulasi waktu bermain
    await asyncio.sleep(2)
    return f"Child {child_id} has finished playing"


async def main():
    # Menentukan jumlah anak yang akan bermain di taman
    num_children = int(input("Enter the number of children: "))

    tasks = [play(i+1) for i in range(num_children)]

    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
