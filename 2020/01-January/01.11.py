#AIRBNB
"""
    SOLVED -- LEETCODE 658
    Given a list of sorted numbers, and two integers k and x, find k closest numbers to the pivot x.
"""

def bsearch(arr, k):
    s = 0
    e = len(arr)
    while e-s > 1:
        m = (e + s) // 2
        if arr[m] == k:
            return (m-1, m)
        if arr[m] < k:
            s = m
        if arr[m] > k:
            e = m
    return (s, e)

def closest_nums(nums, k, x):
    #Time: O(logn + k)  Space: O(1)
    n = len(nums)
    (i, j) = bsearch(nums, x)
    sol = []

    while k:
        if i >= 0:
            if j < n:
                if abs(nums[i] - x) < abs(nums[j] - x):
                    sol.append(nums[i])
                    i -= 1
                else:
                    sol.append(nums[j])
                    j += 1
            else:
                sol.append(nums[i])
                i -= 1
        else:
            sol.append(nums[j])
            j += 1
        k -=1

    return sol
 
print(closest_nums([1, 3, 7, 8, 9], 3, 5))
# [7, 3, 8]
