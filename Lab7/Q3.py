import random

class Target():
    def __init__(self, target = None, length = 4):
        list = []
        self.dict = []
        self.length = length
        self.target = target if target else ''
        for i in range(65,91):
            list.append(i)
        if not self.target:
            for i in random.sample(list, 9):
                self.target += chr(i)
        if type(self.target) is not str and len(self.target) != 9:
            for i in random.sample(list, 9):
                self.target += chr(i)
        with open('Week 8 - dictionary.txt','r') as f:
            for line in f.readlines():
                self.dict.append(line)

a = Target()
print(a.target,a.length)