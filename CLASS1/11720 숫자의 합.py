# 11720 숫자의 합 
# map()을 사용할 것이 아니라 strip으로 공백제거 후 
# 그냥 for문을 돌려주면 됨.

import sys

sep_n = []
n = int(input())
num = sys.stdin.readline().strip()
for i in num:
    sep_n.append(int(i))
print(sum(i for i in sep_n))