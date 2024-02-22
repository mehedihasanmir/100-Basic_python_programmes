first = int(input("Enter the first number of the range: "))
last = int(input("Enter the last nuber of the range: "))
sum = 0
for num in range(first,last+1):
    if num >1:
        for i in range(2,num):
            if num % i ==0:
                break
        else:
            sum = sum + num
print(f"The sum of prime number from {first} to {last} is {sum}")            