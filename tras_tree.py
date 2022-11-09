class Tree:
    def __init__(self, key) -> None:
        self.val = key
        self.left = None
        self.right = None

    def pre_order(self):
        print(self.val, end=' | ')
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):

        if self.left:
            self.left.in_order()
        print(self.val, end=' | ')
        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()

        if self.right:
            self.right.post_order()
        print(self.val, end=' | ')


root = Tree(15)
root.left = Tree(6)
root.right = Tree(20)

root.left.left = Tree(3)
root.left.right = Tree(9)

root.right.left = Tree(18)
root.right.right = Tree(24)

root.left.left.left = Tree(1)
root.left.left.right = Tree(4)

root.left.right.left = Tree(7)
root.left.right.right = Tree(12)

root.right.left.left = Tree(17)

root.pre_order()
print('  ')
root.in_order()
print('  ')
root.post_order()
