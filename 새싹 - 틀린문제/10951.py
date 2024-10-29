# 10951 - 수가 입력되지 않아서 에러가 발생하면 반복문을 끝낼 수 있도록 try except문 사용

# 실패 - 아무리봐도 종료조건이 없어서 그냥 냅다 for문 5번 돌리기^^;
# arr = list()
# for i in range(5):
#     a, b = map(int, input().split())
#     arr.append(a+b)
    
# for i in range(5):
#     print(arr[i])

# 입력 다 끝나고 나서 출력일 것이라 생각했는데 아니어도 되나보다. 
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break