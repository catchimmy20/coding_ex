# 10871: X보다 작은수
# 문제 자체를 이해못함. 입력에 임의로 넣는 것임. 

# N, X입력받기
n, x = map(int, input().split())
# 둘째 줄에 입력되는 숫자를 num리스트에 넣음
num = list(map(int, input().split()))

for i in range(n):
    if num[i] < x:
        print(num[i], end=" ")