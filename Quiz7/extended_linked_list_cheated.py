# Written by **** for COMP9021

'''
这个用了list实现功能，违反了Martin的检测
$ tail -n +8 extended_linked_list.py | egrep ’__|\[|\]’
'''

from linked_list_adt import *


class ExtendedLinkedList(LinkedList):
    def __init__(self, L=None):
        super().__init__(L)

    def rearrange(self):
        if not self.head:
            return
        nodes_value = []
        node = self.head
        while node:
            nodes_value.append(node.value)
            node = node.next_node

        node = self.head
        while node:
            if node.value == min(nodes_value):
                self.head.value = min(nodes_value)
                break
            else:
                node = node.next_node

        node = self.head
        index = nodes_value.index(min(nodes_value))
        for i in range(0, len(nodes_value), 2):
            if not i:
                index -= 1
                self.head.next_node.value = nodes_value[index]
                node = self.head.next_node.next_node
            index = index + 3 if index + 3 < len(nodes_value) else index + 3 - len(nodes_value)
            node.value = nodes_value[index]
            index -= 1
            node.next_node.value = nodes_value[index]
            if node.next_node.next_node:
                node = node.next_node.next_node
            else:
                break

                # Replace pass above with your code



