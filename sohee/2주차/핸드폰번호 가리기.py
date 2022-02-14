def solution(phone_number):
    answer = '*' * (len(phone_number) - 4) + phone_number[-4:]
    return answer


if __name__ == '__main__':
    solution("01033334444")
    solution("027778888")
