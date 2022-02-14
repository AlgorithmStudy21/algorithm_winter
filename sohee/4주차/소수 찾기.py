def solution(n):
    flag = [True] * (n + 1)
    _n = int(n ** 0.5)
    for i in range(2, _n + 1):
        if flag[i]:
            for j in range(i * i, n + 1, i):
                flag[j] = False
    answer = 0
    for i in range(2, n + 1):
        if flag[i]:
            answer += 1
    print(answer)


if __name__ == '__main__':
    solution(10)
    solution(5)
