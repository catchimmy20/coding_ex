# https://school.programmers.co.kr/learn/courses/30/lessons/181832


# 재귀함수 사용
def solution(n):
    global answer
    answer = [[0 for _ in range(n)] for _ in range(n)]
    assign(0, 0, 1, n)
    return answer


def assign(y, x, num, n):
    if n <= 0:
        return answer
    answer[y][x] = num
    for _ in range(1, n):  # →
        x += 1
        num += 1
        answer[y][x] = num
    for _ in range(1, n):  # ↓
        y += 1
        num += 1
        answer[y][x] = num
    for _ in range(1, n):  # ←
        x -= 1
        num += 1
        answer[y][x] = num
    for _ in range(1, n - 1):  # ↑
        y -= 1
        num += 1
        answer[y][x] = num
    return assign(y, x + 1, num + 1, n - 2)

print(solution(4))


# while 사용
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def solution(n):
    answer = [[0] * n for _ in range(n)]
    x, y = 0, 0
    c = 1
    dt = 0

    while c <= n * n:
        answer[x][y] = c
        c += 1
        xx, yy = x + d[dt][0], y + d[dt][1]
        if 0 <= xx < n and 0 <= yy < n:
            if answer[xx][yy] != 0:
                dt = (dt + 1) % 4
                x, y = x + d[dt][0], y + d[dt][1]
            else:
                x, y = xx, yy
        else:
            dt = (dt + 1) % 4
            x, y = x + d[dt][0], y + d[dt][1]

    return answer
