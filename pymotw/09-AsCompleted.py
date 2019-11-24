import asyncio

async def phase(i):
    print(f"phase {i}")
    await asyncio.sleep(0.5 - (0.1 * i))
    print(f"Done with phase {i}")
    return f"phase {i} result"

async def main(num_phases):
    print("Starting main")
    phases = [ phase(i) for i in range(num_phases)]
    print("Waiting for phases")

    results = []

    for next_to_complete in asyncio.as_completed(phases):
        answer = await next_to_complete
        print(f"Received {answer}")
        results.append(answer)
    print(f"results {results}")
    return results

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(20))
    finally:
        loop.close()