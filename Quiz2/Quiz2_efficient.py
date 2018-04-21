# Written by *** and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
from decimal import  *
from math import *


try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''

# Replace this comment with your code

sim_n = numerator // gcd(numerator, denominator)
sim_d = denominator // gcd(numerator, denominator)
sim_d2 = denominator // gcd(numerator, denominator)
sim_d3 = denominator // gcd(numerator, denominator)

integral_part = sim_n // sim_d

count_2_5 = 0
while not sim_d2 % 2:
    count_2_5 += 1
    sim_d2 = sim_d2 // 2
while not sim_d2 % 5:
    count_2_5 += 1
    sim_d2 =sim_d2 // 5

if sim_d2 == 1:
    has_finite_expansion = True

quotient = list(str(Decimal(sim_n) / Decimal(sim_d3) - sim_n // sim_d3))

count = 0
while count_2_5>= 1:
    sim_n *= 10
    count += 1
    if not sim_d3 % 2:
        sim_d3 = sim_d3 // 2
        count_2_5 -= 1
    if not sim_d3 % 5:
        sim_d3 = sim_d3 // 5
        count_2_5 -= 1

if quotient == ['0']:
    sigma = ''
else:
    sigma_string = [str(i) for i in quotient[quotient.index('.')+ 1 : quotient.index('.') + count + 1]]
    sigma = ''.join(sigma_string)

if not has_finite_expansion:
    quotient_1 = quotient[quotient.index('.') + count + 1:]
    quotient_1 = [int(x) for x in quotient_1]
    quotient_1_set = set(quotient_1[:len(quotient_1)-2])
    for i in range(0, (len(quotient_1))):
        tau_1 = quotient_1[0: i + 1]
        tau_2 = quotient_1[i + 1: 2 * i + 2]
        if tau_1 == tau_2 and set(tau_1) == quotient_1_set:
            tau_str = [str(i) for i in quotient_1[0: i + 1]]
            tau = ''.join(tau_str)
            break
        else:
            tau = ''

# Replace this comment with your code

if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')

