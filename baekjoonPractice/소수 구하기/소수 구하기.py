import sys

input = sys.stdin.readline

n1, n2 = map(int, input().strip().split())
numberList = []

# 0부터 n2+1까지 소수 후보로 둔다.
for i in range(0, n2+1):
    numberList.append(True)

i = 2
while i * i <= n2:
    j = 2
    # 곱하기 2부터 n2의 값까지 해당 인덱스에 대해(해당 값에 대해) False로 명명한다. 해당 수의 배수는 전부 약수가 되기 때문
    while i * j <= n2:
        if numberList[i * j] == True:
            numberList[i * j] = False
        j += 1
    i += 1

# 0부터 n1 이전까지는 애초에 i로 들어가지 않기 때문에 생각하지 않아도 된다.
for i in range(n1, n2+1):
    # 0이거나 1인 값은 소수가 아니니 넘어간다.
    if i == 0 or i == 1:
        continue
    # 남은 True들은 소수니 그대로 출력
    if numberList[i] == True:
        print(i)

# 아래 부분은 시간 복잡도를 고려하지 않아 시간 초과가 뜨는 경우이다.

# import sys
# import math

# n1, n2 = map(int, input().strip().split())

# for n in range(n1, n2+1):
#     if n == 1:
#         continue
#     if n == 2 or n == 3:
#         print(n)
#         continue
#     # 막힌 부분: 왜 시간 초과가 뜨는가?
#     # 아무래도 i를 2부터 끝까지 돌리는 게 문제가 되는 듯하다.
#     # n // 2인 값부터 아래로 내려가면서 시작하면 시간복잡도가 많이 내려갈 거 같은데
#     # i가 2일 때부터 n // 2까지 가는 것도 시간 초과가 뜬다.
#     # 다른 방법을 생각해보자.
#     # 소인수분해는? -> 결국 이것도 하나씩 나눠야 함
#     # 루트n * 루트n이면 n이니까 이 루트n보다 크면 n2라고 했을 때 n2 * n2는 n보다 항상 클테니까 루트n보다 작은 부분까지만 보면 된다.. <- 핵심
#     i = 2
#     # math 함수로 계속 계산시키는 것은 시간 복잡도를 올린다.
#     # 따라서 변수에 저장한 뒤에 진행한다.
#     root = math.sqrt(n)
#     floor = math.floor(root)
#     # 짝수는 무조건 2로 나눠지니 홀수만 해볼까? <- 아닌듯
#     # <=로 해야 완전 제곱수도 i에 포함시켜서 결과낼 수 있다.
#     while i <= root:
#         if n % i == 0:
#             break
#         if i == floor and n % i != 0:
#             print(n)
#             break
#         i += 1