# Comment it before submitting
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def get_node_by_index(node, index):
    if not node:
        return None
    while index:
        node = node.next_item
        index -= 1
    return node


def print_list(node):
    while node:
        print(f"{node.value} -> ", end=" ")
        node = node.next_item


def solution(node, idx):
    next = get_node_by_index(node, idx + 1)
    if not idx:
        return next
    prev = get_node_by_index(node, idx - 1)
    prev.next_item = next
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    # result is node0 -> node2 -> node3


test()
