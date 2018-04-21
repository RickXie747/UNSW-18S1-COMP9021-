import sys

try:
    num = int(input('Enter strictly positive number:'))
    if num <= 0:
        print('Wrong input!')
        sys.exit()
except ValueError:
    print('Wrong input!')
    sys.exit()

for i in range(num):
    print((num - i - 1) * ' ', end = '')
    for a in range((i ** 2 + i) // 2, (i ** 2 + i) // 2 + i + 1):
        print(chr(65 + a), end = '')
    for b in range((i ** 2 + i) // 2 + i - 1, (i ** 2 + i) // 2 - 1, -1):
        print(chr(65 + b), end = '')
    print()
    

        
