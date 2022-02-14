def solution(n):
    _n = n
    x = ''
    while _n:
        x += str(_n % 3)
        _n //= 3
    print(int(x, 3))


if __name__ == '__main__':
    solution(45)
    solution(125)
