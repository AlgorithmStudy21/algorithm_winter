def solution(absolutes, signs):
    answer = 0
    for i, val in enumerate(absolutes):
        answer = answer + val if signs[i] else answer - val

    return answer


if __name__ == '__main__':
    solution([4, 7, 12], [True, False, True])
    solution([1, 2, 3], [False, False, True])
