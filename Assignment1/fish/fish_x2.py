'''
问题出现在get_midnum函数，line48,50处不加return，line42,45就不返回值，可是步骤正常，可以求出20，但无返回值。加了就可以，why？
'''

import sys
import os
from statistics import mean


L = []
tmp_L = []

try:
    file = input('Which data file you want to use?')
    with open(file,'r') as f:
        for line in f.readlines():
            tmp_L = line.strip().split()
            print(tmp_L)
            L.append(int(tmp_L[0])),L.append(int(tmp_L[1]))
except IOError:
    sys.exit()


def is_able(num):
    L_distance = L[::2]
    L_fish = L[1::2]
    for i in range(len(L)//2 - 1):
        if L_fish[i] > num + abs(L_distance[i+1] - L_distance[i]):
            L_fish[i + 1] += L_fish[i] - num - abs(L_distance[i + 1] - L_distance[i])
            L_fish[i] = num
        elif L_fish[i] < num:
            if L_fish[i + 1] - abs(L_distance[i + 1] - L_distance[i]) - (num - L_fish[i]) > 0:
                L_fish[i + 1] -= abs(L_distance[i + 1] - L_distance[i]) + (num - L_fish[i])
                L_fish[i] = num
        return True if min(L_fish) >= num else False

def get_midnum(minnum, maxnum):
    midnum = round((minnum + maxnum) / 2)
    print(midnum)
    if minnum == maxnum:
        print('yeah case1 ', midnum)
        return midnum
    if is_able(minnum) and not is_able(maxnum) and maxnum - minnum == 1:
        print('yeah case2 ', minnum)
        return minnum
    if is_able(midnum):
        print('Now the midnum and maxnum are: ',midnum,' ',maxnum)
        get_midnum(midnum, maxnum)    #为何这里不加return就会导致整个函数无法return值，最下面的result为none
    if not is_able(midnum):
        print('Now the minnum and midnum are: ', minnum, ' ', midnum)
        get_midnum(minnum, midnum)

min_fish = min(L[1::2])
max_fish = round(mean(L[1::2]))

print(min_fish)
print(max_fish)
result = get_midnum(min_fish,max_fish)
print(result)


