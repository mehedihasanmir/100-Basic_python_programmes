def count_LMC(a,b):
    if a > b:
        greater = a
    else:
        greater = b
    while (True):
        if ((greater % a == 0)and (greater % b)):
            LCM = greater
            break
        greater +=1
    return LCM
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The least common multiplication",count_LMC(num1,num2))
