print("Enter Number Between 1 to 5")

n=input()
n=int(x)
i=2
while i<n:
    if n%i==0:
        break
i=i+1

if i==n:
    print("prime number")
else:
    print("not prime")