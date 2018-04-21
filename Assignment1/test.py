a = {}
a[50] = 1
a[10] = 5
a[1] = 1
print(max(a.values()))
print(max(a, key = a.get))



