class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)


def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)


# create the tree

root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.left.right.left = Node('g')
root.right.right = Node('f')
root.right.right.left = Node('h')
root.right.right.left.right = Node('j')
root.right.right.right = Node('i')

#print(inOrder(root))

#print(preOrder(root))

print(postOrder(root))



