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

L = []
while not sim_d2 % 2:
    L.append(2)
    sim_d2 = sim_d2 // 2
while not sim_d2 % 5:
    L.append(5)
    sim_d2 =sim_d2 // 5

print(sim_d2)
print(L)

count = 0
while L.count(2) >= 1 or L.count(5) >= 1:
    sim_n1 *= 10
    count += 1
    sim_tmp = sim_n1
    sim_n1 = sim_n1 // gcd(sim_n1, sim_d3)
    sim_d3 = sim_d3 // gcd(sim_tmp, sim_d3)
    L = []
    while not sim_d3 % 2:
        L.append(2)
        sim_d2 = sim_d3 // 2
    while not sim_d3 % 5:
        L.append(5)
        sim_d2 = sim_d3 // 5

print(f'Count ={count}')