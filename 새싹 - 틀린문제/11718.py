# 11718 그대로 출력하기
# try except로 에러잡기

a = []
while True:
    try:
        x = input()
    except EOFError: # 런타임에러 발생시
        break
    a.append(x)
    
for i in range(len(a)):
    print(a[i])