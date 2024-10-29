# 17413 단어뒤집기(스택)
import sys

# 마지막에 공백을 추가 - 문자열의 끝에 도달했음 확인
S = sys.stdin.readline().strip() + ' '
 
# 문자를 임시로 저장할 스택 초기화
stack = [] 

# 최종 결과물 저장할 문자열
result = '' 

# 괄호 안에 있는지 여부, 
# 0 - 괄호 사이가 아님, 
# 1 - 괄호 사이에 존재
cnt = 0 

for i in S :
    if i == '<' :
        # 지금 괄호 안에 있음 표시
        cnt = 1 
        #괄호 만나기 이전 stack 애들 비워주고, 결과 문자열에 더함(뒤집혀서 저장됨)
        for _ in range(len(stack)): 
            result += stack.pop()
    # 현재 문자 스택에 추가
    stack.append(i)
    
    if i == '>' :
         # 지금 괄호 빠져 나왔음 표시 
        cnt = 0
        # 스택에 저장된 문자 pop해서 문자열에 더함. 
        # 스택의 맨앞부터 pop수행 -> <> 사이의 문자는 뒤집어지지 않음.
        for _ in range(len(stack)): 
            # pop(0) - 첫번째 데이터 제거거
            result += stack.pop(0)

    # 공백을 만나고 괄호 밖에 있다면
    if i == ' ' and cnt == 0: 
        # 들어간 공백 뺴주고
        stack.pop() 
        # 스택에 저장된 문자 pop, 문자열에 더함
        # 공백으로 분리된 단어들 뒤집힘
        for _ in range(len(stack)): 
            result += stack.pop()
            
        # 마지막에 공백 살려주기
        result += ' ' 
print(result)
