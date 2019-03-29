def list_comprehensions_test():
    squares = [ x*x for x in range(10)]
    print("List comprehension squares: ", squares)

def dict_comprehensions_test():
    sq = {x:x ** 2 for x in range(10) if x %2}
    print("Dict comprehensions: ", sq)

def set_comprehensions_test():
    sets = [ x*y for x in range(3) for y in range(3)]
    print("Sets comprehension:", sets)

class Sp:
    def __init__(self):
        self.ls = []
        self.so = lambda: sorted(self.ls)
def lambda_test():
    s = Sp()
    s.ls.append(2)
    s.ls.append(3)
    s.ls.append(8)
    s.ls.append(0)
    print("Without sorting:", s.ls)

    print("Sorting :", s.so())

def functools_partial_test():
    print("Instead of callling heappush")
    import heapq
    heap = []
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 4)
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 6)
    print(heapq.nsmallest(3, heap))
    print("We use functools to call partially a function")
    import functools
    push = functools.partial(heapq.heappush, heap)
    push(0)
    push(2)
    push(11)

def functoools_reduce_test():
    print("Reduces operates based on first two operands and using the result operates on third etc.")
    import operator
    import functools
    print("Result of factorial up to 6 :", functools.reduce(operator.mul, range(1,6)))
    print("Essentially doing something like this f(f(f(1,2),3),4)")

def functools_reduce_tree_test():
    import json
    import functools
    import collections

    def tree():
        return collections.defaultdict(tree)

    taxonomy = tree()
    print()
    print("A simple tree: ")
    reptilia = taxonomy['Beverage']['Drinks']['Bar Drinks']
    reptilia['Alcoholic'] = ['Vodka', 'Whiskey', 'Wine']
    reptilia['Soft Drinks'] = ['Coca Cola', 'Fanta', 'Sprite']
    print(json.dumps(taxonomy, indent=4))
    path = "Beverage.Drinks.Bar Drinks".split('.')
    print("Path:", path)
    fam = functools.reduce(lambda a,b: a[b], path, taxonomy)
    print(fam.items())

def iter_tools_accu_test():
    import operator
    import itertools
    print()
    print("Iter tools accumulate")
    semesters = [100, 120, 40, 110]
    print("Q profits: ", semesters)
    print("Accumulated values: ", list(itertools.accumulate(semesters, operator.add)))

def iter_tools_chain_combi_test():
    import itertools
    Q2017 = [10,20,40,22]
    Q2018 = [30,40,2,43]
    acc = list(itertools.chain(Q2017, Q2018))
    print("Q2017: ",Q2017)
    print("Q2018: ",Q2018)
    print("Itertools chained for Q2017 and Q2018:", acc)
    print("Combinations of 0..3 by 2: ", list(itertools.combinations(range(3), 2)))
    print("Combinations of 0..3 by 2 with replacement: ", list(itertools.combinations_with_replacement(range(3), 2)))
    def powerset(iterable):
        return itertools.chain.from_iterable(
            itertools.combinations(iterable, i)
            for i in range(len(iterable) + 1) # Cool way to write list comprehension?
        )
    print("Powerset of 3", list(powerset(range(3))))

    print("Permutations:", list(itertools.permutations(range(3),2 )))

def iter_tools_selecting_items_test():
    import itertools
    print("Compress using a set of bools (to select 2-5th element):", list(itertools.compress(range(10), [0,1,1,1,1,0])))
    print("Dropwhile to wait for a certain response:", list(itertools.dropwhile(lambda x: x<10, range(11))))
    print("Takewhile to run until a certain response:", list(itertools.takewhile(lambda x: x<10, range(11))))
    print("Count function that runs until eternity, we zip it with a range to be limited: ")
    for a,b in zip(range(3), itertools.count()):
        print(a,b)

def iter_tools_grouping_test():
    import itertools
    items = [('a', 1), ('a', 2), ('b', 1), ('b', 2)]
    print("Grouping by first element in following tuple list:", items)
    for group,items in itertools.groupby(items, lambda x: x[0]):
        print('%s:%s' % (group, [ v for k,v in items]))

    print("Iter tools do not have slice capabilities because they use generators")
    print("Instead we can use islice")
    ls = list(itertools.islice(itertools.count(), 2,7))
    print(ls)
if __name__ == "__main__":
    list_comprehensions_test()
    dict_comprehensions_test()
    set_comprehensions_test()
    lambda_test()
    functools_partial_test()
    functoools_reduce_test()
    functools_reduce_tree_test()
    iter_tools_accu_test()
    iter_tools_chain_combi_test()
    iter_tools_selecting_items_test()
    iter_tools_grouping_test()