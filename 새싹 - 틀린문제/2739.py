# 2739 파이썬 print format 

n = int(input())
for i in range(1, 10):
    print("%d * %d = %d" % (n, i, n*i))
    # print(f"{n} * {i} = {n*i}")