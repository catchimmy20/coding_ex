# newline 설정 시 \n 무시
f = open("./for.txt", "r", encoding="utf-8", newline="")
print(f)
line = f.readline()
while line:
    print(line)
    line = f.readline()