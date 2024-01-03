year = int(input("Enter a year"))
if (year % 400 == 0) and (year % 100 == 0):
    print(year," is Leep Year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year," is Leep year")
else:
    print(year," is not Leep year")