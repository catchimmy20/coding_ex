# 1406 에디터 답지
"""
스택을 두개로 쪼개어 생각
두 배열 사이의 공간을 커서라고 간주.

str1        +    str2
________       ________
|_|__|__       __|___|_|

마지막엔 str2를 뒤집어주고 reversed(str2)
출력을 위해 join 사용
"""

import sys

str1 = list(sys.stdin.readline().rstrip())
str2 = []

for _ in range(int(sys.stdin.readline())): # 명령어 개수 입력
    command = list(sys.stdin.readline().split())
    # 커서 왼쪽으로 한칸, 문장 맨앞이면 무시
    if command[0] == 'L': 
        if str1:
            str2.append(str1.pop())
    # 커서 오른쪽으로 한칸, 문장 맨뒤면 무시
    elif command[0] == 'D':
        if str2:
            str1.append(str2.pop())
    # 커서 왼쪽의 문자 삭제
    elif command[0] == 'B':
        if str1:
            str1.pop()
    # P $ - 문자 $ 왼쪽에 추가
    else:
        str1.append(command[1])
        
# extend로 붙일때 str2 뒤집어서 붙여줌        
str1.extend(reversed(str2))
print(''.join(str1))