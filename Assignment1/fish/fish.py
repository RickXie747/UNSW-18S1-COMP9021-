import sys
import os
from statistics import mean


L = []
tmp_L = []

try:
    file = input('Which data file you want to use? ')
    with open(file,'r') as f:
        for line in f.readlines():
            tmp_L = line.strip().split()
            L.append(int(tmp_L[0])),L.append(int(tmp_L[1]))
except IOError:
    print('There is no ' + file)
    sys.exit()


def is_able(num):
    L_distance = L[::2]
    L_fish = L[1::2]
    for i in range(len(L)//2 - 1):
        if L_fish[i] > num + abs(L_distance[i+1] - L_distance[i]):
            L_fish[i + 1] += L_fish[i] - num - abs(L_distance[i + 1] - L_distance[i])
            L_fish[i] = num
        elif L_fish[i] < num:
           # if L_fish[i + 1] - abs(L_distance[i + 1] - L_distance[i]) - (num - L_fish[i]) > 0:
                L_fish[i + 1] -= abs(L_distance[i + 1] - L_distance[i]) + (num - L_fish[i])
                L_fish[i] = num
    return True if min(L_fish) >= num else False

def get_midnum(minnum, maxnum):
    midnum = round((minnum + maxnum) / 2)
    if minnum == maxnum:
        return midnum
    if is_able(minnum) and not is_able(maxnum) and maxnum - minnum == 1:
        return minnum
    if is_able(midnum):
        return get_midnum(midnum, maxnum)
    if not is_able(midnum):
        return get_midnum(minnum, midnum)

min_fish = min(L[1::2])
max_fish = round(mean(L[1::2]))

print(f'The maximum quantity of fish that each town can have is {get_midnum(min_fish,max_fish)}.')


