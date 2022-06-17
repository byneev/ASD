import sys


class MyQueueSized:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.current_size = 0
        self.head = 0
        self.tail = 0

    def push(self, x):
        if self.current_size < self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.current_size += 1
        else:
            print("error")

    def pop(self):
        if not self.current_size:
            print("None")
        else:
            old_head = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.current_size -= 1
            print(old_head)

    def peek(self):
        if not self.current_size:
            print("None")
        else:
            print(self.queue[self.head])

    def size(self):
        print(self.current_size)


def solution():
    command_count = int(input())
    max_size = int(input())
    queue1 = MyQueueSized(max_size)
    for i in range(command_count):
        command = sys.stdin.readline().rsplit()
        if command[0] == "push":
            queue1.push(command[1])
            continue
        if command[0] == "pop":
            queue1.pop()
            continue
        if command[0] == "peek":
            queue1.peek()
            continue
        if command[0] == "size":
            queue1.size()
            continue


solution()
