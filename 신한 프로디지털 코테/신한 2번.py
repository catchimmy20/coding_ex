"""
신한투자증권(프로 디지털 아카데미) 코테 2번

주식을 매매하는 것을 ask라 하고 매도하는 것을 bid라 하자. 이때 매도와 매매 전부 합쳐서 n번만 거래 가능하고 n은 항상 짝수여야 한다. 함수의 형태는 response(bid, ask, n) 이다. 만약 bid값이 ask값보다 작다면 result는 0이 된다.
입력 예시는 다음과 같다.
bid = [100, 50, 150]
ask = [120, 100, 160]
n = 2

출력결과는 result값으로 30이 나온다.
"""

def response(bid, ask, n):
    # 매수(bid)와 매도(ask) 리스트를 (bid, ask) 쌍으로 묶고, bid 값이 큰 순서로 정렬
    transactions = sorted(zip(bid, ask), key=lambda x: x[0], reverse=True)

    result = 0
    for i in range(n//2):  # n은 항상 짝수이므로 n/2번의 거래를 수행
        if transactions[i][0] > transactions[i][1]:  # bid가 ask보다 큰 경우만 거래를 수행
            result += transactions[i][0] - transactions[i][1]  # bid와 ask의 차이를 result에 더함

    return result

bid = [100, 50, 150]
ask = [120, 100, 160]
n = 2
print(response(bid, ask, n))  # 출력: 30
