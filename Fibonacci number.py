n_tarm = int(input("Enter the term: "))
count = 0
n1 = 0
n2 =1
if n_tarm < 0 :
    print ("this is not valid cause of negative number")
elif n_tarm == 0:
    print("the fibonacci number is 0")
else:
    while count < n_tarm:
        print(n1)
        nth = n1+n2
        n1 =n2
        n2 = nth
        count = count + 1
