import sys
# 큐를 사용하기 위해 deque import
from collections import deque

input = sys.stdin.readline

# 명령의 수
N = int(input().strip())

# 넣을 큐
que = deque()

for i in range(N):
    # 입력받는 명령어
    S = input().strip()
    if 'push' in S:
        que.appendleft(S[5:])
    elif 'pop' in S:
        if len(que) > 0:
            print(que.pop())
            continue
        print(-1)
    elif 'size' in S:
        print(len(que))
    elif 'empty' in S:
        if len(que) > 0:
            print(0)
            continue
        print(1)
    elif 'front' in S:
        if len(que) > 0:
            print(que[len(que)-1])
            continue
        print(-1)
    elif 'back' in S:
        if len(que) > 0:
            print(que[0])
            continue
        print(-1)