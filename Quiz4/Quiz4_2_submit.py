'''
这个是Quiz4_2在ed上的版本，已经通过了testcase，不过效率或许还可以提高
和Quiz4_2不同的地方：
1.ed本身应该是类unix系统或者直接就是linux系统，所以文件分隔符是‘/’而不是‘\’ （line 32）
2.ed目录在/home下，txt都在/home/names里面，所以glob直接路径到 ‘names/*。txt‘就行（line32），Quiz4_2用的os.getcwd（）获取路径
'''

# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
#
# Written by *** and Eric Martin for COMP9021


import os
import glob


first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None



# Replace this comment with your code
all_txt = glob.glob(directory + '/*.txt')

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
                if first_name == tmp_L[0]:
                    popular_name_num_f = int(tmp_L[2])
            if tmp_L[1] == 'M':
                sum_m += int(tmp_L[2])
                if first_name == tmp_L[0]:
                    popular_name_num_m = int(tmp_L[2])
        frequency_f = (popular_name_num_f / sum_f) * 100 if popular_name_num_f else 0
        frequency_m = (popular_name_num_m / sum_m) * 100 if popular_name_num_m else 0
    if frequency_f > min_female_frequency and frequency_f:
        min_female_frequency = frequency_f
        female_first_year = (txt.strip('names/yob')).strip('.txt')
    if frequency_m > min_male_frequency and frequency_m:
        min_male_frequency = frequency_m
        male_first_year = (txt.strip('names/yob')).strip('.txt')

# Replace this comment with your code

if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
         )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
         )

