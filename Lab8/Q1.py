def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n - 2) + f(n - 1)


def encode(n):
    if n == 1:
        return '11'
    limit = 0
    L = []
    while f(limit) < n:
        limit += 1
    _encode_1(n, limit, L)
    return _encode_2(L)

def _encode_1(n, limit, L):
    if not n:
        return
    for i in range(limit, 1, -1):
        if f(i) <= n:
            L.append(i)
            _encode_1(n - f(i), limit, L)
            break

def _encode_2(L):
    result = [0] * (L[0] - 1)
    result.append(1)
    for e in L:
        result[e - 2] = 1
    result_1 = ''
    for e in result:
        result_1 += str(e)
    return result_1

def decode(n):
    if n.count('1') == 2:
        return f(len(n))
    elif n.count('1') >= 3:
        for i in range(len(n) - 2):
            if n[i] == n[i + 1] == '1':
                return 0
        L = []
        for i in range(len(n) - 1):
            if n[i] == '1':
                L.append(i + 2)
        result = 0
        for e in L:
            result += f(e)
        return result
    else:
        return 0

print(encode(12))
print(decode('100011011'))







