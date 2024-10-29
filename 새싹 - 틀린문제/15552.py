# 15552 sys.stdin.readline()을 사용해야만 넘어가는 문제
# 그냥 map(int, input().split)으로는 시간초과다

import sys

T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)