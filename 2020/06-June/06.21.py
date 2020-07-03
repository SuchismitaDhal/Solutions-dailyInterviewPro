# TWITTER
"""
    SOLVED -- LEETCODE#581
    Given a list of numbers, find the smallest window to sort such that 
    the whole list will be sorted. If the list is already sorted return (0, 0). 
    You can assume there will be no duplicate numbers.
    Example:
    Input: [2, 4, 7, 5, 6, 8, 9]
    Output: (2, 4)
    Explanation: Sorting the window (2, 4) which is [7, 5, 6] will also means that the whole list is sorted.
"""


def min_window_to_sort(nums):
    n = len(nums)
    ld, ls = n, n
    rd, rs = 0, 0

    for i in range(n-1, 0, -1):
        if nums[i] < nums[i - 1]:
            ld = i
            ls = min(ls, ld - 1)
            while ls > 0:
                if nums[ls - 1] <= nums[ld]:
                    break
                else:
                    ls -= 1
    if ld == n:
        return (0, 0)

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            rd = i
            rs = max(rs, rd + 1)
            while rs < n - 1:
                if nums[rs + 1] >= nums[rd]:
                    break
                else:
                    rs += 1

    return (ls, rs)


print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
# (2, 4)
