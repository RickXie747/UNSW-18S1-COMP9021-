#Written by Rick Xie z5192747 for COMP9021
from copy import *

class FriezeError(Exception):
    def __init__(self, message):
        self.message = message

class Frieze:
    def __init__(self, file):
        self.list_h = []
        self.period = 0
        self.vertical = False
        self.horizontal = False
        self.glided_horizontal = False
        self.rotation = False
        with open(file, 'r') as f:
            for line in f.readlines():
                if not line.strip():
                    continue
                tmp_list = []
                for e in line.split():
                    if int(e) < 0 or int(e) > 15:
                        raise FriezeError('Incorrect input.')
                    tmp_list.append(int(e))
                if len(tmp_list) < 5 or len(tmp_list) > 51:     #length 4-50
                    raise FriezeError('Incorrect input.')
                self.list_h.append(tmp_list)
        if len(self.list_h) < 3 or len(self.list_h) > 17:       #height 2-16
            raise FriezeError('Incorrect input.')
        length = len(self.list_h[0])
        for i in range(len(self.list_h)):
            if len(self.list_h[i]) != length:                   #not equal length(height as well)
                raise FriezeError('Incorrect input.')
        self.is_frieze()
        self.is_translation()

    def binary(self, n):
        result = (6 - len(bin(n))) * '0' + bin(n)[2:]
        return result

    def is_frieze(self):
        for i in range(len(self.list_h[0])):
            if self.binary(self.list_h[0][i])[2:] != '00':
                raise FriezeError('Input does not represent a frieze.')   #upmost line should not have | /
        for i in range(len(self.list_h)):
            if self.binary(self.list_h[i][-1])[:3] != '000':              #rightmost line should not have —— / \
                raise FriezeError('Input does not represent a frieze.')
        for i in range(len(self.list_h[-1])):
            if self.binary(self.list_h[-1][i])[0] != '0':                 #downmost line should not have \
                raise FriezeError('Input does not represent a frieze.')
        for i in range(len(self.list_h) - 1):                             #no crossing
            for j in range(len(self.list_h[0]) - 1):
                if self.binary(self.list_h[i][j])[0] == '1' and self.binary(self.list_h[i + 1][j])[2] == '1':
                    print(i,j)
                    raise FriezeError('Input does not represent a frieze.')

    def transfer_frieze(self):
        list = deepcopy(self.list_h)
        for i in range(len(list)):
            for j in range(len(list[0])):
                if self.binary(self.list_h[i][j])[0] == '1' and i < len(list) - 1 and j < len(list[0]) - 1:
                    list[i + 1][j + 1] += 8
                if self.binary(self.list_h[i][j])[3] == '1':
                    list[i - 1][j] += 1
                if self.binary(self.list_h[i][j])[2] == '1' and i > 0 and j < len(list[0]) - 1:
                    list[i - 1][j + 1] += 2
                if self.binary(self.list_h[i][j])[1] == '1':
                    list[i][j + 1] += 4
        return list

    def is_translation(self):
        for i in range(2, len(self.list_h[0]) // 2 + 1):
            if self.period:
                if (len(self.list_h[0]) - 1) % self.period:     #not fully repeated
                    self.period = 0
                    raise FriezeError('Input does not represent a frieze.')
                else:                                           #smallest period
                    break
            if self.list_h[0][0: i] == self.list_h[0][i: 2 * i]:
                self.period = i
                for j in range(1, len(self.list_h)):
                    if self.list_h[j][0: i] != self.list_h[j][i: 2 * i]:
                        self.period = 0
        if not self.period:
            raise FriezeError('Input does not represent a frieze.')

    def is_vertical(self):
        list = self.transfer_frieze()
        for j in range(len(list[0]) // 2):          # vertical line is in the middle of two points
            if 2 * j - 1 < self.period:             # two parts should be bigger than one period
                continue
            if list[0][1: j] == (list[0][2 * j - 2:j - 1: -1]):
                for i in range(1, len(list)):
                    if list[i][1: j] != list[i][2 * j - 2:j - 1: -1]:
                        break
                    if i == len(list)- 1:
                        self.vertical = True
        for j in range(len(list[0]) // 2):          # vertical line is on one point
            if 2 * j - 1 < self.period:             # two parts should be bigger than one period
                continue
            if list[0][1: j] == (list[0][2 * j - 1:j : -1]):
                for i in range(1, len(list)):
                    if list[i][1: j] != list[i][2 * j - 1:j : -1]:
                        break
                    if i == len(list) - 1:
                        self.vertical = True

    def is_horizontal(self):
        list = self.transfer_frieze()
        if not len(list) % 2:          # horizontal line is in the middle of two points
            if list[:len(list) // 2] == list[-1:len(list) // 2 - 1:-1]:
                self.horizontal = True
        else:                          # horizontal line is on one point
            if list[:len(list) // 2 + 1] == list[-1:len(list) // 2 - 1:-1]:
                self.horizontal = True

    def is_glided_horizontal(self):
        list = self.transfer_frieze()
        list_shift = deepcopy(list[(len(list) + 1) // 2:])
        for i in range(len(list_shift)):
            list_shift[-1 - i] = list[i]
        for i in range(len(list_shift)):
            if list_shift[i][:self.period] != list[i - len(list_shift)][self.period // 2: self.period + self.period // 2]:
                return
            if i == len(list_shift) - 1:
                self.glided_horizontal = True

    def is_rotation(self):
        list = self.transfer_frieze()
        list_rotated = []
        compare_list = []
        for i in range(len(list)):
            list_rotated.append(list[-1 - i][1:self.period + 1][::-1])
        for j in range(1, len(list[0])):
            for i in range(len(list)):
                compare_list.append(list[i][j : j + self.period])
            if compare_list == list_rotated:
                self.rotation = True
                return
            else:
                compare_list = []

    def analyse(self):
        self.is_vertical()
        self.is_horizontal()
        self.is_glided_horizontal()
        self.is_rotation()
        if self.vertical and not self.glided_horizontal and not self.horizontal:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
            print('        and vertical reflection only.')
        elif self.horizontal and not self.vertical:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
            print('        and horizontal reflection only.')
        elif self.glided_horizontal and not self.vertical:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
            print('        and glided horizontal reflection only.')
        elif self.rotation and not self.vertical and not self.glided_horizontal:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
            print('        and rotation only.')
        elif self.vertical and self.horizontal and self.rotation:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation,')
            print('        horizontal and vertical reflections, and rotation only.')
        elif self.vertical and self.glided_horizontal and self.rotation:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation,')
            print('        glided horizontal and vertical reflections, and rotation only.')
        else:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation only.')

frieze = Frieze('frieze_2.txt')
frieze.analyse()
a = frieze.transfer_frieze()
print()
for i in range(len(a)):
    print(a[i])