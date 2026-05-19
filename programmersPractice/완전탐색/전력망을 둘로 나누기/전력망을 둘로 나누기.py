# 입력이 100 이하이므로 완전탐색이 가능하다.
# 즉 모든 전선을 한 번씩은 잘라봐도 괜찮음
# !!!입력값을 보고 입력값이 작으면 웬만하면 완전탐색으로 생각하면 됨!!!

# 하나씩 모든 노드를 돌아봐야 한다면, DFS(모든 경로 탐지)나 BFS(최적 경로)를 사용하면 되는데, 이 문제에서는 DFS를 사용

# 모든 전선을 하나씩 잘라보는데, 양쪽에 남는 전선의 수를 각각 DFS로 계산 후
# 그 차이값(v1과 연결된 부분을 a, v2와 연결된 부분을 n-a)을 리스트에 저장
# min(result) 진행하여 최솟값을 return

from collections import defaultdict

def dfs(graph, v, visited):
    visited.append(v)
    for node in graph[v]:
        if node not in visited:
            dfs(graph, node, visited)
    return len(visited)

def solution(n, wires):
    graph = defaultdict(list)
    minValue = 999

    for i in range(len(wires)):
        # DFS는 양방향으로 값을 넣는 게 필수
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])

    # print('graph:', graph)

    for i in range(len(wires)):
        visited = []

        # 전선 잘라내기
        graph[wires[i][0]].remove(wires[i][1])
        graph[wires[i][1]].remove(wires[i][0])

        # v1와 연결된 값의 전선 길이(개수)를 구함
        v1 = dfs(graph, wires[i][0], visited)
        v2 = n - v1

        if minValue > abs(v1 - v2):
            minValue = abs(v1 - v2)
        
        # 전선 원복
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])

    return minValue