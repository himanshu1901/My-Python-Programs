
A = int(input("Enter the number: "))
if A > 1:
    for i in range(2, int(A/2)+1):
        if A % i == 0:
            print(f'{A} is not a prime number')
            break
    else:
        print(f'{A} is a prime number')
else:
    print(f'{A} is not a prime number')

