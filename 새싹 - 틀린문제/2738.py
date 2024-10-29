# 2738 행렬 구분 잘하자 N*M행렬
# n = row, m = col
n, m = map(int, input().split())
A = list()
B = list()

# list comprehension
# 0으로 2차원 리스트 초기화
C = [[0 for j in range(m)] for i in range(n)]

for i in range(n): 
    num = list(map(int, input().split()))
    A.append(num)
    
for i in range(n): 
    num = list(map(int, input().split()))
    B.append(num)

for i in range(n):
    for j in range(m):
        C[i][j] = A[i][j] + B[i][j]
        print(C[i][j], end=" ")
    print()

# A, B = [], []

# N, M = map(int, input().split())

# for row in range(N):
#     row = list(map(int, input().split()))
#     A.append(row)

# for row in range(N):
#     row = list(map(int, input().split()))
#     B.append(row)
    
# for row in range(N):
#     for col in range(M):
#         print(A[row][col] + B[row][col], end=' ')
#     print()