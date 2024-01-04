number = int(input("Enter a number: "))
num_string =str(number)
num_digit = len(num_string)
sum_of_power = 0
tem_num = number
while tem_num > 0 :
    digit = tem_num % 10
    sum_of_power += digit ** num_digit
    tem_num = tem_num // 10 
if sum_of_power == number:
    print(f"{number} is  a armstrom number")
else:
    print(f"{number} is not a armstrom number")