def solution(n):
    arr = list(str(n))
    arr.sort(reverse=True)

    return int(''.join(arr))


if __name__ == '__main__':
    solution('118372')
