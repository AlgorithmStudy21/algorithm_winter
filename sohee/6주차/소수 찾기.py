from itertools import permutations


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    result = []
    for i in range(1, len(numbers) + 1):
        item = set(int(''.join(x)) for x in list(permutations(list(numbers), i)))
        for j in item:
            if j == 0 or j == 1:
                continue
            re = is_prime(j)
            if re:
                result.append(j)

    return len(set(result))


if __name__ == '__main__':
    solution("17")
    solution("011")

