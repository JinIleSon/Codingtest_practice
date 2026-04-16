import sys
from collections import deque

input = sys.stdin.readline

# 입력받을 문자열
S = input().strip()

# 사용할 큐(리스트로 사용해도 가능)
que = deque()

# 순서를 바꿀 큐
orderQue = deque()

# <가 나오면 count = 1, >가 나오면 count = 0
count = 0

# 아이디어
# '<'가 나오면 '>'가 나올 때까지는 순서를 바꾸지 않는다. 계속 넘어간다.
# ' '이 나오면 초기화하여 큐를 재사용한다.
# 순서의 역순이니 큐를 사용하자.

for s in S:
    que.append(s)

for i in range(len(que)):
    # 해당 위치가 '>'면 count = 0
    if que[i] == '>':
        count = 0
        print(que[i], end='')
        continue
    # 해당 위치가 '<'거나 count = 1일 때(괄호 사이인 경우) count = 1 유지
    if que[i] == '<' or count == 1:
        count = 1
        print(que[i], end='')
        continue
    
    # 해당 위치가 공백일 경우 que에 넣지않고 넘어가기
    if que[i] != ' ':
        orderQue.append(que[i])

    # <> 외부의 문자인 경우, 현재 인덱스가 마지막인 경우 - 공백. 이때 글자를 모두 pop하면서 내보냄
    # 또한 다음 인덱스가 '<'로 되어 있다면 모두 pop
    if i == len(que)-1 or que[i] == ' ' or (i < len(que)-1 and que[i+1] == '<'):
        for j in range(len(orderQue)):
            print(orderQue.pop(), end='')
        # 다음 글자가 '<'거나 마지막이면 공백을 넣지 않음
        if (i < len(que)-1 and que[i+1] == '<') or i == len(que)-1:
            continue
        print('', end=' ')