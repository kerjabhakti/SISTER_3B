import asyncio
import time
from random import randint


async def start_state():
    print('Memulai state\n')
    input_value = randint(0, 1)
    time.sleep(1)

    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)

    print('Hasil transisi: \nMemulai state memanggil ' + result)


async def state1(transition_value):
    output_value = 'State 1 dengan nilai transisi = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...mengevaluasi...')
    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)

    return output_value + 'State 1 memanggil %s' % result


async def state2(transition_value):
    output_value = 'State 2 dengan nilai transisi = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...mengevaluasi...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)

    return output_value + 'State 2 memanggil %s' % result


async def state3(transition_value):
    output_value = 'State 3 dengan nilai transisi = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...mengevaluasi...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await end_state(input_value)

    return output_value + 'State 3 memanggil %s' % result


async def end_state(transition_value):
    output_value = 'End State dengan nilai transisi = %s\n' % transition_value
    print('...berhenti...')
    return output_value


if __name__ == '__main__':
    print('Simulasi Mesin State Terbatas dengan Asyncio Coroutine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())
