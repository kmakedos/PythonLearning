import asyncio


async def phase(i):
    print(f"Phase {i}")



async def main(phases_num):
    phases = [ phase(i) for i in range(phases_num)]
    return asyncio.gather(phases)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(4))


