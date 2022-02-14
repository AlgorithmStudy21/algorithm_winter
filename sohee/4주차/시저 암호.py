import string


def solution(s, n):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    result = ''
    for x in s:
        if x in lower:
            result += lower[(lower.find(x) + n) % 26]
        elif x in upper:
            result += upper[(upper.find(x) + n) % 26]
        else:
            result += ' '

    return result


if __name__ == '__main__':
    solution("AB", 1)
    solution("z", 1)
    solution("a B z", 4)
    solution(" aBZ", 20)
    solution("y X Z", 1)
