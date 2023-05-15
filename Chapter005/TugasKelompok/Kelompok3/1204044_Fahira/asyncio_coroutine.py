import asyncio
import time
from random import randint


async def start_state():
    print('Memulai proses penggajian dan honor\n')
    time.sleep(1)
    input_value = input('Masukkan jam kerja: ')
    input_value = int(input_value)

    if input_value < 40:
        result = await state1(input_value)
    elif input_value >= 40 and input_value < 60:
        result = await state2(input_value)
    else:
        result = await state3(input_value)

    print('Hasil dari mesin keadaan hingga: \n' + result)


async def state1(transition_value):
    output_value = 'Anda bekerja %d jam, gaji Anda Rp. %d\n' % (transition_value, transition_value * 10000)
    return output_value


async def state2(transition_value):
    output_value = 'Anda bekerja %d jam, gaji Anda Rp. %d\n' % (transition_value, (40 * 10000) + ((transition_value - 40) * 15000))
    return output_value


async def state3(transition_value):
    output_value = 'Anda bekerja %d jam, gaji Anda Rp. %d\n' % (transition_value, (40 * 10000) + (20 * 15000) + ((transition_value - 60) * 20000))
    return output_value


if __name__ == '__main__':
    print('Simulasi mesin keadaan hingga untuk penggajian dan honor dengan asyncio coroutine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())
