# APPLE
"""
    You are given two strings, A and B.
    Return whether A can be shifted some number of times to get B.
    Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. 
    A = abc and B= acb should return false.
"""


def getpi(patt):
    pi = [[x, 0] for x in '.' + patt]

    for i in range(2, len(pi)):
        if pi[i][0] == pi[pi[i - 1][1] + 1][0]:
            pi[i][1] = pi[i - 1][1] + 1
    # print(pi)
    return pi


def kmp(str, pi):
    i, j = 0, 0
    while i < len(str):
        print(i, j)
        print(str[i], pi[j + 1][0])
        if str[i] == pi[j + 1][0]:
            i += 1
            j += 1
            if j == len(pi) - 1:
                print('found@', i)
                return True
        else:
            if j == 0:
                i += 1
            else:
                j = pi[j][1]
    return False


def is_shifted(a, b):
    return kmp(a + a, getpi(b))


# print(is_shifted('abcde', 'cdeab'))
# True
print(is_shifted("vcuszhlbtpmksjleuchmjffufrwpiddgyynfujnqblngzoogzg",
                 "fufrwpiddgyynfujnqblngzoogzgvcuszhlbtpmksjleuchmjf"
                 ))
