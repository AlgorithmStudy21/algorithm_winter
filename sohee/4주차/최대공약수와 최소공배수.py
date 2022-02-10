from math import gcd


def solution(n, m):
    x = gcd(n, m)
    y = (n*m) // x
    answer = [x, y]

    return answer
