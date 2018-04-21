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
sim_n1 = numerator // gcd(numerator, denominator)
sim_d = denominator // gcd(numerator, denominator)
sim_d2 = denominator // gcd(numerator, denominator)
sim_d3 = denominator // gcd(numerator, denominator)

integral_part = sim_n // sim_d

def get_prime(n):
    l = []
    for _ in range(2, n + 1):
        while not n % _:
            l.append(_)
            n = n // _
    return l

'''
以上这段 将n不断分解的过程，可能无法跑出结果（e.g. Quiz2 TestCase13 n = 99999900000 过大 ）
'''

L = get_prime(sim_d2)
print(L)

L_1 = list(set(L))
try:
    L_1.remove(2)
except ValueError:
    pass
try:
    L_1.remove(5)
except ValueError:
    pass

print(L_1)

if not len(L_1):
    has_finite_expansion = True

float(sim_n),float(sim_d)
count = 0

print(Decimal(sim_n1) / Decimal(sim_d3) - sim_n1 // sim_d3)
quotient = list(str(Decimal(sim_n1) / Decimal(sim_d3) - sim_n1 // sim_d3))
print(f'QUO = {quotient}')

while L.count(2) >= 1 or L.count(5) >= 1:
    sim_n1 *= 10
    count += 1
    sim_tmp = sim_n1
    sim_n1 = sim_n1 // gcd(sim_n1, sim_d3)
    sim_d3 = sim_d3 // gcd(sim_tmp, sim_d3)
    L = get_prime(sim_d3)
print(f'Count ={count}')

'''
以上这段 sim_n1 不断*10后，再与sim_d3化简的过程，可能无法跑出结果（e.g. Quiz2 TestCase13 sim_d3 = 99999900000 过大 ）
'''

if quotient == ['0']:
    sigma = ''
else:
    sigma_string = [str(i) for i in quotient[quotient.index('.')+ 1 : quotient.index('.') + count + 1]]
    sigma = ''.join(sigma_string)
    print(f'SIGMA = {sigma_string}')

if not has_finite_expansion:
    quotient_1 = quotient[quotient.index('.') + count + 1:]
    quotient_1 = [int(x) for x in quotient_1]
    quotient_1_set = set(quotient_1[:len(quotient_1)-2])
    print(quotient_1)
    for i in range(0, (len(quotient_1))):
        tau_1 = quotient_1[0: i + 1]
        tau_2 = quotient_1[i + 1: 2 * i + 2]
        if tau_1 == tau_2 and set(tau_1) == quotient_1_set:
            tau_str = [str(i) for i in quotient_1[0: i + 1]]
            tau = ''.join(tau_str)
            print('I find it!')
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

