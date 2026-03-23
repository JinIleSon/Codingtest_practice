import sys

input = sys.stdin.readline

N = int(input().strip())
number = list(map(int, input().strip().split()))

stack = []
result = []
freq = []

maxValue = 0

# 최대값 maxValue로 리스트 공간 개수 세기
# result에는 N개의 공간이 필요함
for i in range(N):
    if number[i] > maxValue:
        maxValue = number[i]
    result.append(0)

# freq 리스트(인덱스에 따른 number 횟수) 공간 생성
for i in range(maxValue):
    freq.append(0)

# freq에는 number의 값에 해당하는 인덱스를 '인덱스'로 쓸거니까 공간을 1개 더 추가
freq.append(0)

# 해당 인덱스마다 해당되는 값에 대해 몇 번 나왔는지 체크
# 이중 for문을 사용하면 시간복잡도가 O(N^2)일텐데????
# 스택으로 어떻게 이걸 풀어나가지?
# 미해결 원소의 기준?

# 해당 인덱스 위치를 number 리스트에서 나온 값에 대한 횟수로 값을 정하자. 이렇게 하면 이중 for문 피할 수 있다.
# freq 리스트에 횟수 넣기 = '횟수' 리스트 완성
for i in range(N):
    freq[number[i]] += 1

for i in range(N):
    # 결과 result[i]에는 number[i]가 나와야 함
    # stack에는 미해결 인덱스를 넣기
    while len(stack) > 0 and freq[number[stack[-1]]] < freq[number[i]]:
        # 해당되는 인덱스는 어떻게 찾지? result의 인덱스로 넣어야 될 텐데
        result[stack[-1]] = number[i]
        stack.pop()
    stack.append(i)

# 만약 result에 0으로 된 부분이 있으면 미해결 부분이니 -1로 채우기
for i in range(N):
    if result[i] == 0:
        result[i] = -1

for i in range(N):
    print(result[i], end=' ')