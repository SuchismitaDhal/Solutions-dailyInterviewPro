# GOOGLE
"""
    SOLVED -- LEETCODE#38
    A look-and-say sequence is defined as the integer sequence beginning
    with a single digit in which the next term is obtained by describing
    the previous term. An example is easier to understand:
    Each consecutive value describes the prior value.
        1      #
        11     # one 1's
        21     # two 1's
        1211   # one 2, and one 1.
        111221 # #one 1, one 2, and two 1's.
    Your task is, return the nth term of this sequence
"""


class Solution:
    seq = ['1']     # Static variable

    def countAndSay(self, n: int) -> str:
        if len(Solution.seq) >= n:
            return Solution.seq[n - 1]  # accessing static variable

        prev = self.countAndSay(n - 1)
        sol = []
        count = 1
        for i in range(1, len(prev)):
            if prev[i] != prev[i - 1]:
                sol.append(str(count))
                sol.append(prev[i - 1])
                count = 1
            else:
                count += 1
        sol.append(str(count))
        sol.append(prev[-1])

        Solution.seq.append(''.join(sol))
        return Solution.seq[n - 1]


print(getterm(5))
