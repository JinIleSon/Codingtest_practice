import sys
from collections import deque

input = sys.stdin.readline

t = int(input().strip())

for i in range(t):
    n = deque(map(int, input().strip().split()))
    # count = n의 개수
    count = n.popleft()

    gcd = 0
    minDummy = 0
    for j in range(count):
        for k in range(j+1, count):
            g = 2
            miniGCD = 1
            minDummy = n[j]
            while minDummy != 1 and g <= minDummy:
                # 현재 같은 값으로 계속 나누는 것에 대해서 막힘 다시 해야함
                while minDummy % g == 0 and n[k] % g == 0:
                    miniGCD *= g
                    minDummy //= g
                g += 1
            gcd += miniGCD
    print(gcd)
