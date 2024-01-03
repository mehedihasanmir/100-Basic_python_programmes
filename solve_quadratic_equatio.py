import math 
a = float(input("Enter cofficient a: "))
b = float(input("Enter cofficient b: "))
c = float(input("Enter cofficient c: "))
discriminent = b**2 - 4*a*c
if discriminent == 0:
    root = -b / (2*a)
    print(f"root {root}")
elif discriminent > 0:
    root1 = (-b + math.sqrt(discriminent)) /(2*a)
    root2 = (-b - math.sqrt(discriminent)) /(2*a)
    print(f"root 1: {root1} \nroot 2 {root2}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminent)) / (2*a)
    print(f"root 1: {real_part} + {imaginary_part}")
    print(f"root 2: {real_part} - {imaginary_part}")
    