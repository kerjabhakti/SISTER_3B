import asyncio
from random import randint


async def play_area(transition_value):
    output_value = f'Play Area with transition value = {transition_value}\n'
    input_value = randint(0, 2)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await slide(input_value)
    elif input_value == 1:
        result = await swing(input_value)
    else:
        result = await sandbox(input_value)

    return f'{output_value}Play Area calling {result}'


async def slide(transition_value):
    output_value = f'Slide with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await swing(input_value)
    else:
        result = await play_area(input_value)

    return f'{output_value}Slide calling {result}'


async def swing(transition_value):
    output_value = f'Swing with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await slide(input_value)
    else:
        result = await sandbox(input_value)

    return f'{output_value}Swing calling {result}'


async def sandbox(transition_value):
    output_value = f'Sandbox with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await play_area(input_value)
    else:
        result = await swing(input_value)

    return f'{output_value}Sandbox calling {result}'


async def visit_child(child):
    print(f'Visiting {child}')
    await asyncio.sleep(1)
    print(f'Finished visiting {child}')


async def simulate_play_area():
    print('Simulation of Children\'s Play Area using Asyncio Coroutine')
    children = ['Ilman', 'Nawaf', 'Daffa', 'Fadil']
    for child in children:
        await visit_child(child)
    result = await play_area(0)
    print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(simulate_play_area())
    loop.close()
