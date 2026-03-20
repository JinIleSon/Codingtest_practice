import sys
from collections import deque

input = sys.stdin.readline

# 명령 수 입력
N = int(input().strip())

# 덱 생성
que = deque()

for i in range(N):
    # 명령어 입력
    S = input().strip()
    if 'push_front' in S:
        que.append(S[11:])
    elif 'push_back' in S:
        que.appendleft(S[10:])
    elif 'pop_front' in S:
        if len(que) > 0:
            print(que.pop())
            continue
        print(-1)
    elif 'pop_back' in S:
        if len(que) > 0:
            print(que.popleft())
            continue
        print(-1)
    elif 'size' in S:
        print(len(que))
    elif 'empty' in S:
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in S:
        if len(que) > 0:
            print(que[-1])
            continue
        print(-1)
    elif 'back' in S:
        if len(que) > 0:
            print(que[0])
            continue
        print(-1)