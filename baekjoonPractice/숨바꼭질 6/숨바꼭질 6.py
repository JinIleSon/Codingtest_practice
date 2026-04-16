import sys
import math

input = sys.stdin.readline

N, S = map(int, input().strip().split())
younger = list(map(int, input().strip().split()))

# math.gcd()는 리스트형태로 넣지 못함. 따라서 gcd를 누적시키는 방식으로 진행
# N이 1일 때(1명일 때)는 최대공약수 의미가 없으니 절대값 그대로 출력
if N == 1:
    print(abs(S - younger[0]))
else:
    subtraction = []

    # 알게된 함수 - abs(음수) = 절대값 표현
    for i in range(N):
        subtraction.append(abs(S - younger[i]))
    
    # 2명을 먼저 누적
    # 만약 2명만 있으면 여기서 끝
    GCD = math.gcd(subtraction[0], subtraction[1])
    
    # 3명부터 누적해 나감
    if N >= 3:
        for i in range(2, N):
            GCD = math.gcd(GCD, subtraction[i])
    print(GCD)