L = [(1,1),(2,2),(3,3)]
D = {}
D.update({'N':[i for i in L]})

print(D)

triangles = D

for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')


for x in 'abc':
    print(x)
    print(type(x))