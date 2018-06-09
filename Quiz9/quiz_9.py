# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by Rick Xie z5192747 and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree_adt import *

# Possibly define some functions
L = []

def max_diff_in_consecutive_leaves(tree):
    global L
    get_leaves(tree)
    max_diff = 0
    for i in range(len(L) - 1):
        max_diff = L[i] - L[i + 1] if L[i] - L[i + 1] > max_diff else max_diff
    return max_diff

def get_leaves(tree):
    if tree.right_node.value:
        max_diff_in_consecutive_leaves(tree.right_node)
    if tree.left_node.value:
        max_diff_in_consecutive_leaves(tree.left_node)
    if not tree.left_node.value and not tree.right_node.value:
        L.append(tree.value)

provided_input = input('Enter two integers, the second one being positive: ')
try:
    arg_for_seed, nb_of_nodes = provided_input.split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))


print(L)
