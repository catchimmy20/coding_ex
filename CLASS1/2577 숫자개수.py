import sys

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

result = A*B*C
# 숫자를 list로 변환하기
lst = list(map(int, str(result)))
# print(lst)
for i in range(10):
    print(lst.count(i))