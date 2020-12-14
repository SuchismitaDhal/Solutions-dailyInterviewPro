# UBER
"""
    SOLVED -- LEETCODE#42
    You have a landscape, in which puddles can form.
    You are given an array of non-negative integers representing the elevation at each location.
    Return the amount of water that would accumulate if it rains.

    For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
           X               
       X...XX.X              
     X.XX.XXXXXX                   
    # [0,1,0,2,1,0,1,3,2,1,2,1]
    X reprecents the surface of the mountain any . represent clogged water
"""

def capacity(arr):
    # Time: O(n)    Space: O(n)
    n = len(arr)
    if n == 0: return 0
    leftHigh = [0 for _ in range(n)]  
    rightHigh = [0 for _ in range(n)]
    
    leftHigh[0] = arr[0]
    for i in range(1, n):
        leftHigh[i] = max(leftHigh[i-1], arr[i])

    rightHigh[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        rightHigh[i] = max(rightHigh[i+1], arr[i])

    sol = 0
    for i in range(n):
        sol += max(0, min(leftHigh[i], rightHigh[i]) - arr[i])

    return sol

print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6