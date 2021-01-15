# MICROSOFT
"""
    You are given an array of integers. Return the largest product that 
    can be made by multiplying any 3 integers in the array.
    Example:
    [-4, -4, 2, 8] should return 128 as the largest product 
    can be made by multiplying -4 * -4 * 8 = 128.
"""

def maximum_product_of_three(lst):
	negthree = [0, 0, 0]
	posthree = [-1, -1, -1]

	for x in lst:
		if x >= 0: updatepos(posthree, x)
		else:        upda 


print maximum_product_of_three([-4, -4, 2, 8])
# 128
