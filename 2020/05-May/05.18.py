# UBER
"""
    SOLVED -- LEETCODE#155
    Design a simple stack that supports push, pop, top, and 
    retrieving the minimum element in constant time.
        push(x) -- Push element x onto stack.
        pop() -- Removes the element on top of the stack.
        top() -- Get the top element.
        getMin() -- Retrieve the minimum element in the stack.
    Note: be sure that pop() and top() handle being called on an empty stack.
"""


class minStack(object):
    def __init__(self):
        # Space: O(2n)
        self.maxidx = list()
        self.stack = list()

    def push(self, x):
        # Time: O(1)
        self.stack.append(x)

        if len(self.stack) == 1:
            self.maxidx.append(0)
        else:
            if x < self.getMin():
                self.maxidx.append(len(self.stack)-1)

    def pop(self):
        # Time: O(1)
        if len(self.stack) == 0:
            print("poop operation invalid on empty stomach")
            return

        p = len(self.stack) - 1
        self.stack.pop(p)

        if self.maxidx[len(self.maxidx) - 1] == p:
            self.maxidx.pop(len(self.maxidx)-1)

    def top(self):
        # Time: O(1)
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        # Time: O(1)
        if len(self.maxidx) == 0:
            return None
        return self.stack[self.maxidx[len(self.maxidx)-1]]


x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2
