from collections import deque

def bfs(graph, start, target):
    visited = set()
    queue = deque([(start, 0)]) # 초반 튜플 형식 유지를 위해 []로 감쌈
    visited.add(start)

    while queue:
        v, dist = queue.popleft()

        if v == target:
            return dist

        for node in graph[v]:
            if node not in visited:
                visited.add(node)
                queue.append((node, dist + 1))

    return -1