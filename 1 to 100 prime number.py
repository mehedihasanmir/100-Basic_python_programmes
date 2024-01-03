first = 1
last = 100
print(f"prime number between {first} and {last}")
for num in range (first , last+1):
    if num >1:
        for i in range (2,num):
            if num % i == 0:
                break
        else:
            print(num)