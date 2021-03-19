n=int(input("Enter the number: "))
for i in range(2,n):
    if n%i==0:
        break
else:
    print("Number is prime")
if i!=(n-1):
    print("Number is not prime")
    
