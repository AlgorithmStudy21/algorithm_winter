def solution(priorities, location):
    doc = max(priorities)
    i = priorities.index(doc)

    if i == location:
        return 1

    num = 1
    priorities[i] = 0
    i += 1
    printed = 0
    while printed < len(priorities):
        doc = max(priorities)
        if priorities[i] == doc:
            num += 1
            printed += 1
            priorities[i] = 0
            if i == location:
                return num
        i = (i + 1) % len(priorities)


if __name__ == '__main__':
    solution([1, 2, 3, 2], 0)
    solution([2, 1, 3, 2], 2)
    solution([1, 1, 9, 1, 1, 1], 0)
