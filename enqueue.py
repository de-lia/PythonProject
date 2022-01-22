class Queue:
    def __init__(self, len):
        self.container = []
        self.front = -1
        self.back = -1
        self.length = len

    def is_empty(self):
        return len(self.container) == 0

    def en_queue(self, value):
        if self.is_empty():
            self.front += 1
            self.back += 1
        else:
            self.back += 1
        self.container.append(value)

    def de_queue(self):
        if self.is_empty():
            return None
        else:
            self.container.pop(self.front)
            self.back -= 1

    def is_full(self):
        if len(self.container) >= self.length:
            return True
        else:
            return False

    def snap(self):
        print(self.container)


q1 = Queue(10)

q1.en_queue(1)
q1.snap()

q1.en_queue(4)
q1.en_queue(9)
q1.snap()

q1.de_queue()
print(q1.back)
q1.snap()