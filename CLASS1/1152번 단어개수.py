# 1152번 단어개수 세는 문제

import sys

s = sys.stdin.readline().split()
cnt = 0
for i in s:
    cnt += 1
print(cnt)

# 다른 버전
import sys

sentence = sys.stdin.readline().strip() # 문장 입력 받기
words = sentence.split() # 공백을 기준으로 문장 분리
print(len(words)) # 단어의 개수 출력

# 
"""
if) 단어의 개수가 아니라 서로 다른 알파벳 개수를 세는 문제라면?
-----------------------------------------------------
서로 다른 알파벳의 개수를 세려면, 파이썬의 set 자료형을 사용하면 편리함. 
set은 중복을 허용하지 않는 자료형이므로, 같은 알파벳이 여러 번 나오더라도 한 번만 카운트.

먼저, 모든 문자를 소문자나 대문자로 통일시킨 후 
(알파벳의 대소문자를 구분하지 않는다는 가정 하에) 
set에 넣고, 그 크기를 출력하면 됨.
"""
import sys

sentence = sys.stdin.readline().strip() # 문장 입력 받기
alphabets = set() # 중복을 허용하지 않는 set 생성
for char in sentence: # 각 문자를 순회
    if char.isalpha(): # 문자가 알파벳인 경우
        alphabets.add(char.lower()) # 알파벳을 소문자로 변환하고 set에 추가
print(len(alphabets)) # 서로 다른 알파벳 개수 출력

