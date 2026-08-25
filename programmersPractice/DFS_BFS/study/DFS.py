# graph - 딕셔너리(dict) 형태, key는 노드, value는 그 노드와 연결된 노드들의 리스트

# graph[v]를 했을 때 v와 연결된 노드들의 리스트가 나오는 구조 (인접 리스트 방식)
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

# v - 정수(int) 또는 문자열, 현재 방문 중인 노드 하나
v = 1  # 시작 노드

# - set() 자료형, 방문한 노드들을 저장
visited = set()

def dfs(graph, v, visited):
    visited.add(v)
    for node in graph[v]:
        if node not in visited:
            dfs(graph, node, visited)
    return len(visited)