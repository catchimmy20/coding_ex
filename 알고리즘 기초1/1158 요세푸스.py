# 1158 요세푸스 - 원형큐 deque 모듈로

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

# 1~n까지 덱 생성
queue = deque([i for i in range(1, n+1)])

# 출력 형식 맞춤
print("<", end='')    

while True: # 덱이 없을 때까지 반복
    # k-1번째 사람까지는 원에서 제거되지 않고 원의 끝으로 이동
    for _ in range(k-1):
        # 덱의 왼쪽 값을 꺼내 제거하고 다시 덱의 오른쪽에 추가
        queue.append(queue.popleft())
        # print(queue)
        
    # k번째 사람 원에서 제거(가장 왼쪽값=맨 앞 출력&제거)
    print(queue.popleft(), end='')
    # print(queue)
    
    # 덱에 값이 남아있다면 , 출력.(형식 맞춤) 
    if queue:
        print(', ', end='')
    else:
        break
print(">")