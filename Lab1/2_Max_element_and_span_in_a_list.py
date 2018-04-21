'''
Run and study the program max_in_list.py. Then write a program span.py that prompts the user
for a seed for the random number generator, and for a strictly positive number, nb_of_elements,
generates a list of nb_of_elements random integers between 0 and 99, prints out the list, computes
the difference between the largest and smallest values in the list without using the builtins min()
and max(), prints it out, and check that the result is correct using the builtins.
'''
import sys
from random import randint



nb_of_elements = input('Please input the number of elements: ')
try:
    nb_of_elements = int(nb_of_elements)
except ValueError:
    print('Wrong input, try again')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be positive, try again')
    sys.exit()

L = [randint(0,99) for _ in range(nb_of_elements)]

L_max = 0
for e in L:
    if e >= L_max:
        L_max = e

L_min = L_max
for e in L:
    if e <= L_min:
        L_min = e

print(L)
print()
print('max element = ' + str(L_max))
print('min element = ' + str(L_min))

print()
print('Test in max() and min()')
print('max element = ' + str(max(L)))
print('min element = ' + str(min(L)))






