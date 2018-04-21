
def print_square(*L):
    if not L:
        raise square_exception('No Input!')
    for i in range(len(L[0])):
        if len(L[0]) != len(L[0][i]):
            raise square_exception(f'Wrong Input!')
        for j in range(len(L[0][i])):
            print(L[0][i][j], end = ' ')
        print()


def is_magic_square(*L):
    sum = 0
    for i in range(len(L[0][0])):
        sum += L[0][0][i]
    for i in range(len(L[0])):
        tmp_sum = 0
        for j in range(len(L[0][i])):
            tmp_sum += L[0][i][j]
        if tmp_sum != sum:
            return False
    for i in range(len(L[0])):
        tmp_sum = 0
        for j in range(len(L[0][i])):
            tmp_sum += L[0][j][i]
        if tmp_sum != sum:
            return False
    return True
    
class square_exception(Exception):
    def __int__(self, message):
        self.message = message


    
