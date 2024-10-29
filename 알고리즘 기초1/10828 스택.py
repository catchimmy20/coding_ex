# 10828 스택 구현
"""
한 줄을 받을 때는 input을 사용해도 되지만, 
반복문을 통해 입력받을 때는 input함수 사용 시 런타임 에러가 난다.
"""
# 런타임 에러가 왜 자꾸 나는지 모르겠음...
import sys
n = int(sys.stdin.readline().split()) # 명령어 개수
stack = []

for i in range(n):
    com = sys.stdin.readline().split()
    if com[0] == "push":
        stack.append(com[1])
    elif com[0] == 'pop':
        print(stack.pop() if len(stack) != 0 else -1)
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'empty':
        print(1 if stack else 0)
    elif com[0] == 'top':
        # if len(stk) == 0:
        #     print(-1)
        # else: print(stk[-1])
        print(-1 if stack else stack[-1])
        
