# Written by Rick Xie z5192747 for COMP9021


from binary_tree_adt import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        if self.value is None:
            self.value = value
            self.left_node = PriorityQueue()
            self.right_node = PriorityQueue()
            return True
        else:
            if self.value > value:
                self.value, value = value, self.value
            if self.right_node.size() == self.left_node.size():
                return self.left_node.insert(value)
            if self.left_node.size() == 2 ** (self.left_node.height() + 1) - 1:
                return self.right_node.insert(value)
            return self.left_node.insert(value)