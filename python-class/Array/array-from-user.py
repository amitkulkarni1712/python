from array import *
arr = array('i', []) # Taking a blank array


n = int(input("Enter the length of the Array : "))

for i in range(n):
    x = int(input("Enter Next vale: "))
    arr.append(x)
print(arr)

#### Find the index number of input value
val = int(input("Enter value to search: "))
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k=k+1


