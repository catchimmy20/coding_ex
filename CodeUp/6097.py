# 6097 : [기초-리스트] 설탕과자 뽑기(py)

h, w = map(int, input().split())
# 판 만들고
pan = [[0]*w for _ in range(h)]
# 막대 입력받고
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    # 좌표 찾고 -> 방향 설정 -> 길이만큼 1로 설정
    x_idx = x - 1
    y_idx = y - 1 
    if d == 0: # 가로
        for i in range(l):
            pan[x_idx][y_idx] = 1
            y_idx += 1
    elif d == 1: # 세로
        for i in range(l):
            pan[x_idx][y_idx] = 1
            x_idx += 1

for i in range(h):
    for j in range(w):
        print(pan[i][j], end=" ")
    print()
