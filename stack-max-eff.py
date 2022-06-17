class StackMax:
    def __init__(self):
        self.items = []
        self.max = -999999999999999
        self.is_sorted = True

    def push(self, x):
        if x > self.max:
            self.max = x
        if bool(len(self.items)) and self.items[-1] > x and self.is_sorted:
            self.is_sorted = False
        self.items.append(x)

    def pop(self):
        if not len(self.items):
            print("error")
        else:
            item = self.items.pop()
            if item == self.max:
                if not len(self.items):
                    self.max = -99999999999999999999999999999999
                else:
                    if self.is_sorted:
                        self.max = self.items[len(self.items) - 1]
                        return
                    new_items = self.items.copy()
                    new_items.sort()
                    self.max = new_items.pop()

    def get_max(self):
        if not len(self.items):
            print("None")
        else:
            print(self.max)


def solution():
    command_count = int(input())
    st = StackMax()
    for i in range(command_count):
        command = input().rsplit()
        if command[0] == "push":
            st.push(int(command[1]))
        elif command[0] == "pop":
            st.pop()
        elif command[0] == "get_max":
            st.get_max()


solution()
