def solution(numbers):
    return sum([i + 1 for i in range(9)]) - sum(numbers)


if __name__ == '__main__':
    solution([1, 2, 3, 4, 6, 7, 8, 0])
    solution([5, 8, 4, 0, 6, 7, 9])
