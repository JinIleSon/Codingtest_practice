import sys

input = sys.stdin.readline

# 입력받을 숫자 리스트
numbers = []

while True:
    n = int(input().strip())
    if n == 0:
        break
    numbers.append(n)

# 가장 큰 값 추출(체를 한 번만 돌기 위해)
maxValue = max(numbers)

# 소수만 True인 리스트
decimal = []

# 소수를 담을 숫자 리스트
numberList = []

for i in range(maxValue + 1):
    decimal.append(True)

decimal[0] = False
decimal[1] = False

i = 2
# i 2번 곱하면 maxValue보다 작아야 최소한으로 돌 수 있음
while i * i <= maxValue:
    j = 2
    # 합성수 모두를 False로 바꿈
    while i * j <= maxValue:
        decimal[i * j] = False
        j += 1
    i += 1

for i in range(len(decimal)):
    # 소수 리스트 안에 True로 찍혀있으면 소수니 numberList에 해당 숫자 추가
    if decimal[i]:
        numberList.append(i)

# 알맞은 쌍을 찾아서 print했다면 True로 변경할 변수
found = False

for n in numbers:
    # b는 n에서 a를 뺀 값에 대해 존재해야 하므로 b를 구한 다음 numberList안에 있는지 확인
    for a in numberList:
        b = n - a
        # in을 쓰면 전체 순회를 하기 때문에 인덱스로 접근
        # decimal 리스트는 소수만 True임
        if decimal[b]:
            print(f'{n} = {a} + {b}')
            found = True
            break
if not found:
    print("Goldbach's conjecture is wrong.")