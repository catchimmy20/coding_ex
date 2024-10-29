# 2744 
# s1 = "rich" 라는 문자열이 있다고하면
# s1.upper() 라는 함수를 이용하면 "rich" 내부의 문자들을 모두 각각 대문자로 변환해서 "새로운" 문자열을 반환

word = str(input())

for i in word:
    if i.isupper() == True: # 대문자라면
        print(i.lower(), end="")
    elif i.isupper() == False: # 소문자라면
        print(i.upper(), end="")

# 문자열 대소문자 전환
# print(word.swapcase())