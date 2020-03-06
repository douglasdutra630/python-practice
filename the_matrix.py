import numpy as np

def solution_one():
    x = np.zeros((5,5))
    print("Original array:")
    print(x)
    x += np.arange(5)
    print(x)

#solution_one()


def should_be_doing_mongo():
    for i in range(0,5):
        x = (i + 1)
    
    solution = [[x] * 5 for x in range(5)]
    print(solution)

should_be_doing_mongo()

#Ryan's solution

def manual_matrix(gird_area):
    matrix = []
    counter = 0

    while counter < gird_area:
        matrix.append([x for x in range(counter, gird_area + counter += 1)])

    return matrix

print(manual_matrix(5))