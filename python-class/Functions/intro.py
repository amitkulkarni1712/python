#def add_sub(x , y):
#    c = x + y
#    d = x - y
#    return c,d
#result1, result2 = add_sub(23,67)
#print(result1, result2)

"""
def update(x):
    x = 10
    print(x)

a = 20
update(a)
print(a)
"""
"""
def person(name,age=18):
    print(name)
    print(age)

person('Amit')
"""
def sum(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)
sum(1,2,3,4,5)