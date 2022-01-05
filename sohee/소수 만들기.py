def solution(nums):
    from itertools import combinations
    _nums = list(sum(x) for x in combinations(nums, 3))
    _nums_dict = {}

    for n in _nums:
        _nums_dict[n] = 1 if n not in _nums_dict else _nums_dict[n] + 1

    answer = 0
    for key, value in _nums_dict.items():
        flag = True
        for i in range(2, key):
            if key % i == 0:
                flag = False
        if flag:
            answer += value

    return answer


if __name__ == '__main__':
    solution([1, 2, 3, 4])
    solution([1, 2, 7, 6, 4])
