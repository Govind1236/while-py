def sum_of_even(even):
    
    total_even = 0
    for num in range(2, even + 1, 2):
        total_even += num
    return total_even
even = int(input("Enter number:"))
total_ = sum_of_even(even)
print("The sum of even number",even,"is",total_)