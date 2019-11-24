import asyncio

async def coroutine():
    print("Coroutine")
    return "Coro"



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print("Starting coroutine")
        coro = coroutine()
        print("Entering event loop")
        result = loop.run_until_complete(coro)
        print(f"{result}")
    finally:
        print("closing event loop")
        loop.close()