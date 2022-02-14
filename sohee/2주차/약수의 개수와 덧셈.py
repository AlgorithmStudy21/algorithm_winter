def solution(left, right):
    answer = 0
    for idx in range(left, right + 1):
        num = 0
        for i in range(1, idx + 1):
            if idx % i == 0:
                num += 1
        answer = answer + idx if num % 2 == 0 else answer - idx

    return answer


if __name__ == '__main__':
    solution(13, 17)
    solution(24, 27)
