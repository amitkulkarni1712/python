num=int(input("Enter Number to check if it is prime number or  not:"))

if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num, "IS Not a Prime Number")
            break
    else:
        print(num,"Is a Prime number")
else:
    print(num, "Is not a prime number out of loop")