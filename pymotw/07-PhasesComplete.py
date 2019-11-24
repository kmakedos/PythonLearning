import asyncio


async def phase(i):
    print(f'in phase {i}')
    await asyncio.sleep(0.1 * i)
    print(f'Done with phase {i}')
    return f"phase {i} result"


async def main(num_phases):
    print("Starting main")
    phases = [
        phase(i)
        for i in range(num_phases)
    ]
    print("Waiting for phases to complete")
    completed, pending = await asyncio.wait(phases )
    results = [t.result() for t in completed]
    print(f"results {results}")
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(30))
    finally:
        loop.close()


