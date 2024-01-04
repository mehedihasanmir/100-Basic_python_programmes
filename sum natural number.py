number1 = int(input("Enter the first number: "))
number2 = int(input("Entr the second number: "))
sum = 0
for i in range(number1,number2+1):
    sum = sum + i
print(f"Total additional value is {sum}")