def solution(participant, completion):
    participant.sort()
    completion.sort()

    answer = ''
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]


if __name__ == '__main__':
    solution(["leo", "kiki", "eden"], ["eden", "kiki"])
    solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
    solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]	)
