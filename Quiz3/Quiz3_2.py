# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West) and for a given size greater than 1,
# the number of triangles pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1
#   1 1
#     1
#
# The output lists, for every direction and for every size, the number of triangles
# pointing in that direction and of that size, provided there is at least one such triangle.
# For a given direction, the possble sizes are listed from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles, that is, obtained
# from the latter by ignoring at least one layer, starting from the base.
#
# Written by *** and Eric Martin for COMP9021

'''
实现quiz功能
但是未经优化
时间负责度和代码形式需要尝试优化下
'''

from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def triangles_in_grid():
    dict_of_triangles = {}

    result = get_triangle()
    if result:
        dict_of_triangles.update({'N': [i for i in result]})

    rotate(grid)
    result = get_triangle()
    if result:
        dict_of_triangles.update({'W': [i for i in result]})

    rotate(grid)
    result = get_triangle()
    if result:
        dict_of_triangles.update({'S': [i for i in result]})

    rotate(grid)
    result = get_triangle()
    if result:
        dict_of_triangles.update({'E': [i for i in result]})

    return dict_of_triangles
    # Replace return {} above with your code

def rotate(grid):
    grid[:] = map(list, zip(*grid[::-1]))


# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()


############################################################


def get_triangle():
    result = []
    if dim == 1:
        return
    for _ in range((dim + 1)//2 - 1):
        result.append(0)
    for i in range(0, dim - 1):
        for j in range(1 , dim):
            if grid[i][j] == 0:
                continue
            for a in range(1, (dim + 1)//2):
                if a + i >= len(grid) or a + j >= len(grid) or j - a < 0:
                    break
                if not grid[i + a][j - a: j + a + 1].count(0):
                    result[a-1] += 1
                else:
                    break
    while result.count(0):
        result.remove(0)
    if len(result) == 1:
        result[0] = (2, result[0])
    for i in range(len(result)):
        if i < len(result) - 1:
            result[i] = (i+2, result[i] - result[i + 1])
        if i == len(result) - 1 and i > 0:
            result[i] = (i+2, result[i])
    result = result[::-1]
    return result




############################################################
# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.
triangles = triangles_in_grid()
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')
