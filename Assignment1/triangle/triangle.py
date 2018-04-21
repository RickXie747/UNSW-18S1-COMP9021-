import os
import sys

L_num = []
lines = 0

try:
    file_name = input('Which data file do you want to use? ')
    with open(os.getcwd() + '\\' + file_name, 'r') as f:                  # \\ and /
        for line in f.readlines():
            lines += 1
            line_str = line.strip()
            line_str_list = list(line_str.split())
            line_list = [int(i) for i in line_str_list ]
            L_num += line_list
except IOError:
    print('There is no ' + file_name)
    sys.exit()

if L_num == []:
    print('Empty file, try again.')
    sys.exit()

class TriangleNode:
    def __init__(self,val):
        self.val = int(val)
        self.left = None
        self.right = None

for i in range(len(L_num)):
    exec('node' + str(i+1) + '=TriangleNode(\'' + str(int(L_num[i])) + '\')')
for i in range(lines):
    for a in range(i * (i - 1) // 2 + 1, i * (i - 1) // 2 + 1 + i):
        exec('node' + str(a) + '.left=node' + str(a + i))
        exec('node' + str(a) + '.right=node' + str(a + i + 1))

path = ''
all_path = []
path_sum = 0

def dfs(node, path, path_sum, all_path):
    path_sum += node.val
    path += str(node.val)
    if node.left is not None:
        path += ','
        dfs(node.left, path, path_sum, all_path)
    if node.right is not None:
        dfs(node.right, path, path_sum, all_path)
    if node.left is None and node.right is None:
        all_path.append(path)
        all_path.append(path_sum)

dfs(node1, path, path_sum, all_path)

max_path_sum = (max([all_path[i] for i in range(1,len(all_path),2)]))
all_path_list = all_path[all_path.index(max_path_sum) - 1].split(',')

print(f'The largest sum is: {max_path_sum}')
print(f'The number of paths yielding this sum is: {all_path.count(max_path_sum)}')
print(f'The leftmost path yielding this sum is: {[int(i) for i in all_path_list]}')













