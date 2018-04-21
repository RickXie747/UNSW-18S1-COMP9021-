import sys

try:
    num = int(input('Input a nonnegative integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if num < 0:
    print('Incorrect input, giving up.')
    sys.exit()

factorial = 1

for i in range(1, num + 1):
    factorial *= i

def method_1(factorial):
    count = 0
    while factorial % 10 == 0:
        count += 1
        factorial = factorial // 10
    return count

def method_2(factorial):
    factorial = str(factorial)
    i = -1
    count = 0
    while  factorial[i] == '0':
        i -= 1
        count += 1
    return count

def method_3(factorial):
    pa




print(method_1(factorial))
print(method_2(factorial))







