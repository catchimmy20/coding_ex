# 10807
# 10871과 동일한 이유로 틀림.

N = int(input())
a = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in a:
    if i == v:
        cnt += 1

print(cnt)
    