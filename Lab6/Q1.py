digits = input('Input a number that we will use as available digits:')
goal = int(input('Input a number that represents the desired sum:'))

list = []
for e in digits:
    list.append(int(e))
    
result = []

def find(digits, goal):
    if goal < 0:
        return 0
    if not digits:
        if goal == 0:
            return 1
        return 0
    return find(digits[1:], goal) + find(digits[1:], goal - digits[0])

a = find(list, goal)
print(a)


    
