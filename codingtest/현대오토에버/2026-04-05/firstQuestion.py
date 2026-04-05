import sys
INF = sys.maxsize

def solution(w, h, blocks):
    n = len(blocks)

    # 블록 번호 → 좌표 변환
    def to_coord(k):
        return ((k - 1) // w, (k - 1) % w)

    coords = [to_coord(b) for b in blocks]

    # 맨해튼 거리 행렬 전처리
    dist = [[abs(coords[i][0] - coords[j][0]) + abs(coords[i][1] - coords[j][1])
             for j in range(n)] for i in range(n)]

    # 비트마스킹 DP
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # 시작점: blocks[0] (항상 1번)

    for visited in range(1 << n):
        for cur in range(n):
            if dp[visited][cur] == INF:
                continue
            for nxt in range(n):
                if visited & (1 << nxt):  # 이미 방문한 블록은 스킵
                    continue
                nvisited = visited | (1 << nxt)
                cost = dp[visited][cur] + dist[cur][nxt]
                if cost < dp[nvisited][nxt]:
                    dp[nvisited][nxt] = cost

    return min(dp[(1 << n) - 1])