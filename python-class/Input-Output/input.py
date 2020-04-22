#str = input(' Enter Your name: ')
#
#print(str)

#str = input('Enter the number: ')
#x = float(str) # Str is converted into int
#print(x)

#x = float(input('Enter some number: '))
#print(x)

#ch = input('Enter your name: ')
#print("Name starts from  " +ch[0])


#x = int(input('Enter 1st number: '))
#y = int(input('Enter 2nd number: '))

#print("Addition on two number is : ", x + y)


#x = eval(input("Enter an expression: "))
#print("Result:", x)

import sys
n = len(sys.argv)
args = sys.argv
print('No are arguments given: ', n)
print('2nd Argument is  :', args[1])

for a in args:
    print(a)