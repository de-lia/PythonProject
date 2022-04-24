class Node:
    def __init__(self, data, pointer=None):
        self.next = pointer
        self.data = data

    def __str__(self):
        return "Node[{0} : next<{1}>]".format(self.data, self.next)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            ll_str = "["
            curr = self.head
            while curr is not None:
                ll_str += str(curr.data) + " -> "
                curr = curr.next
            ll_str += "None]"
            return ll_str

    # methods
    def insert_end(self, new_node):
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def is_empty(self):
        return self.head is None


jean = Node("Jean")
kimb = Node("Kimbi")
desm = Node("Desmond")
ayok = Node("Ayoko")

my_ll = LinkedList()
print(my_ll)
my_ll.insert_end(jean)

print(my_ll.head)

my_ll.insert_end(desm)
my_ll.insert_end(ayok)
my_ll.insert_end(kimb)
print(my_ll)