import asyncio


async def task_func():
    print('In task func')
    return 'Te'

async def main(loop):
    print("In main")
    task = loop.create_task(task_func())
    print(f"Waiting for {task}")
    return_val = await task
    print(f"{task} complete")
    print(f"return value: {return_val}")




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()