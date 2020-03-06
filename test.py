#Random Hexadecimal
import random

def hex_maker():
    random_hex = (str(random.choice("0123456789ABCDEF")) + str(random.choice("0123456789ABCDEF"))) * 4
    print(f"Random Hex: #{random_hex}")

hex_maker()

#Hyphen String Sorter

color_wheel = 'green-red-black-white'

def string_sort():
    colors = [ color for color in color_wheel.split('-')]
    colors.sort()
    print('-'.join(colors))

string_sort()