import sys

L = []

try:
    file = input('Which data file do you want to use? ')
    with open(file,'r') as f:
        for line in f.readlines():
            L.append(line[2]+line[4])
except IOError:
    print('There is no ' + file)
    sys.exit()

L_2 = L[:]
L_3 = []

def get_path(fact):
    fact_2 = fact
    for i in range(len(L)):
        print(i)
        if fact[-1] == L[i][0]:
            fact_2 += L[i][1]
            L_3.append(fact_2)
            get_path(fact_2)
    return L_3     # all redundant fact

def remove_redundant(redundant_fact):
    for i in range(len(L)):
        for j in range(len(redundant_fact)):
            if redundant_fact[j][0] + redundant_fact[j][-1] == L[i]:
                if L_2.count(L[i]):
                    L_2.remove(L[i])

for i in range(len(L)):
    remove_redundant(get_path(L[i]))

print('The nonredundant facts are:')
for i in range(len(L_2)):
    print(f'R({L_2[i][0]},{L_2[i][1]})')

print(L_3)
print(L)




