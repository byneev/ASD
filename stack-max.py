class StackMax:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not len(self.items):
            print("error")
        else:
            self.items.pop()

    def get_max(self):
        if not len(self.items):
            print("None")
        else:
            max = -9999999999999999
            for item in self.items:
                if max < item:
                    max = item
            print(max)


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
