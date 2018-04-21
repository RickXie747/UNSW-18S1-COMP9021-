import sys
from math import gcd

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


def has_finite_expansion(denominator):
    while denominator % 2 == 0:
        denominator = denominator / 2
    while denominator % 5 == 0:
        denominator = denominator / 5
    if denominator == 1:
        return True
    return False


has_finite_expansion = has_finite_expansion(denominator)
integral_part = numerator // denominator
sigma = ''
tau = ''

numerator_1 = numerator

denominator_1 = denominator

L = []

L.append(numerator_1 % denominator_1)

L_1 = []

i = 0

while L.count(L[i]) < 2:
    numerator_1 *= 10

    L.append(numerator_1 % denominator_1)

    L_1.append(L[i] * 10 // denominator_1)

    i += 1

sigma_str = [str(i) for i in L_1[0: L.index(L[len(L) - 1])]]

tau_str = [str(i) for i in L_1[L.index(L[len(L) - 1]):]]

sigma = ''.join(sigma_str)


if not tau_str == ['0']:
    tau = ''.join(tau_str)




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
