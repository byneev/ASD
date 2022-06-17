import sys


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class MyLinkedSized:
    def __init__(self):
        self.queue = []
        self.current_size = 0
        self.head = None
        self.tail = None

    def get(self):
        if not self.current_size:
            print("error")
        else:
            prev_head = self.queue.pop(0)
            new_head = prev_head.next
            if new_head:
                self.head = new_head
            else:
                self.head = None
            self.current_size -= 1
            print(prev_head.value)

    def put(self, value):
        node = Node(value)
        if not self.current_size:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.current_size += 1
        self.queue.append(node)

    def size(self):
        print(self.current_size)


def solution():
    command_count = int(input())
    queue1 = MyLinkedSized()
    for i in range(command_count):
        command = sys.stdin.readline().rsplit()
        if command[0] == "put":
            queue1.put(command[1])
            continue
        if command[0] == "get":
            queue1.get()
            continue
        if command[0] == "size":
            queue1.size()
            continue


solution()
