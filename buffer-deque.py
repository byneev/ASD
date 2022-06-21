class Buffer_Deque:
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.deque = [None] * max_size
        self.head = 0
        self.tail = 0
        self.current_size = 0
        self.is_prev_action_push = False

    def push_back(self, value):
        if self.current_size == self.max_size:
            print("error")
            return
        self.deque[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.current_size += 1

    def push_front(self, value):
        if self.current_size == self.max_size:
            print("error")
            return
        if self.head == 0 and self.tail == 0:
            self.deque[self.head] = value
            self.head = (self.head - 1) % self.max_size
        else:
            self.head = (self.head - 1) % self.max_size
            self.deque[self.head] = value
        self.current_size += 1

    def pop_back(self):
        if not self.current_size:
            print("error")
            return
        print(self.deque[self.tail])
        self.deque[self.tail] = None
        self.tail = (self.tail - 1) % self.max_size
        self.current_size -= 1
        if not self.current_size:
            self.tail = 0
            self.head = 0

    def pop_front(self):
        if not self.current_size:
            print("error")
            return
        print(self.deque[self.head])
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.current_size -= 1
        if not self.current_size:
            self.tail = 0
            self.head = 0


def solution():
    commands_count = int(input())
    max_size = int(input())
    deque = Buffer_Deque(max_size)
    for i in range(commands_count):
        input_command = input().rsplit()
        if input_command[0] == "push_back":
            deque.push_back(input_command[1])
        elif input_command[0] == "push_front":
            deque.push_front(input_command[1])
        elif input_command[0] == "pop_front":
            deque.pop_front()
        elif input_command[0] == "pop_back":
            deque.pop_back()


solution()
