
a = 10
print(id(a))

def variable():
    a = 9
    x = globals()['a']
    print(id(x))
    print("Inside Function", a) # changing Global Variables

    globals()['a'] = 25

variable()

print("Outside Function" ,a)