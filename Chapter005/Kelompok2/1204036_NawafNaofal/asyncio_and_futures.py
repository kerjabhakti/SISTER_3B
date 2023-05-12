import asyncio
import sys


async def player_attack(level):
    attack = level * 5
    await asyncio.sleep(2)
    return attack


async def monster_attack(power):
    attack = power * 3
    await asyncio.sleep(2)
    return attack


async def battle(player_level, monster_power):
    player_task = asyncio.create_task(player_attack(player_level))
    monster_task = asyncio.create_task(monster_attack(monster_power))
    await asyncio.gather(player_task, monster_task)
    player_attack_result = player_task.result()
    monster_attack_result = monster_task.result()
    if player_attack_result > monster_attack_result:
        return 'Pemain menang! (Karena serangan sebesar %s berhasil mengalahkan serangan monster sebesar %s)' % (player_attack_result, monster_attack_result)
    elif player_attack_result < monster_attack_result:
        return 'Monster menang! (Karena serangan sebesar %s berhasil mengalahkan serangan pemain sebesar %s)' % (monster_attack_result, player_attack_result)
    else:
        return 'Pertarungan berakhir seri! (Karena serangan pemain dan monster sama kuat, yakni %s)' % player_attack_result


async def main():
    player_level = int(sys.argv[1])
    monster_power = int(sys.argv[2])

    result = await battle(player_level, monster_power)
    print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
