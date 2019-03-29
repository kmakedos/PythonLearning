def square(n):
    '''
    Returns the input number, squared
    >>> square(0)
    0
    >>> square(2)
    4
    >>> square(-4)
    16
    >>> square()
    Traceback (most recent call last):
    ...
    TypeError: square() missing 1 required positional argument: 'n'
    '''
    return n * n

if __name__ == "__main__":
    import doctest
    doctest.testmod()