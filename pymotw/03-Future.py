import asyncio
import time


def mark_done(future, result):
    print(f"setting future result to {result}")
    time.sleep(2)
    future.set_result(result)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        all_done = asyncio.Future()
        loop.call_soon(mark_done, all_done, 'the result')
        rest = loop.run_until_complete(all_done)
        print(rest)
    finally:
        loop.close()
