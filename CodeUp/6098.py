# 6098 : [기초-리스트] 성실한 개미(py)

miro = []
for _ in range(10):
    miro.append(list(map(int, input().split())))

# 오른쪽으로 가다가 1을 만나는 경우 
# -> 다시 1나오기 직전으로 가고 거기서 내려감
# 내려가서 0이 반복되면 9로 바꿈 -> 1 나오면 내려감
# 반복
i = 1
j = 1
while i < 9:
    # 시작
    # miro[1][1] = 9
    # for j in range(1, 9):
    if miro[i][j] == 0:
        print("if-1 i, j: ", i, j)
        miro[i][j] = 9
        j += 1  
    # 벽을 만났을 때 -> 아래로
    elif miro[i][j] == 1:
        print("if-2 i, j: ", i, j)
        j -= 1
        i += 1
    elif miro[i][j] == 2:
        miro[i][j] = 9
        break
print("=======================^^...")
for i in range(10):
    for j in range(10):
        print(miro[i][j], end=" ")
    print()
