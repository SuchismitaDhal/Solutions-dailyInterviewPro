# APPLE
"""
    SOLVED
    You are given a binary tree representation of an arithmetic expression.
    In this tree, each leaf is an integer value, and a non-leaf node is 
    one of the four operations: '+', '-', '*', or '/'.
    Write a function that takes this tree and evaluates the expression.

    Example:

        *
       / \
      +    +
     / \  / \
    3  2  4  5
    This is a representation of the expression (3 + 2) * (4 + 5), and should return 45.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"


def calc(x, y, s):
    switch = {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y
    }
    return switch.get(s)


def evaluate(root):
    # post-order traversal to get postfix expression
    # O(n) time, O(n) space

    stack = list()
    order = list()
    stack.append(root)

    while len(stack):
        n = stack[len(stack) - 1]
        if n.left == None:
            if n.right == None:
                stack.pop()
                if type(n.val) == str:
                    y = order.pop()
                    x = order.pop()
                    order.append(calc(x, y, n.val))
                else:
                    order.append(n.val)
            else:
                stack.append(n.right)
                n.right = None
        else:
            stack.append(n.left)
            n.left = None

    return order[0]


tree = Node(DIVIDE)
tree.left = Node(TIMES)
tree.left.left = Node(2)
tree.left.right = Node(PLUS)
tree.right = Node(3)
tree.left.right.left = Node(2)
tree.left.right.right = Node(1)

# tree = Node(TIMES)
# tree.left = Node(PLUS)
# tree.left.left = Node(3)
# tree.left.right = Node(2)
# tree.right = Node(PLUS)
# tree.right.left = Node(4)
# tree.right.right = Node(5)
print(evaluate(tree))
# 45
