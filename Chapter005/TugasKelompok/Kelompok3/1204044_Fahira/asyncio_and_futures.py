import asyncio
import sys


async def hitung_gaji(jam_kerja, tarif):
    gaji = jam_kerja * tarif
    await asyncio.sleep(3)
    return 'Total gaji: Rp %d' % gaji


async def hitung_honor(jam_kerja, tarif):
    honor = jam_kerja * tarif
    await asyncio.sleep(3)
    return 'Total honor: Rp %d' % honor


def got_result(future):
    print(future.result())


if __name__ == '__main__':
    jam_kerja = int(sys.argv[1])
    tarif = int(sys.argv[2])

    loop = asyncio.get_event_loop()
    task1 = loop.create_task(hitung_gaji(jam_kerja, tarif))
    task2 = loop.create_task(hitung_honor(jam_kerja, tarif))

    task1.add_done_callback(got_result)
    task2.add_done_callback(got_result)

    loop.run_until_complete(asyncio.wait([task1, task2]))
    loop.close()
