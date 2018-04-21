letters = input('Please input a string of lowercase letters:')
L = []

for i in range(len(letters)):
    L.append(ord(letters[i]))
    
L_2 = list(set(L))
L_3 = []
tmp = []

for i in range(len(L_2)):
    if i == len(L_2) - 1:
        if L_2[i - 1] == L_2[i] - 1:
            tmp.append(L_2[i])
            L_3.append(tmp)
            break
        else:
            break
    if L_2[i] == L_2[i + 1] - 1:
        tmp.append(L_2[i])
    else:
        tmp.append(L_2[i])
        L_3.append(tmp)
        tmp = []

max_L = []

for i in range(len(L_3) - 1):
    max_L = L_3[i + 1] if len(L_3[i]) < len(L_3[i + 1]) else L_3[i]

for i in range(len(max_L)):
    print(chr(max_L[i]),end = '')
    
