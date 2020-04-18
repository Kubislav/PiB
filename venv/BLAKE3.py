# SOURCE: https://pypi.org/project/blake3/

# TENTO ZDROJ BOL UPRAVENY PRE POTREBY TESTOVANIA


import timeit
from sys import getsizeof

mycode = ''' 
from blake3 import blake3
test_message = bytearray(1_000_000_000)
hash = blake3(test_message).hexdigest()
'''
# hash = blake3(large_input, multithreading=True).hexdigest()
# KB1 = "x" * 1000
# KB10 = "x" * 10000
# KB100 = "x" * 100000
# MB1 = "x" * 1000000
# MB10 = "x" * 10000000
# MB100 = "x" * 100000000

test_message = bytearray(1_000_000_000)

test_time = (timeit.timeit(stmt=mycode, number=5))
print("Priemerna rychlost hashovania spravy o velkosti: ",
      getsizeof(test_message), "B", " je ", test_time / 5, " sekúnd")
