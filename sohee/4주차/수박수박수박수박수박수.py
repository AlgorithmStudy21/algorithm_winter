def solution(n):
    text = "수박"
    answer = text * (n // 2)
    if n % 2 == 1:
        answer += text[0]
    print(answer)

    return answer


if __name__ == '__main__':
    solution(3)
    solution(4)
