class a:
    def __init__(self):
        a.x = 1
        a.y = 2

    def __init__(self, * , x, y):
        a.x = x
        a.y = y

    def change(self, * , x, y):
        a.x = x
        a.y = y


case = a(x = 2, y = 4)
print(case.x,case.y)
print()
case.change(x = 4, y = 8)
print(case.x,case.y)
if not None:
    print('yyyy')
