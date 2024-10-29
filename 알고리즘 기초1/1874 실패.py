# 1874 스택 수열
# 시간초과로 실패

import sys
n = int(sys.stdin.readline())
a = [] # 결과 출력 리스트
stack = []

# n번 돌아가며 입력
for i in range(n):    
    b = int(sys.stdin.readline()) # 두번째 줄부터 입력시작
    if not stack: # 스택이 비었을때
            for j in range(1, b+1):
                if j not in a:
                    stack.append(j) # push
                    print("+")
                    if j == b:
                        stack.pop()
                        print("-")
                        a.append(j)
    elif b in stack:
        if stack[-1] != b:
            print("NO")
            break
        else:
            stack.pop()
            print("-")
            a.append(b)
    elif b not in stack:
        for k in range(stack[-1]+1, b+1):
            if k not in a:
                stack.append(k) # push
                print("+")
        stack.pop()
        print("-")
        a.append(b)