import sys
from collections import deque

input = sys.stdin.readline
n1, n2 = map(int, input().strip().split())
n = 2

# 만약 숫자가 n2가 더 크면 순서를 바꿈
if n1 < n2:
    number = n1
    n1 = n2
    n2 = number

# n1, n2의 소인수들을 담을 리스트
n1List = []
n2List = []

# LCM(Least Common Multiple) - 최소 공배수
LCM = 1

# GCD(Greatest Common Divisor) - 최대 공약수
GCD = 1

# 아이디어
# n1, n2를 곱으로 만든 리스트로 구성해서 겹치는 거는 바로 계산하면(최대 공약수) popleft()해서 없애고 나머지 전부 곱하면(최소 공배수)
# 해당 값(인덱스)에서 전부 나눴을 때 소수가 아닌 수는 자동으로 걸러짐

# 근데 끝은 어떻게 잡지? => 나눠지지 않으면 알아서 멈춤

for i in range(2, n1+1):
    if n1 % i == 0:
        n = i
        break

dummy = 0
while n1 % n == 0:
    n1List.append(n)
    n1 //= n
    if n1 % n != 0:
        dummy = n
        for i in range(dummy, n1+1):
            if n1 % i == 0:
                n = i
                break
if n1 != 1:
    n1List.append(n1)

for i in range(2, n2+1):
    if n2 % i == 0:
        n = i
        break

dummy = 0
while n2 % n == 0:
    n2List.append(n)
    n2 //= n
    if n2 % n != 0:
        dummy = n
        for i in range(dummy, n2+1):
            if n2 % i == 0:
                n = i
                break
if n2 != 1:
    n2List.append(n2)

# n1List의 길이만큼 인덱스를 늘려가면서 n2List에는 남아있는 것만 계속해서 while 문으로 돌게끔 함. 이렇게 걸러진 값은 최대 공약수가 됨
for i in range(len(n1List)):
    j = 0
    while j < len(n2List):
        # 만약에 같은 값을 찾으면 n2List의 해당 인덱스를 pop하고 해당 i의 인덱스를 끝내야 함. 이거 때문에 계속 문제가 생김.
        if n1List[i] == n2List[j]:
            GCD = GCD * n2List.pop(j)
            break
        # 만약 n1List의 i인덱스, n2List의 j인덱스에 대한 값이 다르면 j를 1 올려서 순회
        j += 1
print(GCD)

# 최소 공배수는 겹치는 것을 하나씩 제외한 모든 것을 곱함
for i in n1List:
    LCM *= i
for i in n2List:
    LCM *= i

print(LCM)

# 유클리드 호제법
# import sys

# input = sys.stdin.readline
# a, b = map(int, input().split())

# x, y = a, b

# while y != 0:
#     x, y = y, x % y

# gcd = x
# lcm = a * b // gcd

# print(gcd)
# print(lcm)
