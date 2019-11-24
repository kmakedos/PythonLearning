import asyncio
import functools

def unlock(lock):
    lock.release()

async def coro1(lock):
    async with lock:
        print("Coro1 acquired lock")
    print("Coro1 released lock")

async def coro2(lock):
    async with lock:
        print("Coro2 acquired lock")
    print("Coro2 released lock")

async def main(loop):
    lock = asyncio.Lock()
    await lock.acquire()
    print(f"Lock acquired {lock.locked()}")
    loop.call_later(0.1, functools.partial(unlock, lock))
    await asyncio.wait([coro1(lock), coro2(lock)])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()