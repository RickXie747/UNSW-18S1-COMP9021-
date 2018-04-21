a = '0123456789'

def f(n, sum, sign, n2, path):
    if n < 9:
        f(n + 1, sum + int(a[n + 1]), ' + ', str(n + 1), path + sign + n2)
        f(n + 1, sum - int(a[n + 1]), ' - ', str(n + 1), path + sign + n2)
        if n < 7:
            f(n + 3, sum + 100 * int(a[n + 1]) + 10 * int(a[n + 2]) + int(a[n + 3]), ' + ', str(a[n + 1]) + str(a[n + 2]) + str(a[n + 3]), path + sign + n2)
            f(n + 3, sum - 100 * int(a[n + 1]) - 10 * int(a[n + 2]) - int(a[n + 3]), ' - ', str(a[n + 1]) + str(a[n + 2]) + str(a[n + 3]), path + sign + n2)
        if n < 8:
            f(n + 2, sum + 10 * int(a[n + 1]) + int(a[n + 2]), ' + ', str(a[n + 1]) + str(a[n + 2]), path + sign + n2)
            f(n + 2, sum - 10 * int(a[n + 1]) - int(a[n + 2]), ' - ', str(a[n + 1]) + str(a[n + 2]), path + sign + n2)

    if n == 9 and sum == 100:
        if path[1] == '+':
            print(' '  + path[2:] + sign + n2 + ' = 100')
        else:
            print(path[1:] + sign + n2 + ' = 100')


f(0,0, '', '', '')


