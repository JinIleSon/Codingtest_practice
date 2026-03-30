import sys
from math import comb


input = sys.stdin.readline

n, r = map(int, input().strip().split())

# nCr = n! / (r! * (n-r)!)
# 0의 개수만 구하면 되니 n!의 0개수 - (r!의 0개수 + (n-r)!의 0개수)

# 2나 5의 제곱 형식으로 값에 대해 계속 나눠가면서 0의 개수를 구하자.
# 왜냐하면 2 * 5 = 10의 형태와 같이 0이 생기는 경우는 2나 5일 것.
# 따라서 2의 개수가 적을 수도 있고 5의 개수가 적을 수도 있으니 더 적은 것을 기준으로 삼아야 함

fivePower = 5
fiveCount = 0
while n >= fivePower:
    fiveCount += n // fivePower

    if r >= fivePower:
        fiveCount -= r // fivePower

    if (n-r) >= fivePower:
        fiveCount -= (n-r) // fivePower
    
    fivePower *= 5

twoPower = 2
twoCount = 0
while n >= twoPower:
    twoCount += n // twoPower

    if r >= twoPower:
        twoCount -= r // twoPower

    if (n-r) >= twoPower:
        twoCount -= (n-r) // twoPower
    twoPower *= 2

# 2나 5 중 더 작은 개수가 정답
if fiveCount > twoCount:
    print(twoCount)
else:
    print(fiveCount)

# 아래는 시간 초과가 난다. 팩토리얼을 직접 계산했기 때문에.

# nCr = n! / (r! * (n-r)!)
# 끝자리 0의 개수를 출력해야 한다.

# 2중 for문은 절대 금물 - 시간 복잡도 문제

# nFactorial = 1
# rFactorial = 1
# complex = 1

# result = 1

# # 적어도 n이 r보다는 크니까 r! 값이 끝나면 그 값도 저장하자. for문 최소화
# for i in range(2, n+1):
#     nFactorial *= i
#     if i <= r:
#         rFactorial *= i

# # (n-r)!을 구해보자
# for i in range(2, (n-r)+1):
#     complex *= i

# result = nFactorial // (rFactorial * complex)
# result = str(result)

# # 문자열로 만든 뒤 역순으로 0의 개수를 카운트하자
# count = 0
# for i in range(len(result)-1, 0, -1):
#     if result[i] == "0":
#         count += 1
#     else:
#         break

# print(result)
# print(nFactorial)
# print(rFactorial)
# print(complex)

# print(count)