
def dec2bin(str_num):
    '''
    娴滃矁绻橀崚鎯版祮閹?
    '''
    l = [[0 ,0 ,0 ,0] ,[0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1],
         [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1],
         [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
         [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
    num = int(str_num, 10)
    return l[num]


class FriezeError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)  # 閸掓繂顫愰崠鏍煑缁?
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


class Frieze:
    def __init__(self, filename):
        self.data = []
        self.linelist_0 = []
        self.linelist_1 = []
        self.linelist_2 = []
        self.linelist_3 = []
        temp = filename[filename.rfind('\\') + 1:]
        self.filename = temp[:temp.rfind('.')]  + '.tex'
        with open(filename, 'r') as fp:
            for line in fp:
                if line.split():
                    self.data.append([dec2bin(x) for x in line.split()])

    def display(self):
        self.find0()
        self.find1()
        self.find2()
        self.find3()
        self.draw()

    def draw(self):
        name = self.filename
        with open(name, 'w')as f:
            f.write('\\documentclass[10pt]{article}\n')
            f.write('\\usepackage{tikz}\n')
            f.write('\\usepackage[margin=0cm]{geometry}\n')
            f.write('\\pagestyle{empty}\n')
            f.write('\n')
            f.write('\\begin{document}\n')
            f.write('\n')
            f.write('\\vspace*{\\fill}\n')
            f.write('\\begin{center}\n')
            f.write('\\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]\n')
            f.write('% North to South lines\n')
            self.linelist_0.sort(key=lambda key: (key[0][0], key[0][1]))
            for line in self.linelist_0:
                str = f'\\draw ({line[0][0]},{line[0][1]}) -- ({line[1][0]},{line[1][1]});'
                f.write(f'    \\draw ({line[0][0]},{line[0][1]}) -- ({line[1][0]},{line[1][1]});\n')
            f.write('% North-West to South-East lines\n')
            self.linelist_1 = list(set(self.linelist_1))
            self.linelist_1.sort(key=lambda key: (key[0][1], key[0][0]))
            for line in self.linelist_1:
                str = f'\\draw ({line[0][0]},{line[0][1]}) -- ({line[1][0]},{line[1][1]});'
                f.write(f'    \\draw ({line[0][0]},{line[0][1]}) -- ({line[1][0]},{line[1][1]});\n')
            f.write('% West to East lines\n')
            for line in self.linelist_2:
                str = f'\\draw ({line[0][0]},{line[0][1]}) -- ({line[1][0]},{line[1][1]});'
                f.write(f'    \\draw ({line[0][0]},{line[0][1]}) -- ({line[1][0]},{line[1][1]});\n')
            f.write('% South-West to North-East lines\n')
            self.linelist_3 = list(set(self.linelist_3))
            self.linelist_3.sort(key=lambda key: (key[0][1], key[0][0]))
            for line in self.linelist_3:
                str = f'\\draw ({line[0][0]},{line[0][1]}) -- ({line[1][0]},{line[1][1]});'
                f.write(f'    \\draw ({line[0][0]},{line[0][1]}) -- ({line[1][0]},{line[1][1]});\n')
            f.write('\\end{tikzpicture}\n')
            f.write('\\end{center}\n')
            f.write('\\vspace*{\\fill}\n')
            f.write('\n')
            f.write('\\end{document}\n')

    def find0(self):
        '''
        閺屻儲澹樼粩?(0,1)->(0,0)
        '''
        rowlen = len(self.data)
        collen = len(self.data[0])
        isbegin = False
        begin = ()
        end = ()

        for col in range(collen):
            for row in range(rowlen - 1, 0, -1):
                a = self.data[row][col][3]
                if a == 1 and not isbegin:
                    begin = (col, row)
                    isbegin = True
                    if row == 1:
                        end = (col, row - 1)
                        isbegin = False
                        if begin[0] > end[0]:
                            begin, end = end, begin
                        if begin[0] == end[0] and begin[1] > end[1]:
                            temp = begin
                            begin = end
                            end = temp
                        self.linelist_0.append((begin, end))
                        continue
                    continue
                if a == 1 and isbegin:
                    if row == 1:
                        end = (col, row - 1)
                        isbegin = False
                        if begin[0] > end[0]:
                            begin, end = end, begin
                        if begin[0] == end[0] and begin[1] > end[1]:
                            temp = begin
                            begin = end
                            end = temp
                        self.linelist_0.append((begin, end))
                        continue
                    continue

                if a == 0 and isbegin:
                    end = (col, row)
                    isbegin = False

                    if begin[0] > end[0]:
                        temp = begin
                        begin = end
                        end = temp
                    if begin[0] == end[0] and begin[1] > end[1]:
                        temp = begin
                        begin = end
                        end = temp

                    self.linelist_0.append((begin, end))
                    continue

                if a == 0 and not isbegin:
                    continue

    def find3(self):
        '''
        閺屻儲澹橀弬婊€绗?5鎺抽敍灞肩矤瀹革缚绗呴幍鎯у煂閸欏厖绗?        '''
        rowlen = len(self.data)
        collen = len(self.data[0])
        isbegin = False
        begin = ()
        end = ()

        for row in range(rowlen):
            x = row
            y = 0
            while x > 0:
                a = self.data[x][y][2]
                if a == 1 and not isbegin:
                    begin = (y, x)
                    isbegin = True
                    x = x - 1
                    y = y + 1
                    if x == 0:
                        end = (y, x)
                        isbegin = False
                        x = x - 1
                        y = y + 1

                        if begin[0] > end[0]:
                            temp = begin
                            begin = end
                            end = temp
                        if begin[0] == end[0] and begin[1] > end[1]:
                            temp = begin
                            begin = end
                            end = temp

                        self.linelist_3.append((begin, end))
                        continue
                    continue
                if a == 1 and isbegin:
                    x = x - 1
                    y = y + 1
                    if x == 0:
                        end = (y, x)
                        isbegin = False
                        x = x - 1
                        y = y + 1

                        if begin[0] > end[0]:
                            temp = begin
                            begin = end
                            end = temp
                        if begin[0] == end[0] and begin[1] > end[1]:
                            temp = begin
                            begin = end
                            end = temp

                        self.linelist_3.append((begin, end))
                        continue
                    continue

                if a == 0 and isbegin:
                    end = (y, x)
                    isbegin = False
                    x = x - 1
                    y = y + 1

                    if begin[0] > end[0]:
                        temp = begin
                        begin = end
                        end = temp
                    if begin[0] == end[0] and begin[1] > end[1]:
                        temp = begin
                        begin = end
                        end = temp

                    self.linelist_3.append((begin, end))
                    continue

                if a == 0 and not isbegin:
                    x = x - 1
                    y = y + 1
                    continue

        isbegin = False
        for col in range(collen):
            x = rowlen - 1
            y = col
            while x > 0 and y < collen:
                a = self.data[x][y][2]
                if a == 1 and not isbegin:
                    begin = (y, x)
                    isbegin = True
                    x = x - 1
                    y = y + 1
                    if x == 0:
                        end = (y, x)
                        isbegin = False
                        x = x - 1
                        y = y + 1

                        if begin[0] > end[0]:
                            temp = begin
                            begin = end
                            end = temp
                        if begin[0] == end[0] and begin[1] > end[1]:
                            temp = begin
                            begin = end
                            end = temp

                        self.linelist_3.append((begin, end))
                        continue
                    continue
                if a == 1 and isbegin:
                    x = x - 1
                    y = y + 1
                    if x == 0:
                        end = (y, x)
                        isbegin = False
                        x = x - 1
                        y = y + 1

                        if begin[0] > end[0]:
                            temp = begin
                            begin = end
                            end = temp
                        if begin[0] == end[0] and begin[1] > end[1]:
                            temp = begin
                            begin = end
                            end = temp

                        self.linelist_3.append((begin, end))
                        continue
                    continue

                if a == 0 and isbegin:
                    end = (y, x)
                    isbegin = False
                    x = x - 1
                    y = y + 1

                    if begin[0] > end[0]:
                        temp = begin
                        begin = end
                        end = temp
                    if begin[0] == end[0] and begin[1] > end[1]:
                        temp = begin
                        begin = end
                        end = temp

                    self.linelist_3.append((begin, end))
                    continue

                if a == 0 and not isbegin:
                    x = x - 1
                    y = y + 1
                    continue

    def find2(self):
        '''
        閺屻儲澹樺Ο顏庣礉娴犲骸涔忔稉瀣閸掓澘褰告稉?
        '''
        rowlen = len(self.data)
        collen = len(self.data[0])
        isbegin = False
        begin = ()
        end = ()

        for row in range(rowlen):
            for col in range(collen):
                a = self.data[row][col][1]
                if a == 1 and not isbegin:
                    begin = (col, row)
                    isbegin = True
                    continue
                if a == 1 and isbegin:
                    continue

                if a == 0 and isbegin:
                    end = (col, row)
                    isbegin = False

                    if begin[0] > end[0]:
                        temp = begin
                        begin = end
                        end = temp
                    if begin[0] == end[0] and begin[1] > end[1]:
                        temp = begin
                        begin = end
                        end = temp

                    self.linelist_2.append((begin, end))
                    continue

                if a == 0 and not isbegin:
                    continue

    def find1(self):
        '''
        閺屻儲澹橀弬婊€绗?5鎺?        '''
        rowlen = len(self.data)
        collen = len(self.data[0])
        isbegin = False
        begin = ()
        end = ()

        for row in range(rowlen - 1, -1, -1):
            x = row
            y = 0
            while x < rowlen and y < collen:
                a = self.data[x][y][0]
                if a == 1 and not isbegin:
                    begin = (y, x)
                    isbegin = True
                    x = x + 1
                    y = y + 1
                    continue
                if a == 1 and isbegin:
                    x = x + 1
                    y = y + 1
                    continue

                if a == 0 and isbegin:
                    end = (y, x)
                    isbegin = False
                    x = x + 1
                    y = y + 1

                    if begin[0] > end[0]:
                        temp = begin
                        begin = end
                        end = temp
                    if begin[0] == end[0] and begin[1] > end[1]:
                        temp = begin
                        begin = end
                        end = temp

                    self.linelist_1.append((begin, end))
                    continue

                if a == 0 and not isbegin:
                    x = x + 1
                    y = y + 1
                    continue

        isbegin = False
        for col in range(collen):
            x = 0
            y = col
            while x < rowlen and y < collen:
                a = self.data[x][y][0]
                if a == 1 and not isbegin:
                    begin = (y, x)
                    isbegin = True
                    x = x + 1
                    y = y + 1
                    continue
                if a == 1 and isbegin:
                    x = x + 1
                    y = y + 1
                    continue

                if a == 0 and isbegin:
                    end = (y, x)
                    isbegin = False
                    x = x + 1
                    y = y + 1

                    if begin[0] > end[0]:
                        temp = begin
                        begin = end
                        end = temp
                    if begin[0] == end[0] and begin[1] > end[1]:
                        temp = begin
                        begin = end
                        end = temp

                    self.linelist_1.append((begin, end))
                    continue

                if a == 0 and not isbegin:
                    x = x + 1
                    y = y + 1
                    continue

a = Frieze('frieze_5.txt')
a.display()