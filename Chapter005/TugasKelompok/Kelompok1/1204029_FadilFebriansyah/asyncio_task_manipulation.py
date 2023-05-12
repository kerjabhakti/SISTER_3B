import asyncio

async def mainan_geser():
    print("Bermain geser...")
    await asyncio.sleep(1)
    print("Selesai bermain geser.")

async def ayunan():
    print("Bermain ayunan...")
    await asyncio.sleep(2)
    print("Selesai bermain ayunan.")

async def kolam_pasir():
    print("Bermain di kolam pasir...")
    await asyncio.sleep(3)
    print("Selesai bermain di kolam pasir.")

async def main():
    await asyncio.gather(
        mainan_geser(),
        ayunan(),
        kolam_pasir()
    )

asyncio.run(main())
