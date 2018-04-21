import sys
from math import factorial


def f(n):
    '''
    >>> f(0)
    0 factorial is 1
    It has 1 digit, the trailing 0's excepted
    >>> f(4)
    4 factorial is 24
    It has 2 digits, the trailing 0's excepted
    >>> f(6)
    6 factorial is 720
    It has 2 digits, the trailing 0's excepted
    >>> f(10)
    10 factorial is 3628800
    It has 5 digits, the trailing 0's excepted
    >>> f(20)
    20 factorial is 2432902008176640000
    It has 15 digits, the trailing 0's excepted
    >>> f(30)
    30 factorial is 265252859812191058636308480000000
    It has 26 digits, the trailing 0's excepted
    >>> f(40)
    40 factorial is 815915283247897734345611269596115894272000000000
    It has 39 digits, the trailing 0's excepted
    '''
    if n < 0:
        sys.exit()

    # Insert your code here
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    digits = len(str(factorial))
    count = 0    
    for i in range(len(str(factorial)) - 1, -1, -1):
        if str(factorial)[i] == '0':
            count += 1
        else:
            break
    result = digits - count
    print(f'{n} factorial is',factorial)
    if result == 1:
        print(f'It has {result} digit, the trailing 0\'s excepted')
    else:
        print(f'It has {result} digits, the trailing 0\'s excepted')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
