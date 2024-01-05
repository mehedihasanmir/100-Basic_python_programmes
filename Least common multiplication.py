def count_LMC(num1,num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    value = greater
    while (True):
        if ((greater % num1 == 0)and (greater % num2 == 0)):
            print(f"The least common value of {num1} and {num2} is {greater}")
            break
        else:
            greater = greater + value
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
count_LMC(num1,num2)