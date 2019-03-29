import functools


def spam(eggs):
    return "spam" * (eggs)


def debug(function):
    @functools.wraps(function)
    def _debug(*args, **kwargs):
        output = function(*args, **kwargs)
        print('%s(%r %r): %r' % function(function.__name__, args, kwargs, output))
        return output
    return _debug


def decor_debug_test():
    print("Decorators debuggin test")
    print(spam(6))


def memoize(function):
#    """
#    A function to memoize or cache results from function calls
#    to speed up execution of function
#    @args: a function
#    @ret: function output either cached or from actual call
#    """
    function.cache = dict()

    @functools.wraps(function)
    def _memoize(*args):
        if args not in function.cache:
            function.cache[args] = function(*args)
        return function.cache[args]
    return _memoize


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@memoize
def fibonacci_with_mem(n):
    if n < 2:
        return n
    else:
        return fibonacci_with_mem(n-1) + fibonacci_with_mem(n-2)

def memoize_test():
    print("Executing simple fibonnacci without memoization for n=35")
    print(fibonacci(35))
    print("Executing with memoization for n = 100")
    print(fibonacci_with_mem(100))

def counter(function):
    function.calls = 0
    @functools.wraps(function)
    def _counter(*args, **kwargs):
        function.calls += 1
        return function(*args, **kwargs)
    return _counter

def lru_test(n=10):
    @functools.lru_cache(maxsize = 3)
    @counter
    def _fibonacci(n):
        if n<2:
            return n
        else:
            return _fibonacci(n - 1) + _fibonacci(n - 2)
    result = _fibonacci(n)
    info = _fibonacci.cache_info()
    return [_fibonacci(n), info]


def add(extra_n=2):
    def _add(function):
        @functools.wraps(function)
        def __add(n):
            return function(n + extra_n)
        return __add
    return _add

def decorator_args_test():
    add(extra_n=4)
    def eggs(n):
        return 'eggs' * n

    print("Decorator with args: ", eggs(2))

def add2(*args, **kwargs):
    default_kwargs = dict(n=1)

    def _add(function):
        @functools.wraps(function)
        def __add(n):
            default_kwargs.update(kwargs)
            return function(n + default_kwargs['n'])
        return __add
    if len(args)==1 and callable(args[0]) and not kwargs:
        return _add(args[0])
    elif not args and kwargs:
        default_kwargs.update(kwargs)
        return _add
    else:
        raise RuntimeError('This decorator only supports keyword arguments')


def decorator_opt_args_test():
    @add2(n=3)
    def spam(n):
        return 'spam' * n
    print("Decorator with optional args: ", spam(8))


class Debug(object):
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        output = self.function(*args, **kwargs)
        print('%s(%r, %r): %r' % (self.function.__name__, args, kwargs, output))
        return output

def decorator_class_test():
    @Debug
    def spam(eggs):
        return "spams" * eggs
    output = spam(3)


#Using property decorators
class Spam(object):

    def get_eggs(self):
        print("Returning ", self._eggs)
        return self.get_eggs

    def set_eggs(self, value):
        print("Adding ", value)
        self._eggs = value

    def delete_eggs(self):
        print("Deleting eggs")
        del self._eggs

    eggs = property(get_eggs, set_eggs, delete_eggs)

    @property
    def spam(self):
        return self._spam

    @spam.setter
    def spam(self, spam):
        self._spam = spam

    @spam.getter
    def spam(self):
        return self._spam

    @spam.deleter
    def spam(self):
        del self._spam

def property_decorator_test():
    spam = Spam()
    spam.eggs = 123
    print(spam.eggs)
    del spam.eggs

# Singleton
def singleton(cls):
    instances = dict()
    @functools.wraps(cls)
    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton

def singleton_test():
    @singleton
    class A:
        def __init__(self):
            print(self)
    a = A()
    b = A()
    print("A is B : ", a is b)

# To change sorted with own implementation of sorting:
def sort_by_attribute(attr, keyfunc=getattr):
    def _sort_by_attribute(cls):
        def __gt__(self, other):
            return getattr(self, attr) > getattr(other, attr)

        def __ge__(self, other):
            return getattr(self, attr) >= getattr(other, attr)

        def __lt__(self, other):
            return getattr(self, attr) < getattr(other, attr)

        def __le__(self, other):
            return getattr(self, attr) <= getattr(other, attr)

        def __eq__(self, other):
            return getattr(self, attr) <= getattr(other, attr)

        cls.__gt__ = __gt__
        cls.__ge__ = __ge__
        cls.__lt__ = __lt__
        cls.__le__ = __le__
        cls.__eq__ = __eq__

        return cls
    return _sort_by_attribute

class Value(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<%s[%d]>' % (self.__class__, self.value)

def value_test():
    @sort_by_attribute('value')
    class Spam(Value):
        pass
    numbers = [4,3,2,5]
    spams = [Spam(n) for n in numbers]
    print("Sorting with decorator" , sorted(spams))

def single_dispatch_test():
    @functools.singledispatch
    def printer(value):
        print('other: %r ' % value)

    @printer.register(str)
    def str_printer(value):
        print(value)

    @printer.register(int)
    def int_printer(value):
        printer('int: %d' % value)

    @printer.register(dict)
    def dict_printer(value):
        printer('dict:')
        for k,v in sorted(value.items()):
            printer('   key: %r, value: %r' % (k,v))
    print("Single dispatch decorator")
    printer('spam')
    printer(1)
    printer([1,2,3])
    printer({'a':1, '2':3})

if __name__ == "__main__":
    decor_debug_test()
    memoize_test()
    print("Trying lru cache: ", lru_test(150))
    decorator_args_test()
    decorator_opt_args_test()
    decorator_class_test()
    property_decorator_test()
    singleton_test()
    value_test()
    single_dispatch_test()
