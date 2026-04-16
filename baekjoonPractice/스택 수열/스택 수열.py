import sys

input = sys.stdin.readline
n = int(input().strip())

# 입력되는 값
target = 0

# 스택 리스트
stack = []

# 출력을 담을 리스트
result = []

# 이때까지 나온 값 중 최대값
maxValue = 0

for i in range(n):
    target = int(input().strip())
    if len(stack) == 0 or stack[-1] < target:
        for j in range(maxValue+1, target+1):
            stack.append(j)
            result.append('+')
            if maxValue < j:
                maxValue = j
    if len(stack) > 0 and stack[-1] == target:
        result.append('-')
        stack.pop()
    if len(stack) > 0 and stack[-1] > target:
        result.clear()
        result.append('NO')
        break
for i in range(len(result)):
    print(result[i])