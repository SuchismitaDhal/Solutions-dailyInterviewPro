# APPLE
"""
    SOLVED -- NO VERIFICATION REQUIRED
    Create a class that initializes with a list of numbers and has one method called sum. 
    sum should take in two parameters, start_idx and end_idx and return the sum of the list 
    from start_idx (inclusive) to end_idx` (exclusive).
    You should optimize for the sum method.
"""


class ListFastSum:
    def __init__(self, nums):
        self.nums = nums
        self.sumtillidx = [0]

        s = 0
        for n in nums:
            s += n
            self.sumtillidx.append(s)

    def sum(self, start_idx, end_idx):
        # Time: O(1)    Space: O(n)
        return self.sumtillidx[end_idx] - self.sumtillidx[start_idx]


print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 5))
# 12 because 3 + 4 + 5 = 12
