def solution(lottos, win_nums):
    min_score = 0
    for w in win_nums:
        if w in lottos:
            lottos.remove(w)
            min_score += 1

    max_score = min_score + lottos.count(0)
    answer = [min(7 - max_score, 6), min(7 - min_score, 6)]
    return answer


if __name__ == '__main__':
    solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
    solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
    solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
