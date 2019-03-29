# From Python 3.5 onwards, async and await are the symbols denoting asycnhronous calls
import asyncio
async def sleeper(delay):
    await asyncio.sleep(delay)
    print("Finished sleeper with delay: %d" % delay)


def test_simple_async():
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.wait((
        sleeper(1),
        sleeper(5),
        sleeper(4),
        sleeper(6),
        sleeper(2),
    )))

def test_task():
    loop = asyncio.get_event_loop()
    # put task in loop
    result = loop.call_soon(loop.create_task, sleeper(1))
    # put task in loop with 2 sec delay
    result = loop.call_later(2, loop.stop)
    # start loop
    loop.run_forever()

def debug_task():
    async def stack_printer():
        for task in asyncio.Task.all_tasks():
            task.print_stack()
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(stack_printer())

def event_loop_selector():
    loop1 = asyncio.ProactorEventLoop()
    loop2 = asyncio.SelectorEventLoop()
    # selecting event loop implementations. Select is used by Linux, Proactor by windows ?

def selectors_show():
    import sys
    import selectors

    def read(fh):
        print('Got input from stdin: %r' % fh.readline())
        return False
    # Selectors we can use are also KqueueSelector, EpollSelector, DevPollSelector
    selector = selectors.DefaultSelector()
    # Register a selector to event read a callback named read
    selector.register(sys.stdin, selectors.EVENT_READ, read)
    rc = True
    while rc:
        for key, mask in selector.select():
            callback = key.data
            rc = callback(key.fileobj)

def event_loop_functions():
    # call_soon: Put item in FIFO end
    # call_soon_threadsafe: Uses GIL
    # call_later: Call function after n secs
    # call_at: Call function at specific time, related to loop.time.
    # All functions return Handle object and they can cancelled with handle.cancel
    import time
    t = time.time()
    def printer(name):
        print('Started %s at %.1f: ' % (name, time.time() - t))
        time.sleep(0.2)
        print('Finished %s at %.1f' % (name, time.time() - t))

    loop = asyncio.get_event_loop()

    result = loop.call_at(loop.time() + .2, printer, 'call_at')
    result = loop.call_later(.1, printer, 'call later')
    result = loop.call_soon(printer, 'call_soon')
    result = loop.call_soon_threadsafe(printer, 'call_soon_threadsafe')
    result = loop.call_later(1, loop.stop)
    loop.run_forever()

def event_loop_async_functions():
    # call_soon: Put item in FIFO end
    # call_soon_threadsafe: Uses GIL
    # call_later: Call function after n secs
    # call_at: Call function at specific time, related to loop.time.
    # All functions return Handle object and they can cancelled with handle.cancel
    import time
    t = time.time()
    async def printer(name):
        print('Started %s at %.1f: ' % (name, time.time() - t))
        await asyncio.sleep(0.2)
        print('Finished %s at %.1f' % (name, time.time() - t))

    loop = asyncio.get_event_loop()

    result = loop.call_at(loop.time() + .2, loop.create_task, printer('call_at'))
    result = loop.call_later(.1, loop.create_task, printer('call later'))
    result = loop.call_soon(loop.create_task, printer('call_soon'))
    result = loop.call_soon_threadsafe(loop.create_task, printer('call_soon_threadsafe'))
    result = loop.call_later(1, loop.stop)
    loop.run_forever()

def serial_subprocess():
    import time
    import subprocess
    t = time.time()

    def process_sleeper():
        print('Started sleep at %.1f ' % (time.time() - t))
        process = subprocess.Popen(['sleep', '0.1'])
        process.wait()
        print('Finished sleep at %.1f' % (time.time() - t))
    for i in range(3):
        process_sleeper()
def parallel_subprocess_naive():
    import time
    import subprocess

    t = time.time()

    def process_sleeper():
        print('Started sleep at %.1f ' % (time.time() - t))
        return subprocess.Popen(['sleep', '0.1'])
    processes = []
    for i in range(5):
        processes.append(process_sleeper())
    for process in processes:
        returncode = process.wait()
        print('Finished sleep at %.1f' % (time.time() - t))



if __name__ == "__main__":
    test_simple_async()
    test_task()
    debug_task()
    #selectors_show()
    event_loop_functions()
    event_loop_async_functions()
    serial_subprocess()
    parallel_subprocess_naive()
