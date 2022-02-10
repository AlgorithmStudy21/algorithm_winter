def solution(x, n):
    answer = []
    if x == 0:
        return [0] * n

    end = x * n + 1 if x > 0 else x * n - 1
    for i in range(x, end, x):
        answer.append(i)

    print(answer)
    return answer


if __name__ == '__main__':
    solution(0, 5)
    solution(4, 3)
    solution(-4, 5)
