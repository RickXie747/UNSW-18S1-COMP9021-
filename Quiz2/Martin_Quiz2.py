import sys


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


##################################

numerator_1 = numerator
denominator_1 = denominator

L = [ ]
L.append(numerator_1 % denominator_1)
L_1 = []
i = 0


while L.count(L[i]) < 2:
    numerator_1 *= 10
    L.append(numerator_1 % denominator_1)
    L_1.append(L[i] * 10 // denominator_1)
    i += 1

print(L)
print(L_1)
sigma_str = [str(i) for i in L_1[0 : L.index(L[len(L) - 1])]]
tau_str = [str(i) for i in L_1[L.index(L[len(L)-1]) : ]]
sigma = ''.join(sigma_str)
tau = ''.join(tau_str)

print(sigma)
print(tau)




