
triangles = {
    'N': [(3,9), (2,2)]
}

F = {
    'N':None,
    'E':None,
    'S':None,
    'W':None}

a = 6
L = {2:5}
L.update({3:a})


print(type(L),L)




for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')


