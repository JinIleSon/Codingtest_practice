import sys

input = sys.stdin.readline
T = int(input().strip())

N = 0

for i in range(T):
    S = input().strip()
    for j in S:
        if j == '(':
            N += 1
        else:
            N -= 1
            if N < 0:
                print('NO')
                break
    if N == 0:
        print('YES')
    elif N > 0:
        print('NO')
    N = 0