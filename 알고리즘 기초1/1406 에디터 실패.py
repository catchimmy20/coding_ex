# 무식하게 스왑으로 바꾸려고 생각함.
# 중간에 아니다 싶어서 탈주

import sys

n = sys.stdin.readline() # 문자열 입력
n = list(n)
m = int(sys.stdin.readline()) # 명령어 개수 입력
cursor = len(n)-1
print(n)

for i in range(m):
    command = sys.stdin.readline().split() # 명령어 입력
    if command[0] == 'P': # 커서 왼쪽에 문자 추가
        n.extend('0')
        print(n)
        # n[cursor+1] = n[cursor]
        cursor -= 1 # 커서 인덱스 == '\n'위치
        n[cursor+1] = n[cursor] # 커서 위치 +1       
        n[cursor] = command[1]
        print(n)
    elif command[0] == 'L':
        n[cursor-1], n[cursor] = n[cursor], n[cursor-1]
        print(n)
        
