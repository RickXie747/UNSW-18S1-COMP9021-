# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
#
# Written by *** and Eric Martin for COMP9021


import os


first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

# Replace this comment with your code
current_year_male = {}
current_year_female = {}
first_name_tally_male = {}
first_name_tally_female = {}
for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    with open(directory + '/' + filename, 'r') as data_file:

        for line in data_file:
            name, gender, tally = line.split(',')
            year = int(filename[3: 7])
            if tally.endswith('\n'):
                tally = int(tally[0:len(tally)-1])
            else:
                tally = int(tally)
            if gender == 'M' and year not in first_name_tally_male:
                first_name_tally_male[year] = tally
            elif gender == 'M' and year in first_name_tally_male:
                first_name_tally_male[year] += tally

            if gender == 'F'and year not in first_name_tally_female:
                first_name_tally_female[year] = tally
            elif gender == 'F' and year in first_name_tally_male:
                first_name_tally_female[year] += tally

            if gender == 'M' and first_name.lower() == name.lower():
                current_year_male[year] = tally

            if gender == 'F' and first_name.lower() == name.lower():
                current_year_female[year] = tally
print('Male++++',current_year_male)
print('Female++++',current_year_female)
print('Total Male',first_name_tally_male)
print('Total Female',first_name_tally_female)
if current_year_male:
    male_first_year = max(current_year_male, key = current_year_male.get)

if current_year_female:
    female_first_year = max(current_year_female, key = current_year_female.get)

min_male_frequency = 0
min_female_frequency = 0

if male_first_year in current_year_male:
    min_male_frequency = current_year_male[male_first_year] / first_name_tally_male[male_first_year] * 100

if female_first_year in current_year_female:
    min_female_frequency = current_year_female[female_first_year] / first_name_tally_female[female_first_year] * 100

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
