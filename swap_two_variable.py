a = input("Enter the first variable (a): ")
b = input("Enter the second variavle (b): ")
print(f"orginal number a = {a} and b = {b}")
# another variable is a temporary variable.
another = a 
a = b
b = another
print(f"swap variavle a = {a} b = {b}")