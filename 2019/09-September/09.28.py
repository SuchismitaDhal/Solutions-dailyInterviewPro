# MICROSOFT
"""
    Given a time in the format of hour and minute,
    calculate the angle of the hour and minute hand on a clock.
"""


def calcAngle(h, m):
    am = m * 6          # angle made by minute hand with 0
    ah = h * 30         # angle made by hour hand with 0
    ad = int(m / 2)  # angle difference in hour hand due to minutes passed
    ah = ah + ad
    a = abs(am-ah)

    # assuming we need the acute angle formed by the hands
    return min(a, 360-a)


print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165

#   my test cases
print(calcAngle(1, 45))
# 142
print(calcAngle(8, 35))
# 47
