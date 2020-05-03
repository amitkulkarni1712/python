def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('Amit', age=32, city='Pune', mob=1234567)
