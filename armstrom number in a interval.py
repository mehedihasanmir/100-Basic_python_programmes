lower = int(input("Enter your lower number:"))
highest = int(input("Enter your highest number: "))
for number in range(lower,highest+1):
    digit = len(str(number))
    tem_num = number
    sum = 0
    while tem_num > 0:
        last_digit = tem_num % 10
        sum = sum + last_digit ** digit
        tem_num = tem_num // 10
    if number == sum:
        print(number)