# GOOGLE
"""
    SOLVED -- LEETCODE#210
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


def visit(c, visiting, visited, order, preq):
    visiting.add(c)
    for x in preq[c]:
        if x in visiting:
            return False
        if x not in visited:
            if not visit(x, visiting, visited, order, preq):
                return False
    visiting.remove(c)
    order.append(c)
    visited.add(c)
    return True


def courses_to_take(course_to_prereqs):
    # Time: O(n)    Space: O(n)
    order = []
    visited = set()
    visiting = set()

    for c in course_to_prereqs:
        if c not in visited:
            if not visit(c, visiting, visited, order, course_to_prereqs):
                return None

    return order


courses = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
}
print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
