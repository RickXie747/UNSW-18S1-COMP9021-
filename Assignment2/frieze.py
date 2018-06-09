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
        self.name = file.split('.')[0]
        with open(file, 'r') as f:
            for line in f.readlines():
                if not line.strip():
                    continue
                tmp_list = []
                for e in line.split():
                    if not e.isdigit():
                        raise FriezeError('Incorrect input.')   #not a digit
                    if int(e) < 0 or int(e) > 15:
                        raise FriezeError('Incorrect input.')   #with number out of range
                    tmp_list.append(int(e))
                if len(tmp_list) < 5 or len(tmp_list) > 51:
                    raise FriezeError('Incorrect input.')       #length 4-50
                self.list_h.append(tmp_list)
        if len(self.list_h) < 3 or len(self.list_h) > 17:
            raise FriezeError('Incorrect input.')               #height 2-16
        length = len(self.list_h[0])
        for i in range(len(self.list_h)):
            if len(self.list_h[i]) != length:
                raise FriezeError('Incorrect input.')           #not equal length(height as well)
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
                    raise FriezeError('Input does not represent a frieze.')

    def is_translation(self):
        for i in range(len(self.list_h[0]) - 1):                        #top and bottom line
            if not int(self.binary(self.list_h[0][i])[1]) or not int (self.binary(self.list_h[-1][i])[1]):
                raise FriezeError('Input does not represent a frieze.')
        for i in range(1 ,(len(self.list_h[0]) - 1) // 2 + 1):
            if self.period:                                         #smallest period
                    break
            if self.list_h[0][0: i] == self.list_h[0][i: 2 * i] and \
                            self.binary(self.list_h[0][i])[3] == self.binary(self.list_h[0][2 * i])[3] and \
                                    not (len(self.list_h[0]) - 1) % i:
                self.period = i
                for j in range(1, (len(self.list_h[0])-1) // i):        #fully repeated
                    for k in range(len(self.list_h)):
                        if self.list_h[k][0: i] != self.list_h[k][j * i: (j + 1) * i] or \
                                        self.binary(self.list_h[k][i])[3] != self.binary(self.list_h[k][(j + 1) * i])[3]:
                            self.period = 0
        if self.period < 2:                                     #period < 2
            raise FriezeError('Input does not represent a frieze.')

    def is_vertical(self):
        list = deepcopy(self.list_h)
        for i in range(len(list)):
            for j in range(len(list[0])):
                if self.binary(self.list_h[i][j])[0] == '1' and i < len(list) - 1 and j < len(list[0]) - 1:
                    list[i + 1][j + 1] += 2
                if  self.binary(self.list_h[i][j])[1] == '1'and j < len(list[0]) - 1:
                    list[i][j + 1] += 4
                if self.binary(self.list_h[i][j])[2] == '1' and i > 0 and j < len(list[0]) - 1:
                    list[i - 1][j + 1] += 8
        count = 0
        for i in range(len(self.list_h[0])):        #avoid period = 2 and only —— |
            for j in range(len(self.list_h)):
                count += 1 if int(self.binary(self.list_h[j][i])[0]) + int(self.binary(self.list_h[j][i])[2]) else count
        if not count and self.period == 2:
            return
        for j in range(len(list[0]) // 2 + 1):      # vertical line is in the middle of two points
            if 2 * j - 1 < self.period:             # two parts should at least be one period
                continue
            if list[0][1: j] == (list[0][j : 2 * j - 1][::-1]):
                for i in range(1, len(list)):
                    if list[i][1: j] != list[i][j : 2 * j - 1][::-1]:
                        break
                    if i == len(list)- 1:
                        self.vertical = True
                        return
        for j in range(3, len(list[0]) // 2 + 2):   # vertical line is on one point
            if 2 * j - 1 <= self.period:             # two parts should at least be one period
                continue
            if list[0][1: j] == (list[0][j - 1: 2 * j - 2][::-1]):  #j starts from 3 to avoid compare the same one column
                for i in range(1, len(list)):
                    if list[i][1: j] != list[i][j - 1: 2 * j - 2][::-1]:
                        break
                    if i == len(list) - 1:
                        self.vertical = True
                        return

    def is_horizontal(self):
        list = deepcopy(self.list_h)
        for i in range(len(list)):
            for j in range(len(list[0])):
                if self.binary(self.list_h[i][j])[0] == '1' and i < len(list) - 1 and j < len(list[0]) - 1:
                    list[i + 1][j + 1] += 8
                if  self.binary(self.list_h[i][j])[3] == '1':
                    list[i][j] -= 1
                    list[i][j] += 2
                    list[i - 1][j] += 2
                if self.binary(self.list_h[i][j])[2] == '1' and i > 0 and j < len(list[0]) - 1:
                    list[i][j] -= 2
                    list[i][j] += 8
                    list[i - 1][j + 1] += 8
        if not len(list) % 2:          # horizontal line is in the middle of two points
            if list[:len(list) // 2] == list[-1:len(list) // 2 - 1:-1]:
                self.horizontal = True
                return
        else:                          # horizontal line is on one point
            if list[:len(list) // 2 + 1] == list[-1:len(list) // 2 - 1:-1]:
                self.horizontal = True
                return

    def is_glided_horizontal(self):
        if self.period % 2:           #odd period
            return
        list = deepcopy(self.list_h)
        for i in range(len(list)):
            for j in range(len(list[0])):
                if self.binary(self.list_h[i][j])[0] == '1' and i < len(list) - 1 and j < len(list[0]) - 1:
                    list[i + 1][j + 1] += 8
                if  self.binary(self.list_h[i][j])[3] == '1':
                    list[i][j] -= 1
                    list[i][j] += 2
                    list[i - 1][j] += 2
                if self.binary(self.list_h[i][j])[2] == '1' and i > 0 and j < len(list[0]) - 1:
                    list[i][j] -= 2
                    list[i][j] += 8
                    list[i - 1][j + 1] += 8
        list_shift = deepcopy(list[(len(list) + 1) // 2:])
        for i in range(len(list_shift)):
            list_shift[-1 - i] = list[i]
        for i in range(len(list_shift)):        #compare one period only
            if list_shift[i][1 :self.period + 2] != list[i - len(list_shift)][self.period // 2 + 1: self.period + 2 + self.period // 2]:
                return
            if i == len(list_shift) - 1:
                self.glided_horizontal = True
                return

    def is_rotation(self):
        list = deepcopy(self.list_h)
        for i in range(len(list)):
            for j in range(len(list[0])):
                if self.binary(self.list_h[i][j])[0] == '1' and i < len(list) - 1 and j < len(list[0]) - 1:
                    list[i + 1][j + 1] += 8
                if  self.binary(self.list_h[i][j])[3] == '1':
                    list[i - 1][j] += 1
                if self.binary(self.list_h[i][j])[2] == '1' and i > 0 and j < len(list[0]) - 1:
                    list[i - 1][j + 1] += 2
                if self.binary(self.list_h[i][j])[1] == '1':
                    list[i][j + 1] += 4
        list_rotated = []
        compare_list = []
        for i in range(len(list)):
            list_rotated.append(list[-1 - i][1:self.period + 2][::-1])
        for j in range(1, len(list[0])):
            for i in range(len(list)):
                compare_list.append(list[i][j : j + self.period + 1])
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

    def get_all_path(self):    #generate the list by order of NW-SE, W-E, SW-NE, N-S
        NW_SE = []
        W_E = []
        SW_NE = []
        N_S = []
        for j in range(len(self.list_h)):
            for i in range(len(self.list_h[0])):
                if self.binary(self.list_h[j][i])[1] == '1':
                    W_E.append(f'{i},{j},{i + 1},{j}')
        for i in range(len(self.list_h[0])):
            for j in range(len(self.list_h)):
                if self.binary(self.list_h[j][i])[3] == '1':
                    N_S.append(f'{i},{j - 1},{i},{j}')
        for sum in range(len(self.list_h) + len(self.list_h[0]) - 1):
            for i in range(sum + 1):
                if i < len(self.list_h[0]) and sum - i < len(self.list_h):
                    if self.binary(self.list_h[sum - i][i])[2] == '1':
                        SW_NE.append(f'{i },{sum - i},{i + 1},{sum - i - 1}')
        for sum in range(len(self.list_h) + len(self.list_h[0]) - 1):
            for i in range(len(self.list_h[0]) - 1, -1, -1):
                if 0 <= len(self.list_h[0]) - i - 1 < len(self.list_h[0]) and 0 <= sum - i < len(self.list_h):
                    if self.binary(self.list_h[sum - i][len(self.list_h[0]) - i - 1])[0] == '1':
                        NW_SE.append(f'{len(self.list_h[0]) - i - 1},{sum - i},{len(self.list_h[0]) - i},{sum - i + 1}')
        NW_SE = self.merge_path(NW_SE)
        W_E = self.merge_path(W_E)
        SW_NE = self.merge_path(SW_NE)
        N_S = self.merge_path(N_S)
        NW_SE.sort(key= lambda path:(int(path[1]),int(path[0])))
        W_E.sort(key= lambda path:(int(path[1]),int(path[0])))
        SW_NE.sort(key= lambda path:(int(path[1]),int(path[0])))
        N_S.sort(key= lambda path:(int(path[0]),int(path[1])))
        return N_S, NW_SE, W_E, SW_NE

    def merge_path(self, path):
        merged_path = []
        tmp_path = []
        for i in range(len(path) - 1):
            if not tmp_path:
                tmp_path = path[i].split(',')
            if tmp_path[2:] == path[i + 1].split(',')[:2]:
                tmp_path = tmp_path[:2] + path[i + 1].split(',')[2:]
            else:
                merged_path.append(tmp_path)
                tmp_path = path[i + 1].split(',')
            if i == len(path) - 2:
                merged_path.append(tmp_path)
        return merged_path

    def display(self):
        N_S, NW_SE, W_E, SW_NE = self.get_all_path()
        with open(self.name + '.tex', 'w') as f:
            f.write(
                '\\documentclass[10pt]{article}\n'
                '\\usepackage{tikz}\n'
                '\\usepackage[margin=0cm]{geometry}\n'
                '\\pagestyle{empty}\n\n'
                '\\begin{document}\n\n'
                '\\vspace*{\\fill}\n'
                '\\begin{center}\n'
                '\\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]\n'
            )
            f.write('% North to South lines\n')
            for e in N_S:
                f.write(f'    \\draw ({e[0]},{e[1]}) -- ({e[2]},{e[3]});\n')
            f.write('% North-West to South-East lines\n')
            for e in NW_SE:
                f.write(f'    \\draw ({e[0]},{e[1]}) -- ({e[2]},{e[3]});\n')
            f.write('% West to East lines\n')
            for e in W_E:
                f.write(f'    \\draw ({e[0]},{e[1]}) -- ({e[2]},{e[3]});\n')
            f.write('% South-West to North-East lines\n')
            for e in SW_NE:
                f.write(f'    \\draw ({e[0]},{e[1]}) -- ({e[2]},{e[3]});\n')
            f.write(
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
                '\\vspace*{\\fill}\n\n'
                '\\end{document}\n'
            )