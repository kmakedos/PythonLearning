# O Complexity
def o_complexity(n=10):
    print("Creating %d items" % n)
    #alist = list(range(n))
    #adict = dict.fromkeys(range(n))


    def o_1(items):
        # O(1)
        return 1

    def o_n(items):
        # O(N)
        total = 0
        for item in items:
            total += item
        return total

    def o_n2(items):
        # O(N^2)
        prod = 1
        for item in items:
            for item2 in items:
                prod =+ item * item2
        return prod

    items = range(n)

    print("O1 items: " , o_1(items))
    print("ON items: ", o_n(items))
    print("ON2 items: ", o_n2(items))

# Lists
def list_examples(n = 100):
    print("List Examples")
    primes = [1,2,3,5,7]
    print("Primes:" , primes)
    items = []
    for i in range(n):
        items.append(i % 10)
    print("Iteratively print non-primes:")
    nonprimes=[]
    for item in items:
        if item not in primes:
            nonprimes.append(item)
    print(nonprimes[1:5])

    print("\nList comprehensions to find non-primes: ")
    s = [ item for item in items if item not in primes ]
    print(s[1:5])

    print("Lambda filters to find non-primes:")
    l = list(filter(lambda item: item not in primes, items))
    print(l[1:5])

def a_dict_implementation():

    def most_significant(value):
        while value >= 10:
            value //= 10
        return value

    def add(collection, key, value):
        index = most_significant(key)
        collection[index].append((key, value))

    def contains(collection, key):
        index = most_significant(key)
        for k,v in collection[index]:
            if k == key:
                return True
        return False

    collection = [ [], [], [], [], [], [], [], [], [], []]
    add(collection, 123, "kostas")
    add(collection, 342, "mnik")
    add(collection ,453, "sad")
    print("A primitive dict implementation:", collection)
    print("Does it contain number 453? ", contains(collection, 453))

def dict_with_memory_leak(n = 100):
    print("A dict with memory leak")
    d = dict.fromkeys(range(n))
    for x in range(n-1):
        d.pop(x)
    for k,v in d.items():
        print(k,v)

def set_example():
    set1 = set('maolemask')
    set2 = set('kolema')
    print("set1: ", set1)
    print("set2: ", set2)
    print("& common: ", set1 & set2)
    print("| all: ", set1 | set2)
    print("^ uncommon:", set1 ^ set2)
    print("- first not later: ", set1-set2)
    print("> every one in latter is in the first: ", set1 > set2)
    print("> every one in first is also in the latter: ", set1 < set2)

# main callers
o_complexity()
o_complexity(100)
o_complexity(1000)
list_examples(10000000)
a_dict_implementation()
dict_with_memory_leak(100000)
set_example()