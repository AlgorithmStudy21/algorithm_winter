def solution(num):
    cnt = 0
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num *= 3
            num += 1
        cnt += 1
        if cnt == 500:
            return -1
    return cnt


if __name__ == '__main__':
    solution(6)
    solution(16)
    solution(626331)
