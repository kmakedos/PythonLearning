# Generators generate values whenever a yield is called
# Cautious is needed because Generators can return infinite series
# Pros and Cons of generators
# Pros:
# -> Memory usage low
# -> Results depend on outside factors
# -> Lazy. Values are calculated when needed.
# -> Simpler
# Cons:
# -> Results available once only
# -> Size unknown
# -> Not indexable

class EmptyError(Exception):
    pass

def count(start=1, step=1, stop=10):
    n = start
    while n <= stop:
        yield n
        n += step

def count_test():
    print("Generator test")
    for x in count(10,2,20):
        print(x)

def comprehension_generator_test():
    print("Generator comprehension list")
    generator = ( x ** 2 for x in range(4))
    for y in generator:
        print(y)

def lazy_example_test():
    def generator():
        print('Before 1')
        yield 1
        print('After 1 Cleanup')
        print('Before 2')
        yield 2
        print('After 2 Cleanup')
    g = generator()
    print('Got %d' % next(g))
    print("Normally After 1 Cleanup should be executed BEFORE this statement, but generators are lazy and actions after one yield are"
          "executed on next yield1")
    print('Got %d' % next(g))


def cat_grep_sed_test():
    def cat(filename):
        for line in open(filename):
            yield line.rstrip()

    def grep(sequence, search):
        for line in sequence:
            if search in line:
                yield line
    def sed(sequence, search, replace):
        for line in sequence:
            yield line.replace(search, replace)
    lines = cat('lines.txt')
    print("\nCat")
    for line in lines:
        print(line)
    print()
    lines = cat('lines.txt')
    print("Grep")
    spam_lines = grep(lines, 'spam')
    for line in spam_lines:
        print(line)
    print()
    lines = cat('lines.txt')
    spam_lines = grep(lines, 'spam')
    print("Sed")
    bacon_lines = sed(spam_lines, 'spam', 'bacon')
    for line in bacon_lines:
        print(line)

import itertools
def powerset(sequence):
    for size in range(len(sequence) + 1):
        yield from itertools.combinations(sequence, size)
def flatten(sequence):
    for item in sequence:
        try:
            yield from flatten(item)
        except TypeError:
            yield item

def powerset_flatten_test():
    print("\nPower set of abc")
    for result in powerset('abc'):
        print(result)
    print(list(flatten([1,[1,2] ])))

# Remember to Check contextlib and its uses in: https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack
# Useful when you want to handle exit gracefully
import contextlib
import datetime
@contextlib.contextmanager
def timer(name):
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    print('%s took %s' % (name, stop_time - start_time))

@contextlib.contextmanager
def write_to_log(name):
    with contextlib.ExitStack() as stack:
        fh = stack.enter_context(open('stdout.txt', 'a+'))
        stack.enter_context(contextlib.redirect_stdout(fh))
        stack.enter_context(timer(name))
        yield

import os
def test_context():
    @write_to_log('myfunction')
    def myfunction():
        print("This function takes a little bit time")
        print("A little more")

    myfunction()



def coroutines_basic():
    def generator():
        value = yield 'spam'
        print('Generator received: %s' % value)
        yield 'Previous value: %r' % value
    print("\nCoroutines basic")
    g = generator()
    print("Result from generator: %s" % next(g))
    print(g.send('efffs'))

# You cannot send a value to a brand new generator. A send(None) has to be send to initialize him.
# Let's create a decorator for it
# coroutine decorator essentially calls with initial values the function and then calls next
import functools
def coroutine(function):
    @functools.wraps(function)
    def _coroutine(*args, **kwargs):
        active_coroutine = function(*args, **kwargs)
        next(active_coroutine)
        return active_coroutine
    return _coroutine
@coroutine
def print_(formatstring):
    while True:
        print(formatstring % (yield))


def coroutines_with_decorator():
    @coroutine
    def spam():
        while True:
            print('waiting for a yield')
            value = yield
            print('Spam received %s' % value)

    generator = spam()
    generator.send('a')

    @coroutine
    def simple_coroutine():
        print('Setting up the coroutine')
        try:
            while True:
                item = yield
                print('Got item: %r' % item)
        except GeneratorExit:
            print('Normal Exit')
        except Exception as e:
            print('Exception exit %r' % e)
            raise
        finally:
            print('Any exit')
    print("\nCreating simple coroutine")
    active_coroutine = simple_coroutine()
    print()

    print('Sending spam')
    active_coroutine.send('spam')
    print()

    print('Close the coroutine')
    active_coroutine.close()
    print()

    print('Creating simple coroutine')
    active_coroutine = simple_coroutine()
    print()

    print('Sending eggs')
    active_coroutine.send('eggs')
    print()

    print('Throwing runtime error')
    #active_coroutine.throw(EmptyError, 'oops..')
    print()


def bidirectional_pipelines_simple_silly():
    @coroutine
    def replace(search, replace):
        item = yield
        while True:
            item = yield item.replace(search, replace)

    spam_replace = replace('spam', 'bacon')
    for line in open('lines.txt'):
        print(spam_replace.send(line.rstrip()))

def multiple_pipelines():
    # Grep send all matching items to the target
    @coroutine
    def grep(target, pattern):
        while True:
            item = yield
            if pattern in item:
                target.send(item)

    # Replace does a search and replace on the items and sends it to the target
    @coroutine
    def replace(target, search, replace):
        while True:
            target.send((yield).replace(search, replace))

    # Print will print the items
    @coroutine
    def print(formatstring):
        while True:
            print(formatstring % (yield))

    # Tee multiplexes items to multiple targets
    @coroutine
    def tee(*targets):
        while True:
            item = yield
            for target in targets:
                target.send(item)

    print("\n Starting multiple pipelines")
    printer = print('%s')

    replacer_spam = replace(printer, 'spam', 'bacon')
    replacer_eggs = replace(printer, 'spam spam', 'big sausage')

    branch = tee(replacer_eggs, replacer_spam)

    grepper = grep(branch, 'spam')
    for line in open('lines.txt'):
        grepper.send(line.rstrip())

def state_test():
    @coroutine
    def average():
        count = 1
        total = yield
        while True:
            total += yield total / count
            count += 1
    averager = average()
    print(averager.send(20))
    print(averager.send(10))
    print(averager.send(10))
    print(averager.send(10))

    print()
    @coroutine
    def average(target):
        count = 0
        total = 0
        while True:
            count += 1
            total += yield
            target.send(total/count)
    printer = print_('%.1f')
    averager = average(printer)
    averager.send(20)
    averager.send(10)
    averager.send(6)


def group_by_test():
    @coroutine
    def groupby():
        # Fetch the first key-value and initialize state vars
        key,value = yield
        old_key, values = key, []
        while True:
            # Store previous valuse so we can store it in the list
            old_value = value
            if key == old_key:
                key, value = yield
            else:
                key, value = yield old_key, values
                old_key, values = key, []
            values.append(old_value)

    grouper = groupby()
    print(grouper.send(('a', 1)))
    print(grouper.send(('a', 2)))
    print(grouper.send(('a', 3)))
    print(grouper.send(('b', 1)))
    print(grouper.send(('b', 4)))
    print(grouper.send(('a', 5)))

    print()
    @coroutine
    def groupby2(target):
        old_key = None
        while True:
            key, value = yield
            if old_key != key:
                # a different key means a new group, so send previous and restart cycle
                if old_key and values:
                    target.send((old_key, values))
                values = []
                old_key = key
            values.append(value)

    grouper2 = groupby2(print_('group: %s, values: %s'))
    grouper2.send(('a', 2))
    grouper2.send(('a', 3))
    grouper2.send(('b', 1))


# Coroutines are synchronous and thus problematic to use when time or cpu are needed

if __name__ == "__main__":
    count_test()
    comprehension_generator_test()
    lazy_example_test()
    cat_grep_sed_test()
    powerset_flatten_test()
    test_context()
    coroutines_basic()
    coroutines_with_decorator()
    bidirectional_pipelines_simple_silly()
    multiple_pipelines()
    state_test()
    group_by_test()
