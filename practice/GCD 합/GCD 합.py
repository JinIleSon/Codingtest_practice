import sys

from math import gcd

input = sys.stdin.readline

t = int(input().strip())

for i in range(t):
    n = list(map(int, input().strip().split()))
    
    result = 0
    for j in range(1, len(n)):
        for k in range(j+1, len(n)):
            # gcd 함수를 사용하면 최대 공약수를 자동으로 만들어줌
            result += gcd(n[j], n[k])
    print(result)


# import sys
# import math
# from collections import deque

# input = sys.stdin.readline

# t = int(input().strip())

# for i in range(t):
#     n = deque(map(int, input().strip().split()))
#     # count = n의 개수
#     count = n.popleft()

#     factorsList = []
#     # 리스트 안에 리스트 형태로 저장하자 - 소인수분해
#     for j in range(count):
#         k = 2
#         factors = {}
#         # n[j]값은 변하면 안 되니 njDummy 넣기
#         njDummy = n[j]
#         while k <= math.sqrt(njDummy) and n[j] != 1:
#             while njDummy % k == 0:
#                 # dict 형태의 factors에 key인 k가 없다면 k에 1이라는 value 부여
#                 if k not in factors:
#                     factors[k] = 1
#                 # 있으면 k의 value += 1
#                 else:
#                     factors[k] += 1
#                 njDummy //= k
#             k += 1
#         # 남은 수는 소수니까 그것도 추가
#         if njDummy != 1:
#             factors[njDummy] = 1
#         factorsList.append(factors)
    
#     miniGcd = 1
#     gcd = 0
#     # dict 형태로 소인수 개수들을 받아서 min으로 최소 개수만 받아서 서로 곱하면 그게 gcd임. 쌍들끼리 모두 더해서 구하면 끝
#     for j in range(count-1):
#         for k in range(j+1, count):
#             # 앞의 dict에서 key를 뽑아서 for문을 돌린 다음
#             miniGcd = 1
#             for l in factorsList[j]:
#                 # 다음 dict에서 key에 해당되는 게 있다면
#                 if l in factorsList[k]:
#                     # key와 둘 중 가장 작은 개수만큼 똑같이 곱해줘야 함(제곱하기)
#                     miniGcd *= l ** min(factorsList[j][l], factorsList[k][l])
#             # 그 값들을 더하기
#             gcd += miniGcd
#     print(gcd)