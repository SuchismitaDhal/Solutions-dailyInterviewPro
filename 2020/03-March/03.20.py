# GOOGLE
"""
    You are given a hash table where the key is a course code, 
    and the value is a list of all the course codes that are prerequisites for the key. 
    Return a valid ordering in which we can complete the courses. 
    If no such ordering exists, return NULL.
    Example:
    {
    'CSC300': ['CSC100', 'CSC200'], 
    'CSC200': ['CSC100'], 
    'CSC100': []
    }
    This input should return the order that we need to take these courses:
    ['CSC100', 'CSC200', 'CSCS300']
"""
from collections import deque


def courses_to_take(course_to_prereqs):
    # Fill this in.
    order = []
    visited = set()
    Q = deque()

    for c in course_to_prereqs:
        if c not in visited:
            Q.append(c)
            while Q:
                for pre in course_to_prereqs[Q[0]]:
                    if pre in visited:
                        return None
                    Q.append(pre)
                order.append(Q[0])
                visited.add(Q[0])
                Q.popleft()

    return order[::-1]


courses = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
}
print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
