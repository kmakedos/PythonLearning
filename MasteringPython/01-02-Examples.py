
# Test a filter and use yield to produce items
def filter(items, f):
    for item in items:
        if f(item) == True:
            yield item

def f(item):
    if (item % 2) == 0:
        return True
    else: return False
#items = range(10)

#for item in filter(items, f):
#    print(item)


# Lists and dicts are NOT re-initialized between calls.
def wrong_args(k, v, dict_ = {}, list_ = []):
    list_.append(v)
    dict_[k] = v
    print("List: %r" % list_)
    print("Dict: %r" % dict_)

wrong_args(k=1,v=2)
wrong_args(k=4,v=5)



# This is correct handling
def ff(k,v,dict_=None, list_=None):
    if list_ is None:
        list_ = []
    if dict_ is None:
        dict_ = {}
    list_.append(v)
    dict_[k] = v

    print("List: %r" % list_)
    print("Dict: %r" % dict_)

ff(k="1", v="2")
ff(k="a", v="3")



# Similarly here this list is not re-initialized when inheriting
class Spam(object):
    a = []

class Bpam(Spam):
    pass

A = Spam()
B = Bpam()
A.a.append(1)
print(A.a, B.a)


# Usage of args and kwargs
def pprol(*args, **kwargs):
    for x in args:
        print(x)
    for y in kwargs:
        print(y)

pprol(1,2,0)

ls = [1,2,4]
for x in ls:
    if x > 3:
        ls.remove(x)
print(ls)
