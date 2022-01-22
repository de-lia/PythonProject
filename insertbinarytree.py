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
                    self. right.insert(data)
        else:
            self.data = data

    def print_tree(self):  # visiting the nodes and printing the tree
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.print_tree()

