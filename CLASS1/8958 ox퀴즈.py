"""
8958 ox퀴즈
lambda, reduce 활용
"""
from functools import reduce
import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    s = sys.stdin.readline().strip()
    s = s.split('X')
    result = 0
    for i in s:
        if i:
            # O의 개수를 셈
            n = i.count('O')
            # lambda, reduce를 사용한 누적합
            result += reduce(lambda a, b: a+b, range(1, n+1))
    print(result)
    
# 다른 버전
import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    s = sys.stdin.readline().strip()
    splits = s.split('X')

    result = 0
    for s in splits:
         # 연속된 'O'의 개수
        length = len(s)
        # 1부터 'O'의 개수까지의 합을 점수에 더함
        # 등차수열의 합 공식을 이용
        # 'O'의 연속 길이가 n일 때 점수는 1부터 n까지의 합인 n*(n+1)/2
        result += length * (length + 1) // 2 

    print(result) 

