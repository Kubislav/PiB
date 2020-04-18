# SOURCE: https://asecuritysite.com/encryption/s3

# TENTO ZDROJ BOL UPRAVENY PRE POTREBY TESTOVANIA

import sys

import timeit
from sys import getsizeof

mycode = ''' 
from hashlib import sha3_224
large_input = bytearray(1_000_000_000)
s = sha3_224()
s.update(large_input)
'''

# KB1 = "x" * 1000
# KB10 = "x" * 10000
# KB100 = "x" * 100000
# MB1 = "x" * 1000000
# MB10 = "x" * 10000000
# MB100 = "x" * 100000000
message = "x"

test_time = (timeit.timeit(stmt=mycode, number=5))
print("Priemerna rychlost hashovania spravy o velkosti: ",
      getsizeof(message), "B", " je ", test_time / 5, " sekúnd")
