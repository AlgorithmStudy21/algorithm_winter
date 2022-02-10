def solution(numbers):
    _numbers = list(map(str, numbers))

    x = []
    for i, val in enumerate(_numbers):
        x.append(((val * 4)[:4], len(val)))

    x.sort(reverse=True)

    answer = ''
    for j in x:
        answer += j[0][:j[1]]

    return "0" if answer.count("0") == len(answer) else answer


if __name__ == '__main__':
    solution([0, 0, 0])
    solution([9, 998])
    solution([67,676,677])
    solution([979, 97, 978, 81, 818, 817])
    solution([6, 10, 2])
    solution([3, 30, 34, 5, 9])
    solution([3, 30, 34, 5, 50, 9])
