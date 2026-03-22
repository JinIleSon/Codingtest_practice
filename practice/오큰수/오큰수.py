import sys

input = sys.stdin.readline
N = int(input().strip())
number = list(map(int, input().strip().split()))

stack = []

# result에는 number와 똑같은 길이만큼의 list를 넣어줌
result = number

for i in range(N):
    # 현재 number의 i 인덱스에 대한 값이 스택 내부의 마지막 값보다 크면 pop하고 result 리스트에 추가
    while len(stack) > 0 and number[stack[len(stack)-1]] < number[i]:
        result[stack[len(stack)-1]] = number[i]
        stack.pop()
    stack.append(i)

# 스택에 인덱스가 남으면 결정이 나지 않았다는 거니까 -1로 넣기
for i in stack:
    result[i] = -1

# 출력
for i in range(len(result)):
    print(result[i], end=' ')