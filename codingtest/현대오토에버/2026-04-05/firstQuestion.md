# 🗺️ 최단 경로로 모든 블록 방문하기

> **유형**: 비트마스킹 DP (TSP 변형)  
> **난이도**: 골드 2 ~ 골드 1  
> **핵심 알고리즘**: 맨해튼 거리 + 비트마스킹 DP

---

## 📋 문제 설명

`w × h` 크기의 격자에서 `blocks` 리스트에 해당하는 모든 지점을 방문하는 **최단 거리**를 구한다.

- 시작점: `blocks[0]` (오름차순 정렬이므로 항상 가장 작은 번호 = 1번)
- 이동: 4방향
- 장애물: 없음
- 블록 번호: `1 ~ w*h` (1D 번호)

---

## 💡 핵심 아이디어

### 1. 블록 번호 → 좌표 변환

블록 번호 `k`를 격자 좌표로 변환한다.

```python
행 = (k - 1) // w
열 = (k - 1) % w
```

### 2. 맨해튼 거리

장애물이 없으므로 BFS 없이 두 좌표 간 거리를 공식으로 바로 계산한다.

```
dist(A, B) = |Ax - Bx| + |Ay - By|
```

### 3. 거리 행렬 전처리

모든 블록 쌍 사이의 거리를 미리 2D 배열로 저장한다.

```
예) blocks = [1, 3, 7], w = 3
좌표: (0,0), (0,2), (2,0)

         (0,0)  (0,2)  (2,0)
(0,0) [   0,     2,     2  ]
(0,2) [   2,     0,     4  ]
(2,0) [   2,     4,     0  ]
```

DP 실행 중 `dist[cur][nxt]` 로 O(1) 조회한다.

### 4. 비트마스킹 DP

각 블록의 방문 여부를 **정수의 비트**로 표현한다.

```
블록 4개 기준:
0b0000 = 0   → 아무것도 방문 안 함
0b0001 = 1   → 0번 블록만 방문
0b0101 = 5   → 0번, 2번 블록 방문
0b1111 = 15  → 전부 방문 완료
```

**핵심 연산**

```python
visited & (1 << i)      # i번 방문 여부 확인
visited | (1 << i)      # i번 방문 처리
(1 << n) - 1            # 전부 방문한 상태
```

**DP 정의**

```
dp[visited][cur] = visited 상태에서 cur에 있을 때 최소 거리
```

**점화식**

```
dp[visited | (1<<nxt)][nxt] = min(dp[visited | (1<<nxt)][nxt],
                                  dp[visited][cur] + dist[cur][nxt])
```

---

## 📝 최종 코드

```python
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
```

---

## ⏱️ 시간 복잡도

| 단계 | 복잡도 |
|------|--------|
| 좌표 변환 | O(N) |
| 거리 행렬 전처리 | O(N²) |
| 비트마스킹 DP | O(2ᴺ × N²) |

N ≤ 10 → `2^10 × 10² = 약 100,000` → **충분히 통과**

---

## 🔍 예시

```
w=3, h=3, blocks=[1, 3, 7]

1번 → (0,0)  ← 시작점
3번 → (0,2)
7번 → (2,0)

경로 1: (0,0) → (0,2) → (2,0) = 2 + 4 = 6
경로 2: (0,0) → (2,0) → (0,2) = 2 + 4 = 6

정답: 6
```

---

## 🔗 관련 문제

| 문제 | 난이도 | 비고 |
|------|--------|------|
| [BOJ 2098 - 외판원 순회](https://www.acmicpc.net/problem/2098) | 골드 1 | TSP 정석 |
| [BOJ 15686 - 치킨 배달](https://www.acmicpc.net/problem/15686) | 골드 1 | 비트마스킹 응용 |
| [BOJ 1102 - 발전소](https://www.acmicpc.net/problem/1102) | 플래티넘 5 | 비트마스킹 DP 심화 |

---

## 📌 유형 인식 팁

> **"모든 ~를 방문/선택하는 최솟값/최댓값"** → 비트마스킹 DP 의심