# 1926 - BFS 그림그리기

"""
1. 아이디어
- 2중 for문 => 1, 방문X => BFS
- BFS를 돌면서 그림 개수 +1, 최댓값 갱신
 
2. 시간복잡도
- BFS: 0(V+E) = v+4v = 5V
- V: m*n = 500*500
- E: v*4 = 4*500*500
- V+E: 5*250000 = 100만 < 2억 -> 가능

3. 자료구조
- 그래프 전체 지도: int[][]
- 방문: bool[][]
- Queue(BFS)
"""
import sys
input = sys.stdin.readline()

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)] # 방문 횟수

# 상하좌우 방향(세로로)
#     R  D   L  U
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            # 지도 사이즈를 넘어가지 않게함
            if (0 <= ny < n) and (0 <= nx < m):
                # 길이 있고 방문하지 않았다면(새로운 1을 발견했다면)
                if map[ny][nx] == 1 and chk[ny][nx] == False: 
                    rs += 1
                    # 방문한 것으로 바꿔줌
                    chk[ny][nx] = True 
                    q.append((ny, nx))
    return rs

cnt = 0
maxv = 0

# 이중 for문(x*y) -> y먼저 돌고 x돌기
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            # 방문을 True로 해야 다시 방문 안함.
            chk[j][i] = True 
            # 전체 그림 개수를 +1
            cnt += 1
            # bfs > 그림 크기를 구해주고 최대값 갱신  
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)