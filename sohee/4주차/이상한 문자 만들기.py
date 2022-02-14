def solution(s):
    _s = s.lower()
    answer = ''
    idx = 0
    for i, x in enumerate(_s):
        if x == ' ':
            answer += ' '
            idx = 0
        else:
            if idx % 2 == 0:
                answer += x.upper()
            else:
                answer += x
            idx += 1

    return answer


if __name__ == '__main__':
    solution("try hello world")
    solution("hello")
