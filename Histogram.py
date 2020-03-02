"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

sales = {
    'g': 18,
    'f': 38,
    't': 10,
    'o': 12
}

def sales_levels(sales_values):
    for key, value in sales_values.items():
        print  (f'{key} sale: {value * "$"}')

sales_levels(sales)


