
import sys

# push
def plus(num):
    stack.append(num)
    # answer.append('+')
    print("+")
    
# pop
def minus():
    stack.pop()
    # answer.append('-')
    print("-")
 
stack=[]
answer=[] # 결과 출력 리스트
start=1 # 시작포인터

  
n=int(input())

for _ in range(n):
    num=int(sys.stdin.readline()) # 입력하는 정수

    if not stack or stack[-1]<num: # 스택이 비었음 or 스택의 top < 입력하는 정수
        #push and pop
        for i in range(start,num+1):
            plus(i) # push
        minus() # pop
        start=num+1
        print("start: %d" % start)
        print(stack)
        
    elif stack[-1]==num: # 스택에 num이 존재, 스택의 top == 입력하는 정수
        #pop
        minus()
        print("start: %d" % start)
        print(stack)

    elif stack[-1]>num: # 스택의 top > 입력하는 정수 (불가능한 경우)
        #NO!
        print('NO')
        sys.exit()

# for _ in answer: # +-결과 한꺼번에 출력
#     print(_)
