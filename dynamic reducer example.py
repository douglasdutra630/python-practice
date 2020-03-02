"""
dynamic_reducer([1,2,3],'+')
dynamic_reducer([1,2,3],'-')
dynamic_reducer([1,2,3],'*')
dynamic_reducer([1,2,3],'/')
"""
from functools import reduce
import operator

def dynamic_reducer(collection, op):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    return reduce((lambda var1, var2: operators[op](var1, var2)),collection)

print (dynamic_reducer([1,2,3],'+'))
print (dynamic_reducer([1,2,3],'-'))
print (dynamic_reducer([1,2,3],'*'))
print (dynamic_reducer([1,2,3],'/'))