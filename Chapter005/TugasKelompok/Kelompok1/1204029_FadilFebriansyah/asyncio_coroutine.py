import asyncio
import time
from random import randint


async def play_area(transition_value):
    output_value = 'Play Area with transition value = %s\n' % transition_value
    input_value = randint(0, 2)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await slide(input_value)
    elif input_value == 1:
        result = await swing(input_value)
    else:
        result = await sandbox(input_value)

    return output_value + 'Play Area calling %s' % result


async def slide(transition_value):
    output_value = 'Slide with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await swing(input_value)
    else:
        result = await play_area(input_value)

    return output_value + 'Slide calling %s' % result


async def swing(transition_value):
    output_value = 'Swing with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await slide(input_value)
    else:
        result = await sandbox(input_value)

    return output_value + 'Swing calling %s' % result


async def sandbox(transition_value):
    output_value = 'Sandbox with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await play_area(input_value)
    else:
        result = await swing(input_value)

    return output_value + 'Sandbox calling %s' % result


async def visit_child(child):
    print('Visiting', child)
    await asyncio.sleep(1)
    print('Finished visiting', child)


async def main():
    children = ['Ilman', 'Nawaf', 'Daffa', 'Fadil']
    for child in children:
        await visit_child(child)


if __name__ == '__main__':
    print('Simulation of Children\'s Play Area using Asyncio Coroutine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(play_area(0), main()))
    loop.close()
