import functools

@functools.singledispatch
def pack_file(f):
    print('Packing unknown')

@pack_file.register(str)
def pack_file_str(f):
   print("Packing str file")

@pack_file.register(int)
def pack_file_int(f):
    print("Packing int file")


pack_file("s")
pack_file(2.3)
pack_file(3)
