# ⚔️ 용사의 최소 전투력

> **유형**: Greedy + Simulation  
> **난이도**: 실버 2 ~ 골드 5  
> **핵심 알고리즘**: 탐욕법 + 순서 결정 + 누적 조건 관리

---

## 📋 문제 설명

적을 잡는 용사가 있다. 용사의 전투력이 적의 전투력보다 **커야만** 잡을 수 있으며,  
적을 잡으면 적의 전투력이 **내 전투력에 합산**된다. (음수면 감소)

`enemy_power` 리스트가 주어질 때, 적을 **1명, 2명, 3명 ... N명** 잡기 위한  
**최소 시작 전투력**을 각각 구하여 리스트로 반환하라.

- 전투력은 적을 잡은 **후에도 항상 1 이상**을 유지해야 한다
- 적의 전투력은 **음수, 양수 모두 가능**
- 잡는 **순서는 자유롭게** 결정 가능
- 시작 전투력은 **정수**

---

## 💡 핵심 아이디어

### 1. 핵심 변수 3가지

```
start         = 시작 전투력 (우리가 구하는 답)
gained        = 지금까지 잡은 적들의 전투력 합
current_power = start + gained (현재 내 전투력)
```

> `gained`는 잡은 적들의 합이라 **내가 바꿀 수 없다.**  
> 전투력을 올리려면 **start를 올리는 수밖에 없다.**
>
> 비유하자면, `start`는 월급이고 `gained`는 고정 알바비다.  
> 총 수입을 올리고 싶으면 알바비는 고정이니 **월급(start)을 올려야 한다.**

### 2. 최적 순서 (Greedy)

**양수 적 먼저, 음수 적 나중에**

```
양수 적: 작은 값부터  →  전투력 조건 만족하면서 누적
음수 적: 절댓값 작은 것부터  →  -1, -3, -5 순서로 조금씩 깎이게
```

> 양수 적을 먼저 잡아 전투력을 키운 뒤 음수 적을 감당해야  
> 최소 시작 전투력으로 버틸 수 있다.

### 3. 체크해야 할 두 가지 조건

매 적마다 **두 가지 상황**이 독립적으로 발생할 수 있다.

```
조건1 (잡기 전): current_power > e 이어야 함
→ 만족 못하면 start를 올려서 이길 수 있게

조건2 (잡은 후): current_power >= 1 이어야 함
→ 만족 못하면 start를 올려서 1 이상 유지
```

```
조건1은 양수 적에서 주로 발동  →  나보다 강한 적을 못 이기는 경우
조건2는 음수 적에서 주로 발동  →  이기긴 하지만 잡고 나면 전투력이 깎이는 경우
```

> 두 조건은 독립적이다. 조건1을 통과해도 조건2에서 실패할 수 있다.

---

## 📝 최종 코드

```python
def solution(enemy_power):
    result = []

    for k in range(1, len(enemy_power) + 1):
        enemies = sorted(enemy_power)[:k]

        positives = sorted([e for e in enemies if e >= 0])               # 작은 것부터
        negatives = sorted([e for e in enemies if e < 0], reverse=True)  # 절댓값 작은 것부터
        order = positives + negatives

        start = 1    # 가능한 최솟값 1부터 시작, 조건 불만족 시 올림
        gained = 0   # 지금까지 잡은 적들의 전투력 합

        for e in order:
            current_power = start + gained  # 잡기 직전 내 전투력

            # 조건1: 적을 이길 수 있냐?
            if current_power <= e:
                start += e - current_power + 1

            gained += e                     # 적 잡음
            current_power = start + gained  # 잡고 난 후 내 전투력

            # 조건2: 잡고 나서 살아있냐?
            if current_power < 1:
                start += 1 - current_power

        result.append(start)

    return result
```

---

## ⏱️ 시간 복잡도

| 단계 | 복잡도 |
|------|--------|
| 정렬 | O(N log N) |
| 전체 시뮬레이션 | O(N²) |
| **최종** | **O(N²)** |

---

## 🔍 예시

### 입력
```python
enemy_power = [-5, -3, 2]
```

### k=3 풀이 과정

**최적 순서: `[2, -3, -5]`** (양수 먼저, 음수는 절댓값 작은 것부터)

```
start=1, gained=0

── 2 잡기 ──
current_power = 1 + 0 = 1
조건1: 1 <= 2 → start += 2 - 1 + 1 = 2 → start = 3
gained = 0 + 2 = 2
current_power = 3 + 2 = 5
조건2: 5 >= 1 ✅

── -3 잡기 ──
current_power = 3 + 2 = 5
조건1: 5 > -3 ✅ (start 그대로)
gained = 2 + (-3) = -1
current_power = 3 + (-1) = 2
조건2: 2 >= 1 ✅

── -5 잡기 ──
current_power = 3 + (-1) = 2
조건1: 2 > -5 ✅ (start 그대로)
gained = -1 + (-5) = -6
current_power = 3 + (-6) = -3
조건2: -3 < 1 ❌ → start += 1 - (-3) = 4 → start = 7
```

### 검증 (start=7)

```
시작: 7
2  잡기: 7 > 2  ✅ → 7 + 2  = 9  (>= 1 ✅)
-3 잡기: 9 > -3 ✅ → 9 - 3  = 6  (>= 1 ✅)
-5 잡기: 6 > -5 ✅ → 6 - 5  = 1  (>= 1 ✅)
```

### 출력
```python
solution([-5, -3, 2])  # [1, 1, 7]
```

---

## 🔗 관련 문제

| 문제 | 난이도 | 비고 |
|------|--------|------|
| [BOJ 1946 - 신입 사원](https://www.acmicpc.net/problem/1946) | 실버 1 | Greedy 정렬 기본 |
| [BOJ 1041 - 주사위](https://www.acmicpc.net/problem/1041) | 실버 2 | 조건 분리 사고 |
| [BOJ 1781 - 컵라면](https://www.acmicpc.net/problem/1781) | 골드 2 | Greedy + 누적 조건 |
| [BOJ 2585 - 경비원](https://www.acmicpc.net/problem/2585) | 골드 5 | 조건 시뮬레이션 |

---

## 📌 유형 인식 팁

> **"순서를 내가 정할 수 있고, 매 순간 조건을 유지해야 한다"** → Greedy + 조건 시뮬레이션 의심  
> **"잡기 전 조건"과 "잡은 후 조건"이 따로 존재한다** → 두 조건을 독립적으로 체크