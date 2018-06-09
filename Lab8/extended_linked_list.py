# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        if not self.head:
            return

        min_val = self.head.value
        node = self.head
        while node:
            min_val = node.value if min_val > node.value else min_val
            if node.next_node:
                node = node.next_node
            else:
                node.next_node = self.head
                break

        while node:
            if node.next_node.value == min_val:
                self.head = node.next_node
                break
            else:
                node = node.next_node

        tmp_val_1 = node.value
        while node:
            tmp_val_2 = node.next_node.next_node.value
            node.next_node.next_node.value = tmp_val_1
            node = node.next_node.next_node
            tmp_val_1 = tmp_val_2
            if node.next_node is self.head:
                node.next_node = None
                break

    def remove_duplicates(self):
        if not self.head:
            return

        node = self.head
        while node:
            if node.next_node:
                if not node.next_node.next_node:
                    if node.value == node.next_node.value:
                        node.next_node = None
                else:
                    if node.value == node.next_node.value:
                        node1 = node
                        while node.value == node.next_node.value:
                            node = node.next_node
                        node1.next_node = node.next_node
            node = node.next_node





