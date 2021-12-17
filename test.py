import math
import sys

# 호텔 호수 계산
repeat = int(sys.stdin.readline())
for _ in range(repeat):
    a,b,c = list(map(int, sys.stdin.readline().split()))
    X = (c-1)//a+1
    Y = (c-1)%a+1
    result = int(f'{str(Y)+str(X).zfill(2)}')
    print(result)