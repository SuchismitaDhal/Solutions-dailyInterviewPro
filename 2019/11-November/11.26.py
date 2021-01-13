# LINKEDIN
"""
	SOLVED -- LEETCODE#223
    Given two rectangles, find the area of intersection.
"""


class Rectangle():
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y


def intersection_area(rect1, rect2):
    # Time:  O(1) 	Space: O(1)
    min_x = max(rect1.min_x, rect2.min_x)
    max_x = min(rect1.max_x, rect2.max_x)
    min_y = max(rect1.min_y, rect2.min_y)
    max_y = min(rect1.max_y, rect2.max_y)

    return (max_x - min_x) * (max_y - min_y) 


rect1 = Rectangle(0, 0, 3, 2)
rect2 = Rectangle(1, 1, 3, 3)

print(intersection_area(rect1, rect2))
# 2
