def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst=[1,3,54,767,45,76,34,76,87,97,43,55]
even ,odd = count(lst)
print("even" ,even)
print("Odd" , odd)