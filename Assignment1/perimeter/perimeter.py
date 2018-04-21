import sys

tmp_L = []
L = []

try:
    file = input('Which data file do you want to use? ')
    with open(file,'r') as f:
        for line in f.readlines():
            tmp_L = line.strip().split()
            tmp_L = [int(i) for i in tmp_L]
            L.append(tmp_L[:2])
            L.append(tmp_L[2:4])
except IOError:
    print('There is no ' + file)
    sys.exit()

def get_perimeter(L1, L2):
    perimeter = (abs(L1[0] - L2[0]) + abs(L1[1] - L2[1])) * 2
    return perimeter

def is_overlapped(L1, L2, L3, L4):
    if L1[0] < L3[0] and L1[1] < L3[1] and L2[0] > L4[0] and L2[1] > L4[1]:
        return 1    #fully overlapped L1 L2 contains L3 L4
    if L1[0] > L3[0] and L1[1] > L3[1] and L2[0] < L4[0] and L2[1] < L4[1]:
        return 2    #fully overlapped L3 L4 contains L1 L2
    if abs((L1[0] + L2[0]) / 2 - (L3[0] + L4[0]) / 2) <= abs((L1[0] - L2[0]) / 2) + abs((L3[0] - L4[0]) / 2) and \
                    abs((L1[1] + L2[1]) / 2 - (L3[1] + L4[1]) / 2) <= abs((L1[1] - L2[1]) / 2) + abs((L3[1] - L4[1]) / 2):
        return 3    # |(x1+x2)/2 - (x3+x4)/2| <= |x1-x2|/2 + |x3-x4|/2 and
                    # |(y1+y2)/2 - (y3+y4)/2| <= |y1-y2|/2 + |y3-y4|/2
                    # partly overlapped
    else:
        return 4    #disjoint

def get_perimeter_all():
    perimeter_all = 0
    for i in range(len(L) // 2):
        perimeter_all += get_perimeter(L[i * 2], L[i * 2 + 1])
        difference = 0
        for j in range(i + 1, len(L) // 2):
            if is_overlapped(L[i * 2], L[i * 2 + 1], L[j * 2], L[j * 2 + 1]) == 1:
                difference += get_perimeter(L[j * 2], L[j * 2 + 1])
            if is_overlapped(L[i * 2], L[i * 2 + 1], L[j * 2], L[j * 2 + 1]) == 2:
                difference = get_perimeter(L[i * 2], L[i * 2 + 1])
                break
            if is_overlapped(L[i * 2], L[i * 2 + 1], L[j * 2], L[j * 2 + 1]) == 3:
                if (L[i * 2][0] + L[i * 2 + 1][0]) == (L[j * 2][0] + L[j * 2 + 1][0]):
                    difference = min(abs(L[i * 2][0] - L[i * 2 + 1][0]), abs(L[j * 2][0] - L[j * 2 + 1][0])) * 2
                else:
                    difference += (abs((L[i * 2][0] - L[i * 2 + 1][0]) / 2 ) + abs((L[j * 2][0] - L[j * 2 + 1][0]) / 2) \
                              - abs((L[i * 2][0] + L[i * 2 + 1][0]) / 2 - (L[j * 2][0] + L[j * 2 + 1][0]) / 2)) * 2
                if (L[i * 2][1] + L[i * 2 + 1][1]) == (L[j * 2][1] + L[j * 2 + 1][1]):
                    difference += min(abs(L[i * 2][1] - L[i * 2 + 1][1]), abs(L[j * 2][1] - L[j * 2 + 1][1])) * 2
                else:
                    difference += (abs((L[i * 2][1] - L[i * 2 + 1][1]) / 2) + abs((L[j * 2][1] - L[j * 2 + 1][1]) / 2) \
                              - abs((L[i * 2][1] + L[i * 2 + 1][1]) / 2 - (L[j * 2][1] + L[j * 2 + 1][1]) / 2)) * 2
        perimeter_all -= difference
    return  perimeter_all

print('The perimeter is:', int(get_perimeter_all()))

