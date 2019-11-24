import asyncio
async def wrapped():
    print("Wrapped")
    return "Te"


async def inner(task):
    print("inner starting")
    print(f"inner waiting for {task}")
    result = await task

async def starter():
    print("Starter creating task")
    task = asyncio.ensure_future(wrapped())
    await inner(task)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print("Entering event loop")
        res = loop.run_until_complete(starter())

    finally:
        loop.close()