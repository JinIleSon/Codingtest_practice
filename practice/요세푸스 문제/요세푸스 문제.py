import sys
from collections import deque

input = sys.stdin.readline

# N은 사람 수, K는 K번째
N, K = map(int, input().strip().split())

# 순서대로 두 번 뺐다가 맨 뒤에 그걸 다시 넣고를 반복 -> 큐
que = deque()

# 값을 저장할 리스트
result = []

# 전체 큐 구성(1부터 N까지)
for i in range(1, N+1):
    que.append(i)

# 사람 수만큼 반복해야 함
for i in range(N):
    for j in range(K-1):
        que.append(que.popleft())
    result.append(que.popleft())

print('<', end='')
for i in range(N):
    if i < N-1:
        print(result[i], end=', ')
        continue
    print(result[i], end='')
print('>')