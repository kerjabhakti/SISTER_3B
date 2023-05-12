import asyncio
import time
from random import randint


async def start_state():
    print('Selamat datang di aplikasi pemesanan makanan!\n')
    input_value = randint(0, 1)
    time.sleep(1)

    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)

    print('Langkah selanjutnya: ' + result)


async def state1(transition_value):
    output_value = 'Anda sedang memilih menu makanan = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...mengevaluasi...')
    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)

    return output_value + 'Waiters mempersilahkan %s' % result


async def state2(transition_value):
    output_value = 'Anda sedang memilih metode pembayaran = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...mengevaluasi...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)

    return output_value + 'Waiters meminta %s' % result


async def state3(transition_value):
    output_value = 'Anda sedang melakukan konfirmasi pesanan = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)

    print('...mengevaluasi...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await end_state(input_value)

    return output_value + 'Waiters meminta %s' % result


async def end_state(transition_value):
    output_value = 'Pesanan Anda berhasil = %s\n' % transition_value
    print('...menyelesaikan komputasi...')
    return output_value


if __name__ == '__main__':
    print('Simulasi Pemesanan Makanan dengan Asyncio Coroutine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())
