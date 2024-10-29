# 10809
import sys

s = sys.stdin.readline().strip()
alpha = [chr(c) for c in range(97, 123)]
for a in alpha:
    if a in s:
        print(s.find(a), end=' ')
    else:
        print(-1, end=' ')