
n = int(input("Enter a value: "))

for i in range(2,n):
    if(n % i==0):
        print("number is not prime")
        break
else:
    print(f"Number is prime:{n}")