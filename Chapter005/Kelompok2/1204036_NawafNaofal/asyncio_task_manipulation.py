import asyncio
import random

async def battle(enemy_name, enemy_hp):
    print(f"Player memasuki pertarungan dengan {enemy_name}!")
    while enemy_hp > 0:
        player_dmg = random.randint(10, 20)
        enemy_hp -= player_dmg
        print(f"Player menyerang {enemy_name} dan mengurangi {player_dmg} HP-nya.")
        if enemy_hp <= 0:
            break
        enemy_dmg = random.randint(5, 15)
        print(f"{enemy_name} menyerang player dan mengurangi {enemy_dmg} HP-nya.")
        await asyncio.sleep(1)
    print(f"Player berhasil mengalahkan {enemy_name} dan mendapatkan XP!")

async def explore_area(area_name, enemy_name, enemy_hp):
    print(f"Player memasuki area {area_name}.")
    await asyncio.sleep(random.randint(1, 3))
    print(f"Player bertemu dengan {enemy_name}!")
    await asyncio.sleep(random.randint(1, 3))
    await battle(enemy_name, enemy_hp)

async def main():
    await asyncio.gather(
        explore_area("Hutan Angker", "Goblin", 30),
        explore_area("Gunung Berapi", "Naga", 50),
        explore_area("Pantai Terpencil", "Harimau", 40)
    )

asyncio.run(main())
