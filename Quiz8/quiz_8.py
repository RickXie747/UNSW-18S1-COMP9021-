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
from collections import defaultdict

from queue_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def leftmost_longest_path_from_top_left_corner():
    if grid[0][0] == 0:
        return False
    find_path(0, 0)
    queue.enqueue('00 ')
    final_position = ''
    while not queue.is_empty():
        position = queue.dequeue()
        final_position = compare_path(position, final_position)
        if position[-3: -1] in path_dict:
            for i in range(len(path_dict[position[-3: -1]]), 0, -3):
                if path_dict[position[-3: -1]][i - 3: i] not in position:
                    queue.enqueue(position + path_dict[position[-3: -1]][i - 3: i])
    path = []
    for i in range(len(final_position) // 3):
        path.append((int(final_position[3 * i]), int(final_position[3 * i + 1])))
    return path


def find_path(a, b):
    path_dict[f'{a}{b}'] = '' if f'{a}{b}' not in path_dict else path_dict[f'{a}{b}']
    if b != 9:
        if grid[a][b + 1] and f'{a}{b + 1}' not in path_dict[f'{a}{b}']:
            path_dict[f'{a}{b}'] += f'{a}{b + 1} '
            find_path(a, b + 1)
    if a != 9:
        if grid[a + 1][b] and f'{a + 1}{b}' not in path_dict[f'{a}{b}']:
            path_dict[f'{a}{b}'] += f'{a + 1}{b} '
            find_path(a + 1, b)
    if b != 0:
        if grid[a][b - 1] and f'{a}{b - 1}' not in path_dict[f'{a}{b}']:
            path_dict[f'{a}{b}'] += f'{a}{b - 1} '
            find_path(a, b - 1)
    if a != 0:
        if grid[a - 1][b] and f'{a - 1}{b}' not in path_dict[f'{a}{b}']:
            path_dict[f'{a}{b}'] += f'{a - 1}{b} '
            find_path(a - 1, b)

def compare_path(a, b):
    if len(a) > len(b):
        return a
    if len(a) < len(b):
        return b
    else:
        a_priority = 1
        b_priority = 1  # highest to lowest: 3 - 2 - 1 which are left straight right
        for i in range(len(a) // 3):
            if a[3 * i: 3 * i + 2] != b[3 * i: 3 * i + 2]:
                index = i
                break
        if index == 1:
            if a[3:5] == '01':
                return a
            else:
                return b
        if int(a[(index - 1) * 3: (index - 1) * 3 + 2]) - int(a[(index - 2) * 3: (index - 2) * 3 + 2]) == 1:
            # former direction is E
            if int(a[index * 3: index * 3 + 2]) - int(a[(index - 1) * 3: (index - 1) * 3 + 2]) == 1:
                a_priority = 2 # Now direction is E, which is straight
            if int(a[index * 3: index * 3 + 2]) - int(a[(index - 1) * 3: (index - 1) * 3 + 2]) == 10:
                a_priority = 1 # Now direction is S, which is right
            if int(a[index * 3: index * 3 + 2]) - int(a[(index - 1) * 3: (index - 1) * 3 + 2]) == -10:
                a_priority = 3 # Now direction is N, which is left
        if int(a[(index - 1) * 3: (index - 1) * 3 + 2]) - int(a[(index - 2) * 3: (index - 2) * 3 + 2]) == -1:
            # former direction is W
            if int(a[index * 3: index * 3 + 2]) - int(a[(index - 1) * 3: (index - 1) * 3 + 2]) == -1:
                a_priority = 2 # Now direction is W, which is straight
            if int(a[index * 3: index * 3 + 2]) - int(a[(index - 1) * 3: (index - 1) * 3 + 2]) == 10:
                a_priority = 3 # Now direction is S, which is left
            if int(a[index * 3: index * 3 + 2]) - int(a[(index - 1) * 3: (index - 1) * 3 + 2]) == -10:
                a_priority = 1 # Now direction is N, which is right
        if int(a[(index - 1) * 3: (index - 1) * 3 + 2]) - int(a[(index - 2) * 3: (index - 2) * 3 + 2]) == 10:
            # former direction is S
            if int(a[index * 3: index * 3 + 2]) - int(a[(index - 1) * 3: (index - 1) * 3 + 2]) == -1:
                a_priority = 1 # Now direction is W, which is right
            if int(a[index * 3: index * 3 + 2]) - int(a[(index - 1) * 3: (index - 1) * 3 + 2]) == 10:
                a_priority = 2 # Now direction is S, which is straight
            if int(a[index * 3: index * 3 + 2]) - int(a[(index - 1) * 3: (index - 1) * 3 + 2]) == 1:
                a_priority = 3 # Now direction is E, which is left
        if int(a[(index - 1) * 3: (index - 1) * 3 + 2]) - int(a[(index - 2) * 3: (index - 2) * 3 + 2]) == -10:
            # former direction is N
            if int(a[index * 3: index * 3 + 2]) - int(a[(index - 1) * 3: (index - 1) * 3 + 2]) == -1:
                a_priority = 3 # Now direction is W, which is left
            if int(a[index * 3: index * 3 + 2]) - int(a[(index - 1) * 3: (index - 1) * 3 + 2]) == -10:
                a_priority = 2 # Now direction is N, which is straight
            if int(a[index * 3: index * 3 + 2]) - int(a[(index - 1) * 3: (index - 1) * 3 + 2]) == 1:
                a_priority = 1 # Now direction is E, which is right

        if int(b[(index - 1) * 3: (index - 1) * 3 + 2]) - int(b[(index - 2) * 3: (index - 2) * 3 + 2]) == 1:
            # former direction is E
            if int(b[index * 3: index * 3 + 2]) - int(b[(index - 1) * 3: (index - 1) * 3 + 2]) == 1:
                b_priority = 2 # Now direction is E, which is straight
            if int(b[index * 3: index * 3 + 2]) - int(b[(index - 1) * 3: (index - 1) * 3 + 2]) == 10:
                b_priority = 1 # Now direction is S, which is right
            if int(b[index * 3: index * 3 + 2]) - int(b[(index - 1) * 3: (index - 1) * 3 + 2]) == -10:
                b_priority = 3 # Now direction is N, which is left
        if int(b[(index - 1) * 3: (index - 1) * 3 + 2]) - int(b[(index - 2) * 3: (index - 2) * 3 + 2]) == -1:
            # former direction is W
            if int(b[index * 3: index * 3 + 2]) - int(b[(index - 1) * 3: (index - 1) * 3 + 2]) == -1:
                b_priority = 2 # Now direction is W, which is straight
            if int(b[index * 3: index * 3 + 2]) - int(b[(index - 1) * 3: (index - 1) * 3 + 2]) == 10:
                b_priority = 3 # Now direction is S, which is left
            if int(b[index * 3: index * 3 + 2]) - int(b[(index - 1) * 3: (index - 1) * 3 + 2]) == -10:
                b_priority = 1 # Now direction is N, which is right
        if int(b[(index - 1) * 3: (index - 1) * 3 + 2]) - int(b[(index - 2) * 3: (index - 2) * 3 + 2]) == 10:
            # former direction is S
            if int(b[index * 3: index * 3 + 2]) - int(b[(index - 1) * 3: (index - 1) * 3 + 2]) == -1:
                b_priority = 1 # Now direction is W, which is right
            if int(b[index * 3: index * 3 + 2]) - int(b[(index - 1) * 3: (index - 1) * 3 + 2]) == 10:
                b_priority = 2 # Now direction is S, which is straight
            if int(b[index * 3: index * 3 + 2]) - int(b[(index - 1) * 3: (index - 1) * 3 + 2]) == 1:
                b_priority = 3 # Now direction is E, which is left
        if int(b[(index - 1) * 3: (index - 1) * 3 + 2]) - int(b[(index - 2) * 3: (index - 2) * 3 + 2]) == -10:
            # former direction is N
            if int(b[index * 3: index * 3 + 2]) - int(b[(index - 1) * 3: (index - 1) * 3 + 2]) == -1:
                b_priority = 3 # Now direction is W, which is left
            if int(b[index * 3: index * 3 + 2]) - int(b[(index - 1) * 3: (index - 1) * 3 + 2]) == -10:
                b_priority = 2 # Now direction is N, which is straight
            if int(b[index * 3: index * 3 + 2]) - int(b[(index - 1) * 3: (index - 1) * 3 + 2]) == 1:
                b_priority = 1 # Now direction is E, which is right
    if a_priority > b_priority:
        return a
    else:
        return b

path_dict = defaultdict()
queue = Queue()
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