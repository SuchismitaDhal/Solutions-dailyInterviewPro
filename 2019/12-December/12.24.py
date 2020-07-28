# TWITTER
"""
    SOLVED -- NO SIMILAR QUESTION FOUND
    Given a 32-bit integer, swap the 1st and 2nd bit, 3rd and 4th bit, up til the 31st and 32nd bit.
"""
swap = [0, 2, 1, 3]


def swap_bits(num):
    # Time: O(logn)  Space: O(1)
    sol = 0
    p = 1
    while num:
        r = num % 4
        num = num // 4
        sol = swap[r] * p + sol
        p = p << 2
    return sol


print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
# 0b01010101010101010101010101010101
