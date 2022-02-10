def solution(answers):
    answer = []
    score = [0, 0, 0]

    sol_one = [1, 2, 3, 4, 5]
    sol_two = [2, 1, 2, 3, 2, 4, 2, 5]
    sol_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    iter_one = len(sol_one)
    iter_two = len(sol_two)
    iter_three = len(sol_three)
    iter_ans = len(answers)

    for i in range(int(iter_ans)):
        if sol_one[i % iter_one] == answers[i % iter_ans]:
            score[0] += 1
        if sol_two[i % iter_two] == answers[i % iter_ans]:
            score[1] += 1
        if sol_three[i % iter_three] == answers[i % iter_ans]:
            score[2] += 1

    max_score = max(score)
    for i in range(3):
        if score[i] >= max_score:
            answer.append(i + 1)

    return answer
