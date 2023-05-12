import asyncio
import random
import time

async def slide(child):
    print(f"{child} sedang bermain di slide")
    await asyncio.sleep(random.randint(1, 5))
    print(f"{child} selesai bermain di slide")

async def monkey_bars(child):
    print(f"{child} sedang bermain di monkey bars")
    await asyncio.sleep(random.randint(1, 5))
    print(f"{child} selesai bermain di monkey bars")

async def sandbox(child):
    print(f"{child} sedang bermain di kotak pasir")
    await asyncio.sleep(random.randint(1, 5))
    print(f"{child} selesai bermain di kotak pasir")

async def play_area(child, play_areas):
    for play_area in play_areas:
        await play_area(child)

async def child_play_area(child, play_areas):
    print(f"{child} memasuki area bermain")
    await play_area(child, play_areas)
    print(f"{child} meninggalkan area bermain")

async def main(num_children):
    play_areas = [slide, monkey_bars, sandbox]
    children = [f"Anak-{i}" for i in range(1, num_children+1)]
    while True:
        tasks = []
        for child in children:
            tasks.append(asyncio.ensure_future(child_play_area(child, play_areas)))
        await asyncio.gather(*tasks)
        print("Semua anak telah selesai bermain di semua area bermain")
        await asyncio.sleep(5)

if __name__ == "__main__":
    num_children = 3
    asyncio.run(main(num_children))
