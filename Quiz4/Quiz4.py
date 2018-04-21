'''
忘了用Martin给的代码了
新的放在Quiz4_2里了
'''

import os
import glob

name = input('Enter a first name:')

all_txt = glob.glob(os.getcwd() + '\\names\\*.txt')

frequency_f_all = 0
frequency_m_all = 0

for txt in all_txt:
    with open(txt,'r') as f:
        sum_f = 0
        sum_m = 0
        popular_name_num_f = ''
        popular_name_num_m = ''
        for line in f.readlines():
            tmp_L = line.strip().split(',')
            if tmp_L[1] == 'F':
                sum_f += int(tmp_L[2])
                if name == tmp_L[0]:
                    popular_name_num_f = int(tmp_L[2])
            if tmp_L[1] == 'M':
                sum_m += int(tmp_L[2])
                if name == tmp_L[0]:
                    popular_name_num_m = int(tmp_L[2])
        frequency_f = popular_name_num_f / sum_f if popular_name_num_f else 0
        frequency_m = popular_name_num_m / sum_m if popular_name_num_m else 0
    frequency_f_all = frequency_f if frequency_f > frequency_f_all and frequency_f else frequency_f_all
    frequency_m_all = frequency_m if frequency_m > frequency_m_all and frequency_m else frequency_m_all

if frequency_f:
    print(f'{name} in Female is {frequency_f_all}')
else:
    print(f'no {name} in Female')

if frequency_m:
    print(f'{name} in male is {frequency_m_all}')
else:
    print(f'no {name} in Male')











