python3 -m timeit '"".join(str(i) for i in range(10000))'
python2 -m timeit '"".join(str(i) for i in range(10000))'
pypy -m timeit '"".join(str(i) for i in range(10000))'


python3 -m timeit 'x=[]; [x.insert(0, i) for i in range(10000)]'
python3 -m timeit 'x=[]; [x.append(i) for i in range(10000)]'
python3 -m timeit 'x=[i for i in range(10000)]'
python3 -m timeit 'x=list(range(10000))'


python3 -m cProfile -s calls test_fibonacci.py no_cache

#pyprof2calltree -i pystone.profile -o pystone.callgrind
#writing converted data to: pystone.callgrind
# qcachegrind pystone.callgrind


pip install line_profiler
kernprof -l test_primes.py

python3 -m line_profiler test_primes.py.lprof


# General guidelines

# - Try versus if
# - Generators vs Lists
# - Recreating Collections!!
# - LRU Cache
# - Redis
# - numpy, pandas, scipy, sklearn
# - JIT numba

# Memory consumption
import tracemalloc
if __name__ == '__main__':
tracemalloc.start()
# Reserve some memory
x = list(range(1000000))
# Import some modules
import os
import sys
import asyncio
# Take a snapshot to calculate the memory usage
snapshot = tracemalloc.take_snapshot()
for statistic in snapshot.statistics('lineno')[:10]:
print(statistic)

# Also memory profiler
import memory_profiler
@memory_profiler.profile
def main():
n = 100000
a = [i for i in range(n)]
b = [i for i in range(n)]
c = list(range(n))
d = list(range(n))
e = dict.fromkeys(a, b)
f = dict.fromkeys(c, d)
if __name__ == '__main__':
main()

 # gc collector !! in long running scripts


 # Memory in Python
#There are four concepts which you need to know about within the Python memory
#manager:
#• First we have the heap. The heap is the collection of all Python managed
#memory. Note that this is separate from the regular heap and mixing the two
#could result in corrupt memory and crashes.
#• Second are the arenas. These are the chunks that Python requests from the
#system. These chunks have a fixed size of 256 KiB each and they are the
#objects that make up the heap.
#• Third we have the pools. These are the chunks of memory that make up the
#arenas. These chunks are 4 KiB each. Since the pools and arenas have fixed
#sizes, they are simple arrays.
#• Fourth and last, we have the blocks. The Python objects get stored within
#these and every block has a specific format depending on the data type. Since
#an integer takes up more space than a character, for efficiency a different
#block size is used.