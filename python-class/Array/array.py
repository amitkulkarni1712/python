from array import *

vals = array('i', [5,6,9,34,67,69,34,32])

for i in range(len(vals)):
    print(vals[i])



print(vals.buffer_info())
print(vals.typecode)

newArray = array(vals.typecode, (a*a for a in vals))

for i in newArray:
    print(i)
