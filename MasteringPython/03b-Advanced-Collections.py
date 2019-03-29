import collections
# Chain of dictionaries
def chainmaps():
    print("Example of usage of chain of dictionaries")
    print("We can use collections.ChainMap to chain together dictionaries")
    import argparse
    defaults = {
        'file': 'config.txt',
        'port': '8080'
    }

    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    parser.add_argument('--port')
    args = vars(parser.parse_args())


    filtered_args = {k: v for k,v in args.items() if v}
    combined = collections.ChainMap(filtered_args, defaults)

    print(combined['file'])
    print(combined['port'])


def counter_test():
    print("Counter is used among others to quickly find most common items even in a million range list")
    import math
    counter = collections.Counter()
    for i in range(1000000):
        counter[math.sqrt(i) // 25] += 1
    print("Most common 5 elements in a 1M items list, it should execute in 1\"")
    for k,v in counter.most_common(5):
        print("%s, %d " % (k,v))


def deque_test():
    print("The double ended queue is a double linked list, ideal for stack/queue purposes")
    dq = collections.deque()
    for x in range(10):
        dq.append(x)
    print("Queue at start: ",dq)
    dq.pop()
    print("Queue after a pop: ",dq)
    dq.popleft()
    print("Queue after another pop", dq)
    dq.append(dq.popleft())
    print("Queue after last pop", dq)

def defaultdict_test():
    import json
    print("Dictionaries with default values")
    nodes = [
        ('a', 'b'),
        ('c', 'd'),
        ('a', 'c'),
        ('c', 'b')
    ]
    dd = collections.defaultdict(list)
    for orig,dest in nodes:
        dd[orig].append(dest)
    print("Original relations", nodes)
    print("After an assignment to default dict", dd)

    di = collections.defaultdict(int)
    di['kostas'] = 1
    di['viktor'] =+ 2
    print("after some assignments:", di)
    print("And an example with a tree generated on the fly")
    def tree():
        return collections.defaultdict(tree)

    genealogic = tree()

    genealogic['kostas']['son'] = ('viktor')
    genealogic['viktor']['father'] = ('kostas')

    genealogic['iason']['father'] = ('kostas')
    genealogic['kostas']['son'] = ('iason')
    print("A json with default values generated")
    print(json.dumps(genealogic, sort_keys=True, indent=4))

def ordered_dict_test():
    import collections
    spam = collections.OrderedDict()
    spam['b'] = 3
    spam['c'] = 4
    spam['a'] = 5
    print("Ordered dict: ", spam)


def enum_test():
    import enum
    class Animals(enum.Enum):
        race = 0
        color = 1
        muppet = 2
    print("Enums test: " , Animals.race)

def heapq_test():
    import heapq
    ls = [1,2,5,8,3,3,5,4,6]
    hq = heapq.heapify(ls)
    print("Heap Q is used in ordered dict, returning smallest or largest item from list: ")
    while ls:
        print(heapq.heappop(ls), ls)
    print("HeapQ creates a heap tree for holding the list, with smallest element on top")
    print("But searching in it is very costly")


def bisect_test(n=15):
    import bisect
    import random
    ls = []
    for x in range(n):
        ls.append(random.randint(0,10))
    ls.sort()
    print("Bisect is a way to keep a list always sorted", ls)
    print("Bisect is much faster on finding items: ", bisect.bisect_left(ls,n/2+1))



# Main callers
print("An ordered dict example is needed ")
chainmaps()
counter_test()
deque_test()
defaultdict_test()
ordered_dict_test()
enum_test()
heapq_test()
bisect_test()