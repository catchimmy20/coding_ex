# 10872 팩토리얼 

n = int(input())

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    return 1 # 0! = 1 이라는 것을 잊지 말자.

print(factorial(n))