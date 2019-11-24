import asyncio
import functools


def callback(future, n):
    print(f"{future} done {n}")


async def register_callbacks(all_done):
    print("Registering callbacks")
    all_done.add_done_callback(functools.partial(callback, n=1))
    all_done.add_done_callback(functools.partial(callback, n=2))


async def main(all_done):
    await register_callbacks(all_done)
    all_done.set_result('Done result')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        all_done = asyncio.Future()
        loop.run_until_complete(main(all_done))
    finally:
        loop.close()