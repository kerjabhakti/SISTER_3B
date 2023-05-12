import asyncio
import sys


async def play(child_id):
    # Simulasi waktu bermain
    await asyncio.sleep(2)
    return f"Child {child_id} has finished playing"


async def main():
    # Menentukan jumlah anak yang akan bermain di taman
    num_children = int(sys.argv[1])

    tasks = []
    for i in range(num_children):
        child_id = i + 1
        tasks.append(play(child_id))

    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
