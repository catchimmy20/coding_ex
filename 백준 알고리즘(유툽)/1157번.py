# 1157번 : 단어 공부
"""
set() - 집합연산의 경우 count() 사용이 안되며 callable하지 않다고 뜸. 
append()가 아닌 add(), remove()가 아닌 discard()를 사용해야됨. 
in 사용가능, update()는 여러데이터를 한번에 추가할때 사용.
"""

import sys 

cnt = [] # 서로 다른 알파벳의 개수를 저장하는 리스트

s = sys.stdin.readline().strip().upper() # 대문자로 변환해서 s에 저장
print(s)
s1 = list(set(s)) # 알파벳 중복 제거
print(s1)


for i in s1:
    cnt.append(s.count(i)) # 서로 다른 알파벳의 개수를 저장
    
print(cnt)


if cnt.count(max(cnt)) > 1: #count숫자 최댓값이 중복되면
    print("?")
    
else:
    max_i = cnt.index(max(cnt)) # count숫자 최댓값 인덱스 위치
    print(s1[max_i])
    


