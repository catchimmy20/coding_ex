# 6096
d = []

# 2차원 배열 입력 받기 
for i in range(19): # 행
    d.append(list(map(int, input().split()))) # 각 행의 요소 입력해서 받음


n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for j in range(19):
      if d[j][y-1] == 0:
          d[j][y-1] = 1
      else:
          d[j][y-1] = 0

      if d[x-1][j] == 0:
          d[x-1][j] = 1
      else:
          d[x-1][j] = 0

print("=================================")
print()

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()