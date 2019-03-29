import functools

def f(x,y):
    return x * y

mult = functools.partial(f, 2)

print(mult(3))
print(mult(4))
