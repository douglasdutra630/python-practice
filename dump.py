# challenge 1
# use len to add up index of string > create function
string = 'This is my string'

def how_long():
    print(len(string))

how_long()

# challenge 2
# add first > add second > add third > function to print result
string1 = 'the '
string2 = 'shaggy '
string3 = 'dog'

def add_string():
    print(string1 + string2 + string3)

add_string()

# challenge 3
# use variable "str" >  add last letter > add all letter between first and last > add first letter
str ="The dog"
def new_str():
    print(str[-1:] + str[1:-1] + str[:1])

new_str()

# challenge 4
# establish the total as 0 > extablish for/in x and list > add sum of x and total > make a function to complete action
num = [1, 2, 3, 4, 5]

def sum(num):
    total = 0
    for x in num:
        total += x
    print(total)

sum(num)

# challenge 5
# find the lenght of the strings > establish the longest > use for/in to create a function
words = ['short', 'long', 'disestablishment']

def long_ass_word():
    print(max(len(lenght) for lenght in words))

long_ass_word()
# correct solution
def return_longest(words):
  longest_word = words[0]

  for word in words:
    if len(word) > len(longest_word):
      longest_word = word

  return f"""
  Longest Word: {longest_word}
  Length: {len(longest_word)}
  """.strip()

print(return_longest(words))

# challenge 6
my_string = "racecar driver"
replace_value = my_string[0]
modified_string = my_string.replace(replace_value, "$")

print (replace_value + modified_string[1:])

# hard way (challenge 6)
def custom_split(string):
  return [char for char in string]

def character_replace(string):
  split_list = custom_split(string)
  second_list = split_list[1:]

  for letter in second_list:
    if letter == split_list[0]:
      idx = second_list.index(letter)
      second_list[idx] = "$"

  return f'{split_list[0]}{"".join(second_list)}'


print(character_replace("retrofitter"))

# alphabetical order
string= 'the quick brown fox jumps over the lazy dog'

def organize(string):
    return "".join(sorted(string)).strip()
    
print (organize(string))

# manual exponent /My Result/ Jordan's result
num = 2
iteration = 3
list = ([num] * iteration)

def multiply_list (list):
    result = 1
    for x in list:
        result *= x
    return result

print(multiply_list(list))

num = 10
iteration = 2
list = ([num] * iteration)

def multiply_list2 (list):
    result = 1
    for x in list:
        result *= x
    return result

print(multiply_list(list))

#Jordan's Solution
from functools import reduce

def manual_exponent (num, exp):
    computed_list = [num] * exp
    return (reduce(lambda total, element: total * element, computed_list))

print (manual_exponent(2,3))
print (manual_exponent(10,2))

# name reversalt
name_field = 'Test'

def name_reversal ():
    reversed_name =''.join(reversed(name_field))
    if len(name_field) >= 1:
        return reversed_name

print(name_reversal())

name = 'Doug'

reversed_string = ''.join(reversed(name))
print(reversed_string)

#qap.dev - testautomationu.com

def add(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    raise ValueError()

# Input, output, oracle
def test_add_even_numbers():
    assert add(x=1, y=2) == 3


def test_add_whatever():
    assert add(x='foo ', y=None) == 'foo'

print(test_add_whatever())


def heading_generator(heading, i):
    if i <= 6 and i > 0:
        return f'<h{i}>{heading}</h{i}>'
    else:
        return "Error. Headings range from 1-6 in HTML."
print(heading_generator('Greeting', 1))
print(heading_generator('Hi There', 3))
print(heading_generator('Hi There', 9))

age = 27

if age < 25:
    print(f"You're too damn young")
elif age == 27:
    print("Do not buy any white lighters. EVER!")
elif age > 50:
    print(f"You're too damn old")
else:
    print(f"Welcome!")

print(age)

# Ternary Operator

role = 'guest'
auth = 'can access' if role == 'admin' else 'fuck off'

print(auth)