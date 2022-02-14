def solution(n, a, b):
    answer = 0
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

    return answer


if __name__ == '__main__':
    solution(8, 4, 7)
    solution(16, 6, 12)
    solution(16, 1, 2)
    solution(16, 1, 3)
    solution(16, 1, 4)
    solution(16, 1, 6)
