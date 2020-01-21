# AIRBNB
"""
    We have a list of tasks to perform, with a cooldown period. 
    We can do multiple of these at the same time, but we cannot run the same task simultaneously.
    Given a list of tasks, find how long it will take to complete the tasks in the order they are input.

    tasks = [1, 1, 2, 1]
    cooldown = 2
    output: 7 (order is 1 _ _ 1 2 _ 1)
"""


def findTime(arr, cooldown):
    # Time : O(n)     Space: O(n), dict is implemented using hashmap
    last = dict()
    if len(arr) == 0:
        return 0
    d = 0

    for i in range(0, len(arr)):
        if arr[i] in last:
            if d - last[arr[i]] > cooldown:
                d += 1
                last[arr[i]] = d-1
            else:
                d = last[arr[i]] + 1 + cooldown + 1
                last[arr[i]] = d-1

        else:
            d += 1
            last[arr[i]] = d-1

    return d


print(findTime([1, 1, 2, 1], 2))
# 7
