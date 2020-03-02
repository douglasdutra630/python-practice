#lists

tags = ['python', 'development', 'tutorials', 'code']

print (tags)

tags.sort()

print(tags)

tags.sort(reverse=True)

print(tags)

totals = [123, 234, 354, 8876]

totals.sort()

print(totals)

totals.sort(reverse=True)
print(totals)
#spli
uri = 'https://www.google.com/search?q='

tags = ['python', 'development', 'tutorial']

formatted_tags = "+".join(tags)

print (formatted_tags)

query_uri = f'{uri}{formatted_tags}'

print (query_uri)

tag_range = tags[1:2]
# changing list order by index
name = 'doug'

reverse_lenght = len(name)
sliced_string = name[reverse_lenght::-1]
print (sliced_string)

tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming',
    'computer science'
]

tag_range = tags [::-1]

print(tag_range)

#list median/mean
"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""
import math

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

def mean_finder():
    list_sum = 0
    for y in sale_prices:
        for x in sale_prices:
            x = len(sale_prices)
        list_sum += y
        mean = list_sum / x
    return mean

print(mean_finder())

def median_finder():
    sale_prices.sort()
    median = (sale_prices[4])
    return median

print(median_finder())

#jordan's answer
sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
j_median = sorted_list[half_slice:(half_slice + 1)]

print(j_median)
tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

print(tags[1:4:2])

slice_obj = slice(1, 4, 2)

print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)

print(tags[slice_obj])


