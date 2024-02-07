def add_numbers(num, num1):
    sum_of_numbers = num + num1
    return sum_of_numbers

def multipy_num(num , num1):
    multiple_ = num * num1
    return multiple_


num2 = int(input("Enter a number: "))
num1 = int(input("Enter a second number: "))
multiple_ = multipy_num(num2, num1)
sum_of_numbers = add_numbers(num2,num1)
print(f"The sum of {num2} and {num1} is:", sum_of_numbers)
print(f"The multiple of {num2} and {num1} is:", multiple_)

