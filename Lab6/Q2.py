a_1 = input('a:')
b_1 = input('b:')
c_1 = input('c:')

a,b,c = [],[],[]

for e in a_1:
    a.append(e)
for e in b_1:
    b.append(e)
for e in c_1:
    c.append(e)

result = False

def find(a, b, c):
    global result
    if not c:
        return 
    if not a and not b:
        return 
    if a.count(c[0]):
        if len(c) == 1:
            result = True
            return 
        if len(a) == 1:
            find([], b, c[1:])
        find(a[a.index(c[0]) + 1:], b, c[1:])
    if b.count(c[0]):
        if len(c) == 1:
            result = True
            return 
        if len(b) == 1:
            find(a, [], c[1:])
        find(a, b[b.index(c[0]) + 1:], c[1:])
    if not a.count(c[0]) and not b.count(c[0]):
        return 

find(a, b, c)
print(result)
