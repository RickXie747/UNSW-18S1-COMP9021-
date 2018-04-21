import copy


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def dfs(node, result, tmp=list()):
    if node is None:
        print('none')
        return

    tmp.append(node)
    print('back')
    print([i.val for i in tmp])
    # 这里需要用拷贝而不是用 = 赋值，也可以遍历赋值
    tmp1 = copy.deepcopy(tmp)

    if node.left is None and node.right is None:
        result.append([i.val for i in tmp])
        print(result)
        print('return')
        return


    if node.left is not None:
        print(f'left ++ {node.left.val}')
        dfs(node.left, result, tmp)

    # 遍历右子树需要带上不同的变量，否则左子树的tmp和右子树的tmp都指向一块内存
    if node.right is not None:
        print(f'right ++ {node.left.val}')
        dfs(node.right, result, tmp1)



if __name__ == '__main__':
    node1 = TreeNode('1')
    node2 = TreeNode('2')
    node3 = TreeNode('3')
    node4 = TreeNode('4')
    node5 = TreeNode('5')
    node6 = TreeNode('6')
    node7 = TreeNode('7')
    node8 = TreeNode('8')
    node9 = TreeNode('9')
    node10 = TreeNode('10')

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node5
    node3.left = node6
    node4.left = node7
    node4.right = node8
    node5.left = node8
    node5.right = node9
    node6.left = node9
    node6.right = node10


    r = []
    dfs(node1, result=r)
    print(r)