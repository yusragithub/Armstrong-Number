def armstrong_number(num):
    str_num = str(num)
    num_digits = len(str_num)
    power_sum = 0
    for digit in str_num:
        power_sum += int(digit) ** num_digits
        return power_sum == num
user_input = int(input("Enter a number: "))
if (user_input < 0) :
    print("Please enter a positive number.")
elif (armstrong_number(user_input)) :
    print(user_input, "is an armstrong number.")
else :
    print(user_input, "is not an armstrong number.")
