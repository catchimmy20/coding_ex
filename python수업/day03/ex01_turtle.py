import turtle

# 터틀 인스턴스 출력
t = turtle.Turtle()

# 화살표를 거북이 모양으로 설정
t.shape("turtle")
# 거북이 이동속도 설정
t.speed(3)
# 앞으로 100만큼 이동
t.forward(100)
# 터틀 그래픽창 유지하면서 종료
turtle.done()