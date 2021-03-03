# Implementing Binary Search Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return not self.root

    def insert(self, x):
        self.root == self._insert(self.root, x)

    def _insert(self, p, x):
        if p is None:
            p = Node(x)
        elif x < p.value:
            p.lchild = self._insert(p.lchild, x)
        elif x > p.value:
            p.rchild = self._insert(p.rchild, x)
        else:
            print(x, " is already present!")
        return p

    def insert1(self, p, x):
        p = self.root
        par = None
        while p is not None:
            par = p
            if x < p.value:
                p = p.lchild
            elif x > p.value:
                p = p.rchild
            else:
                print(x, " is already present!")

        temp = Node(x)

        if par == None:
            self.root = temp
        elif x < par.value:
            par.lchild = temp
        else:
            par.rchild = temp
