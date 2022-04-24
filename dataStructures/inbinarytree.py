class Node:  # class for the parent node
    def __init__(self, data):
        self.left = None  # initialize the left node and right node to nothing.
        self.right = None
        self.data = data  # set the content of the node to the value of the parent node.

    # methods
    def insert(self, data):
        if self.data:  # compare the new value with the parent node, node.data
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):  # visiting the nodes and printing the tree
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    # Inorder traversal: from the left subtree to the parent node to the right subtree.
    def in_order(self, root):
        my_lis = []
        if root:
            my_lis = self.in_order(root.left)
            my_lis.append(root.data)
            my_lis = my_lis + self.in_order(root.right)
            return my_lis


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print(root.in_order(root))
