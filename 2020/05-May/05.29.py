# TWITTER
"""
    SOLVED -- NO SIMILAR PROBLEM FOUND
    You are the manager of a number of employees who all sit in a row. 
    The CEO would like to give bonuses to all of your employees, but since 
    the company did not perform so well this year the CEO would like to keep the bonuses to a minimum.
    The rules of giving bonuses is that:
    - Each employee begins with a bonus factor of 1x.
    - For each employee, if they perform better than the person 
    sitting next to them, the employee is given +1 higher bonus 
    (and up to +2 if they perform better than both people to their sides).
    Given a list of employee's performance, find the bonuses each employee should get.
    Example:
    Input: [1, 2, 3, 2, 3, 5, 1]
    Output: [1, 2, 3, 1, 2, 3, 1]
"""


def getBonuses(performance):
    # Time: O(n)     Space: O(1)
    sol = [1 for i in range(len(performance))]

    for i in range(len(performance)):
        if i - 1 >= 0:
            if performance[i - 1] < performance[i]:
                sol[i] += 1
        if i + 1 < len(performance):
            if performance[i + 1] < performance[i]:
                sol[i] += 1
    return sol


print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]
