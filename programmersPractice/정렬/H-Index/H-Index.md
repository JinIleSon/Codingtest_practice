# Programmers 42747 — H-Index

[![Level 2](https://img.shields.io/badge/난이도-Level%202-orange)](https://school.programmers.co.kr/learn/courses/30/lessons/42747)
[![분류](https://img.shields.io/badge/분류-정렬-blue)](#)

> 논문의 인용 횟수 배열이 주어졌을 때, 과학자의 H-Index를 구하는 문제.

🔗 [문제 보기](https://school.programmers.co.kr/learn/courses/30/lessons/42747)

---

## 목차

- [문제 설명](#문제-설명)
- [입출력](#입출력)
- [헷갈렸던 부분](#헷갈렸던-부분)
- [풀이 접근](#풀이-접근)
- [최종 코드](#최종-코드)
- [복잡도 분석](#복잡도-분석)
- [배운 점](#배운-점)

---

## 문제 설명

어떤 과학자가 발표한 논문 n편 중, **h번 이상 인용된 논문이 h편 이상**이고 나머지 논문이 h번 이하 인용되었다면, h의 최댓값이 이 과학자의 H-Index이다.

| citations | return |
|-----------|--------|
| `[3, 0, 6, 1, 5]` | `3` |

---

## 입출력

**입력**
- `citations` : 길이 1 이상 1,000 이하, 각 원소 0 이상 10,000 이하

**출력**
- H-Index 값 (정수)

---

## 헷갈렸던 부분

**`result`에 무엇을 저장해야 하는가**

초기 풀이에서는 `citations[i] <= count[i]`를 만족할 때 `result = citations[i]`로 저장했다.
그러나 H-Index는 "인용 횟수"가 아니라 **"h편이 h회 이상 인용됐을 때의 h"** 이므로,
저장해야 할 값은 인용 횟수(`citations[i]`)가 아니라 편수(`count[i]`)이다.

**비교 방향 (`<=` vs `>=`)**

처음에 `citations[i] <= count[i]` 방향으로 비교했는데, 이 경우:
- 인용 횟수가 편수보다 작은 상황 → h 후보가 `citations[i]`
- 하지만 "citations[i]편이 citations[i]회 이상 인용됐는가"를 보장할 수 없다

반면 `citations[i] >= count[i]`를 만족하면 오름차순 정렬 특성상,
뒤에 남은 `count[i]`편이 모두 `citations[i]`회 이상임이 보장된다.

**굳이 조건 분기가 필요한가**

특정 조건을 만족하는 경우만 탐색하는 방식 대신,
**모든 index에 대해 `min(citations[i], count[i])`를 구하고 최댓값을 반환**하면
두 조건(인용 횟수 ≥ h, 편수 ≥ h)을 동시에 만족하는 최적의 h를 자연스럽게 찾을 수 있다.

---

## 풀이 접근

### 핵심 아이디어 — 정렬 후 `min(인용횟수, 편수)`의 최댓값

```
핵심 원칙: H-Index는 인용횟수와 편수 두 조건을 동시에 만족해야 하므로,
각 index에서 두 값 중 작은 쪽이 h 후보가 되고, 그 중 최댓값이 정답이다.
```

**Step 1.** `citations`를 오름차순 정렬한다.

**Step 2.** `count` 배열을 내림차순(`[n, n-1, ..., 1]`)으로 만든다.
- `count[i]`는 index i의 논문을 포함해 뒤에 남은 논문의 수를 의미한다.

**Step 3.** 각 index i에서 `min(citations[i], count[i])`를 계산한다.
- `citations[i] >= count[i]` 이면 → h 후보는 `count[i]` (편수가 병목)
- `citations[i] < count[i]` 이면 → h 후보는 `citations[i]` (인용횟수가 병목)
- 어느 경우든 **작은 쪽이 두 조건을 동시에 만족하는 최대 h**이다.

**Step 4.** 모든 후보 중 최댓값을 반환한다.

---

## 최종 코드

```python
def solution(citations):
    citations.sort()

    length = len(citations)

    count = []
    for i in range(length, 0, -1):
        count.append(i)

    result = []
    for i in range(length):
        result.append(min(citations[i], count[i]))

    return max(result)
```

---

## 복잡도 분석

| 항목 | 복잡도 |
|------|--------|
| 시간 복잡도 | `O(n log n)` |
| 공간 복잡도 | `O(n)` |

> `n` = citations의 길이 (최대 1,000)

정렬에 O(n log n), 이후 순회는 O(n). 전체는 정렬이 지배한다.
count와 result 배열을 별도로 저장하므로 공간은 O(n).

---

## 배운 점

**두 조건을 동시에 만족하는 값은 `min`으로 표현된다**

H-Index는 인용횟수 ≥ h 이면서 편수 ≥ h 를 동시에 만족해야 한다.
두 조건을 동시에 만족하는 최대 h는 자연스럽게 `min(인용횟수, 편수)`가 된다.
조건 분기를 복잡하게 세우기 전에, 이처럼 수학적으로 단순화할 수 있는지 먼저 생각해보는 것이 좋다.

**오름차순 정렬 + 내림차순 count의 의미**

정렬된 배열에서 index i의 `count[i]`는 "i번째 논문 포함 뒤에 남은 편수"이다.
오름차순 citations와 내림차순 count가 맞물리는 지점이 H-Index가 가장 커지는 균형점이다.

**터널 비전 주의**

초기 `<=` 방향의 비교와 `citations[i]` 저장에 집착하다 전체 구조를 놓쳤다.
막힐 때는 "지금 result에 뭘 저장하고 있나"처럼 기본 질문으로 돌아가는 것이 효과적이다.

---

> 이 문제의 핵심은 **H-Index의 정의를 `min(인용횟수, 편수)`로 수학적으로 재해석**하는 것이다.
> 정렬 후 각 index에서 두 값의 최솟값을 구하고, 전체 최댓값을 반환하면 깔끔하게 풀린다.