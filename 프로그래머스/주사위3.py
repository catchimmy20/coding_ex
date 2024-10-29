# 바로 if문 사용할 시 순서에 따라 값 달라짐
# Counter사용해서 같은게 몇갠지 세기?
# Counter 값에 따라서 연산 진행
def solution(a, b, c, d):
    num = sorted([a, b, c, d])
    print(num)
    if all(n == a for n in num):
        print("전부 같음")
        return 1111 * a


# print(solution(2, 2, 2, 2))
solution(2, 2, 2, 2)
solution(6, 3, 3, 6)
solution(4, 2, 4, 4)
solution(2, 5, 2, 6)
solution(6, 4, 2, 5)
