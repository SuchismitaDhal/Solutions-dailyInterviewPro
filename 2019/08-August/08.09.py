# TWITTER
"""
    SOLVED -- LEETCODE#155
    Implement a class for a stack that supports all the regular functions
    (push, pop) and an additional function of max() which returns the maximum
    element in the stack (return None if the stack is empty).
    Each method should run in constant time.
"""


class MaxStack:
    def __init__(self):
        # O(n) extra space
        self.maxidx = list()
        self.stack = list()

    def push(self, val):
        self.stack.append(val)

        if len(self.stack) == 1:
            self.maxidx.append(0)
        else:
            if val > self.max():
                self.maxidx.append(len(self.stack) - 1)

    def pop(self):
        if len(self.stack) == 0:
            print("poop operation invalid on empty stomach")
            return

        p = len(self.stack) - 1
        self.stack.pop(p)

        if self.maxidx[len(self.maxidx) - 1] == p:
            self.maxidx.pop(len(self.maxidx)-1)

    def max(self):
        if len(self.maxidx) == 0:
            return None
        return self.stack[self.maxidx[len(self.maxidx)-1]]


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
