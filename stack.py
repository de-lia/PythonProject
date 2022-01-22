class Stack:
    # attributes
    def __init__(self, size):
        self.top = -1
        self.container = []
        limit = 5
        self.size = size

        if self.size > limit:
            print("Provided size of stack exceeds limit 0f {0}. Size is now {0}".format(limit, limit))
            self.size = limit

    # methods
    def push(self, x):
        if self.is_full():
            print("Stack is full.")
            return
        else:
            self.container.append(x)
            self.top += 1
            return

    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            exiting = self.container[self.top]
            self.container.pop(self.top)
            self.top -= 1
            return exiting

    def is_empty(self):

        return self.top < 0

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        else:
            return self.container[self.top]

    def is_full(self):
        return len(self.container) >= self.size

    def snap(self):
        print(self.container)


my_Stack = Stack(10)

my_Stack.push(1)
my_Stack.snap()

my_Stack.push(2)
my_Stack.snap()

my_Stack.push(3)
my_Stack.snap()

my_Stack.push(4)
my_Stack.snap()

my_Stack.push(5)
my_Stack.snap()

my_Stack.push(6)
my_Stack.snap()

my_Stack.push(7)
my_Stack.snap()

my_Stack.push(8)
my_Stack.snap()

my_Stack.push(9)
my_Stack.snap()
