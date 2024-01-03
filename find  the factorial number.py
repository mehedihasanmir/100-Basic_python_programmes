number = int(input("Enter a number: "))
factorial = 1
if number < 0 :
    print("factorial doesn't exist in negative number")
elif number ==0:
    print("The factorial number is 0)")
else:
    for i in range (1,number+1):
        factorial = factorial * i 
    print(f"{number}'s factorial is {factorial}")
