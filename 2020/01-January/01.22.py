# TWITTER
"""
    SOLVED -- LEETCODE#1213
    Given 3 sorted lists, find the intersection of those 3 lists.
"""


def intersection(list1, list2, list3):
    # Time: O(n)     Space: O(n)
    temp = []
    sol = []

    # intersection of list1 and list2
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            i += 1
        if list1[i] > list2[j]:
            j += 1
        if list1[i] == list2[j]:
            temp.append(list1[i])
            i += 1
            j += 1

    # intersection of temp and list3
    i = 0
    j = 0
    while i < len(temp) and j < len(list3):
        if temp[i] < list3[j]:
            i += 1
        if temp[i] > list3[j]:
            j += 1
        if temp[i] == list3[j]:
            sol.append(temp[i])
            i += 1
            j += 1

    return sol


print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
# [4]
