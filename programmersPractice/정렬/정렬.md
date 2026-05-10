# Programmers 42748 — K번째수

[![Level 1](https://img.shields.io/badge/난이도-Level%201-green)](https://school.programmers.co.kr/learn/courses/30/lessons/42748)
[![분류](https://img.shields.io/badge/분류-정렬-blue)](#)

> 배열을 특정 구간으로 자르고 정렬했을 때, k번째 원소를 구하는 문제.

🔗 [문제 보기](https://school.programmers.co.kr/learn/courses/30/lessons/42748)

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

배열 `array`의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구한다.
`commands`의 모든 원소 `[i, j, k]`에 대해 연산을 수행한 결과를 배열로 반환한다.

| array | commands | return |
|-------|----------|--------|
| `[1, 5, 2, 6, 3, 7, 4]` | `[[2, 5, 3], [4, 4, 1], [1, 7, 3]]` | `[5, 6, 3]` |

---

## 입출력

**입력**
- `array` : 길이 1 이상 100 이하, 각 원소 1 이상 100 이하
- `commands` : 길이 1 이상 50 이하, 각 원소는 길이 3인 배열 `[i, j, k]`

**출력**
- 각 command에 대한 k번째 수를 담은 배열

---

## 헷갈렸던 부분

**전체를 미리 정렬하면 안 된다**

처음에는 `array` 전체를 먼저 정렬해두고 시간복잡도를 줄이려 했다.
하지만 정렬 전 원본 배열을 기준으로 구간을 잘라야 하므로, 미리 정렬하면 인덱스 기준 자체가 틀어진다.
결국 **구간을 먼저 자르고, 그 부분만 정렬**하는 방식으로 접근해야 한다.

---

## 풀이 접근

### 핵심 아이디어 — 구간 슬라이싱 후 부분 정렬

각 command마다 독립적으로 슬라이싱 → 정렬 → 인덱스 접근을 수행한다.

```
핵심 원칙: 전체를 건드리지 않고, 매 command마다 해당 구간만 처리한다.
```

**Step 1.** `commands`를 순회하며 각 `[i, j, k]`를 읽는다.

**Step 2.** `array[i-1:j]`로 해당 구간을 슬라이싱한다. (문제의 i, j는 1-based이므로 `i-1` 보정)

**Step 3.** 슬라이싱된 배열을 `sort()`로 오름차순 정렬한다.

**Step 4.** `k번째` = `[k-1]` 인덱스 접근. (1-based → 0-based 보정)

**Step 5.** 결과를 `result`에 append하고 반환한다.

---

## 최종 코드

```python
def solution(array, commands):
    result = []

    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        slicedStr = array[start:end]
        slicedStr.sort()
        result.append(slicedStr[commands[i][2] - 1])

    return result
```

---

## 복잡도 분석

| 항목 | 복잡도 |
|------|--------|
| 시간 복잡도 | `O(m · n log n)` |
| 공간 복잡도 | `O(n)` |

> `n` = array의 길이 (최대 100), `m` = commands의 길이 (최대 50)

commands를 순회하며 (O(m)), 매 iteration마다 슬라이싱된 구간을 정렬 (O(n log n)).
슬라이싱된 배열을 임시 저장하므로 공간은 O(n).
제한 조건상 n, m이 작아 실질적인 부담은 없다.

---

## 배운 점

**슬라이싱은 원본을 건드리지 않는다**
`array[start:end]`는 새로운 리스트를 반환하므로, `sort()`를 호출해도 원본 `array`는 변하지 않는다.
commands를 여러 번 처리할 때 원본이 유지되는 이유가 여기에 있다.

**1-based 인덱스는 접근할 때마다 보정해야 한다**
문제에서 주어지는 i, j, k는 모두 1-based이므로, 슬라이싱 시작(`i-1`)과 결과 접근(`k-1`) 모두 보정이 필요하다.
슬라이싱 끝 인덱스(`j`)는 Python의 exclusive 특성 덕분에 보정 없이 사용할 수 있다.

---

> 이 문제의 핵심은 **전체 정렬이 아닌 구간 슬라이싱 후 부분 정렬**이다.
> 슬라이싱이 원본을 보존한다는 점과 1-based → 0-based 인덱스 보정을 정확히 처리하면 깔끔하게 풀린다.