import os

first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None
my_data_female = {}
my_data_male = {}
total_stats = {}
current_year_stats = {}

current_year_male = {}
current_year_female = {}

# Replace this comment with your code
for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    with open(directory + '/' + filename) as data_file:
        for line in data_file:
            name, gender, tally = line.split(',')
            year = int(filename[3: 7])
            if tally.endswith('\n'):
                tally = int(tally[0:len(tally) - 1])
            else:
                tally = int(tally)
            if name == first_name:
                first_name_tally = tally
            if gender == 'M' and year not in current_year_male:
                current_year_male[year] = tally
            elif gender == 'M' and year in current_year_male:
                current_year_male[year] += tally
        current_year_male[year] = first_name_tally / current_year_male[year] * 100

print(current_year_male)

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
