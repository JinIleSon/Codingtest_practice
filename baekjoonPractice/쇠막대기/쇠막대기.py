import sys

input = sys.stdin.readline
pipe = input().strip()

count = 0

stack = []

i = 0
while i < len(pipe):
    # '('를 만난 상태 - 파이프를 쌓자.
    if '(' == pipe[i]:
        stack.append(pipe[i])
    # ')'를 만난 상태(레이저) - 파이프를 지나는 개수를 세자
    # 여기서 1을 빼는 이유는 레이저에 해당하는 '('도 포함되기 때문
    elif ')' == pipe[i] and '(' == pipe[i-1]:
        count = count + (len(stack) - 1)
        stack.pop()
        # 파이프 하나가 끝난 시점 - 잘라진 파이프 하나가 더 추가됨
        while i+1 < len(pipe) and ')' == pipe[i+1]:
            stack.pop()
            count += 1
            i += 1
    i += 1
print(count)