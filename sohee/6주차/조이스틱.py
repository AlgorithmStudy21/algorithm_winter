def solution(name):
    diff = []
    for n in name:
        diff.append(min(ord(n) - ord('A'), ord('Z') - ord(n) + 1))

    movement = len(name)
    for i, char in enumerate(name):
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        movement = min(movement, i + i + len(name) - next_i)

    answer = sum(diff) + movement
    return answer


if __name__ == '__main__':
    solution("JEROEN")
    solution("JAN")
