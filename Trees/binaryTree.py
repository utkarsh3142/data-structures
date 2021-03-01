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

    def _display(self, p, depth):
        if p is None:
            return
        self._display(p.rchild, depth+1)
        for i in range(depth):
            print(" ", end=" ")
        print(p.value)
        self._display(p.lchild, depth+1)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, p):
        if p is None:
            return
        print(p.value, " ", end=" ")
        self._preorder(p.lchild)
        self._preorder(p.rchild)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, p):
        if p is None:
            return
        self._preorder(p.lchild)
        print(p.value, " ", end=" ")
        self._preorder(p.rchild)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.value, " ", end=" ")

    def height(self):
        return self._height(self.root)

    def _height(self, p):
        if p is None:
            return 0
        hL = self._height(p.lchild)
        hR = self._height(p.rchild)

        if hL> hR:
            return 1 + hL
        else:
            return 1 + hR


if __name__ == "__main__":

    bt = BinaryTree()
    bt.root = Node("P")
    bt.root.lchild = Node("Q")
    bt.root.rchild = Node("R")
    bt.root.lchild.lchild = Node("A")
    bt.root.lchild.rchild = Node("B")
    bt.root.rchild.lchild =Node("C")

    bt.display()
    print("Preorder: ", bt.preorder())
    print("Inorder: ", bt.inorder())
    print("Postorder: ", bt.postorder())
    print("Height of tree: ", bt.height())

