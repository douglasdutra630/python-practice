# List Comprehension

num_list = range (1, 11)
cubed_nums = []

for num in num_list:
    cubed_nums.append(num ** 3)

print(cubed_nums)
#-------------------------------------------------
cubed_nums = [num ** 3 for num in num_list]
#              Action > Loop 
print(cubed_nums)



num_list = range (1, 11)

even_numbers = []

for num in num_list:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)
# ---------------------------------------------------------
even_numbers = [num for num in num_list if num % 2 == 0]
#               Action > Loop           > Conditional
print(even_numbers)


num_list = range (1, 26)

odds = [num for num in num_list if num % 2 != 0]
#       Action > Loop           > Conditional
print (odds)