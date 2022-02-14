from math import sqrt, pow


def solution(n):
    x = sqrt(n)
    if x % 1 == 0:
        return pow(int(x), 2)
    else:
        return -1
