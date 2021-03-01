# Implementing Binary Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return not self.root

    def display(self):
        self._display(self.root, 0)
        print()

    def display(self, p, depth):
        if p is None:
            return
        self._display(p.rchild, depth+1)
        print()

        for i in range(level):
            print()
