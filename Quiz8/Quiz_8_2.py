# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

from queue_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))


def leftmost_longest_path_from_top_left_corner():
    path = []
    a, b = 0, 0
    over = False
    if grid[0][0] == 0:
        return False
    path.append((0, 0))
    while not over:
        over = True
        if grid[a + 1][b] and a < 9 and (a + 1, b) not in path:
            a += 1
            over = False
            path.append((a, b))
        if grid[a][b + 1] and b < 9 and (a, b + 1) not in path:
            b += 1
            over = False
            path.append((a, b))
        if grid[a - 1][b] and a > 0 and (a - 1, b) not in path:
            a -= 1
            over = False
            path.append((a, b))
        if grid[a][b - 1] and b > 0 and (a, b - 1) not in path:
            b -= 1
            over = False
            path.append((a, b))
    return path


# Replace pass above with your code

provided_input = input('Enter one integer: ')
try:
    for_seed = int(provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {path})')

