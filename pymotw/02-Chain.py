import asyncio
import functools

async def outer():
    print("In outer")
    result = await phase1()
    result2 = await phase2()

async def phase1():
    print("Phase 1")

async def phase2():
    print("Phase 2")

def callback(arg, *, kwarg="default"):
    print(f"callback invoked with {arg} and {kwarg}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.call_soon(callback,1)
        loop.call_soon(functools.partial(callback, 1, kwarg="SSS"))
        loop.call_soon(callback,5)
        ret = loop.run_until_complete(outer())
    finally:
        loop.close()