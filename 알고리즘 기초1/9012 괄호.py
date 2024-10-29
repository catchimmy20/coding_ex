# 9012 괄호

t = int(input())

for i in range(t):
    stack = []
    ps = input()

    for i in ps:
        if i == '(':
            stack.append(i) # push
            # print("%c push" % i)
        elif i == ')':
            if stack:
                stack.pop()
                # print("%c pop" % i)
            else: # 스택에 괄호가 없을 경우 NO
                print("NO")
                break
    else: # break문으로 안끊기고 수행됐을 때
        if not stack: # 스택이 비었다면
            print("YES") # 괄호가 다 맞음
        else: # break안걸렸더라도 괄호가 남아있다면
            print("NO")
            
# T = int(input())

# for i in range(T):
#     stack = []
#     a=input()
#     for j in a:
#         if j == '(':
#             stack.append(j)
#         elif j == ')':
#             if stack:
#                 stack.pop()
#             else: # 스택에 괄호가 없을경우 NO
#                 print("NO")
#                 break
#     else: # break문으로 끊기지 않고 수행됬을경우 수행한다
#         if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
#             print("YES")
#         else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
#             print("NO")