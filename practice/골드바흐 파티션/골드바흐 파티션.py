import sys

# 골드바흐의 추측: 두 소수의 합으로 나타내기
# 조건 1. 모든 케이스를 리스트에 저장. 최대값까지 가능한 소수를 리스트로 구현.
# 조건 2. 짝수의 딱 절반까지만 보면 된다.
# 조건 3. 앞에서, 뒤에서 각각 i, j로 변수를 줘서 최소한만 보게끔하기

input = sys.stdin.readline
T = int(input().strip())

testCase = []
for i in range(T):
    testCase.append(int(input().strip()))

primeNumber = []
maxValue = max(testCase)
for i in range(maxValue+1):
    primeNumber.append(True)
# 소수 구하기(가장 큰 값 기준)
i = 2
while i * i <= maxValue:
    j = 2
    while i * j <= maxValue:
        primeNumber[i * j] = False
        j += 1
    i += 1
primeNumber[0] = False
primeNumber[1] = False

# 현재 문제: a가 2일 때부터 한 테스트케이스까지 계속 도는 것(시간복잡도의 문제 발생)
# 시간 복잡도를 줄일 방법: 소수인 값만 반복문에 돌리기

realPrimeNumber = []
for i in range(2, len(primeNumber)):
    if primeNumber[i] == True:
        realPrimeNumber.append(i)

for t in testCase:
    result = 0
    for a in realPrimeNumber:
        if a > (t // 2):
            break
        b = t - a
        if primeNumber[a] == True and primeNumber[b] == True:
            result += 1
    print(result)
