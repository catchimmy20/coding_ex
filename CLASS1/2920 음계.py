# 2920 음계
"""
https://dandyrilla.github.io/2017-08-08/python-all-zip/

https://blockdmask.tistory.com/564

"""
import sys

scale = list(map(int, sys.stdin.readline().split()))

if scale[0] < scale[1]: # asc
    # is_sorted = (sorted(scale) == scale)
    is_sorted = all(scale[i] < scale[i+1] for i in range(len(scale)-1))
    if is_sorted == True:
        print("ascending")
    else:
        print("mixed")
else: # desc
    # is_sorted = (sorted(scale, reverse=True) == scale)
    is_sorted = all(scale[i] > scale[i+1] for i in range(len(scale)-1))
    if is_sorted == True:
        print("descending")
    else:
        print("mixed")