# TWITTER
"""
    SOLVED -- LEETCODE#838
    Given a string with the initial condition of dominoes, where:
    . represents that the domino is standing still
    L represents that the domino is falling to the left side
    R represents that the domino is falling to the right side
    Figure out the final position of the dominoes. 
    If there are dominoes that get pushed on both ends, 
    the force cancels out and that dominoes remains upright.
    Example:
    Input:  ..R...L..R.
    Output: ..RR.LL..RR
"""
from collections import deque


class Solution(object):
    def pushdominoes(self, dominoes):
        # Time: O(n)    Space: O(1)
        n = len(dominoes)
        l = -1
        state = []
        for c in dominoes:
            if c == '.':
                state.append(0)
            if c == 'L':
                state.append(-1)
            if c == 'R':
                state.append(1)

        for i in range(n-1):
            if state[i] > 0 and state[i+1] == 0:
                state[i+1] = state[i] + 1

        for i in range(n-1, 0, -1):
            if state[i] < 0:
                if state[i-1] == 0:
                    state[i-1] = state[i] - 1
                if state[i-1] > 0:
                    if -(state[i] - 1) == state[i-1]:
                        state[i-1] = 0
                    elif -(state[i] - 1) < state[i-1]:
                        state[i-1] = state[i] - 1

        for i in range(n):
            if state[i] == 0:
                state[i] = '.'
            elif state[i] > 0:
                state[i] = 'R'
            else:
                state[i] = 'L'

        return ''.join(state)


print(Solution().pushdominoes('..R...L..R.'))
# ..RR.LL..RR
