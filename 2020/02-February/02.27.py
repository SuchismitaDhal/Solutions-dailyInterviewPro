# AMAZON
"""
    SOLVED -- LEETCODE#621
    A task is a some work to be done which can be assumed takes 1 unit of time. 
    Between the same type of tasks you must take at least n units of time 
    before running the same tasks again.
    Given a list of tasks (each task will be represented by a string), 
    and a positive integer n representing the time it takes to run the same task again, 
    find the minimum amount of time needed to run all tasks.
"""


def schedule_tasks(tasks, n):
    maxfreq = 0
    e = 0

    freq = dict()
    for t in tasks:
        if t in freq:
            freq[t] += 1
            maxfreq = max(maxfreq, freq[t])
        else:
            freq[t] = 1

    for t in freq:
        if freq[t] == maxfreq:
            e += 1

    return max(len(tasks), (maxfreq - 1) * (n + 1) + e)


print(schedule_tasks(['q', 'q', 'w', 'w'], 3))
# print 6
# one of the possible orders to run the task would be
# 'q', 'w', idle, idle, 'q', 'w'
