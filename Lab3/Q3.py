import math
L = []

def is_special(n):
    a, b, c = 0, 0, 0
    L_tmp = []
    for i in range(int(math.sqrt(n) + 1)):
        for j in range(i, int(math.sqrt(n) + 1)):
            if a == 1:
                break
            if i ** 2 + j ** 2 == n:
                L_tmp.append([n,i,j])
                a = 1
    for i in range(int(math.sqrt(n + 1) + 1)):
        for j in range(i, int(math.sqrt(n + 1) + 1)):
            if b == 1:
                break
            if i ** 2 + j ** 2 == n + 1:
                L_tmp.append([n + 1,i,j])
                b = 1
    for i in range(int(math.sqrt(n + 12) + 1)):
        for j in range(i, int(math.sqrt(n + 2) + 1)):
            if c == 1:
                break
            if i ** 2 + j ** 2 == n + 2:
                L_tmp.append([n + 2,i,j])
                c = 1
    if a + b + c == 3:
        L.append(L_tmp)

for i in range(100, 997):
    is_special(i)
    
for i in range(len(L)):
    print(L[i],end = '\n')
            
