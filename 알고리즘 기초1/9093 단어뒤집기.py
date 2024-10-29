# 9093 단어뒤집기
"""
reverse를 이용하기 위해서 
문자열을 리스트로 타입을 변환한 다음 reverse 함수를 이용

a.reverse() - 새 목록을 만들지 않음, 리스트 메소드
reversed(객체) - 새 목록을 반환, 내장함수
"""
import sys
t = int(input())

for i in range(t):
    sent = sys.stdin.readline().split()
    for j in sent:
        flip = reversed(j)
        print(''.join(flip), end=" ")
    print()