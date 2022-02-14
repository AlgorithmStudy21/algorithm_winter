from collections import deque


def solution(maps):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]

    q = deque()
    q.append([0, 0])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y]

        for i in range(4):
            _dx, _dy = dx[i] + x, dy[i] + y
            if 0 <= _dx < n and 0 <= _dy < m and visited[_dx][_dy] == 0 and maps[_dx][_dy]:
                q.append([_dx, _dy])
                visited[_dx][_dy] = visited[x][y] + 1

    return -1


if __name__ == '__main__':
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
