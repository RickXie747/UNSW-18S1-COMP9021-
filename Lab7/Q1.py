amount = int(input('desired amount: '))
a,b,c,d,e,f,g = 0,0,0,0,0,0,0

if amount >= 100:
    a = amount // 100
    amount %= 100
if amount >= 50:
    b = amount // 50
    amount %= 50
if amount >= 20:
    c = amount // 20
    amount %= 20
if amount >= 10:
    d = amount // 10
    amount %= 10
if amount >= 5:
    e = amount // 5
    amount %= 5
if amount >= 2:
    f = amount // 2
    amount %= 2
g = amount // 1

print(a+b+c+d+e+f+g, 'banknotes are needed')
if a:
    print('$100:', a)
if b:
    print('$50:', b)
if c:
    print('$20:', c)
if d:
    print('$10:', d)
if e:
    print('$5:', e)
if f:
    print('$2:', f)
if g:
    print('$1:', g)
        
    
