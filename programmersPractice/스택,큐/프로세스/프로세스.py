# 현재 문제: 현재 위치가 몇번째인지를 정확하게 알아내지 못함
# 튜플 형태로 만들어서 해당 location과 같다면 추적한 실행횟수 count를 바로 리턴하게끔 진행

from collections import deque

def solution(priorities, location):
    tuplePrior = deque()

    # 값과 해당 location 함께 묶어 튜플로 생성
    for i in range(len(priorities)):
        tuplePrior.append((priorities[i], i))

    # 배운 점: 정렬을 사용하면 크기의 순서를 알 수 있다. 즉, 크기의 정도를 알고 싶을 때
    sortPrior = sorted(priorities)

    # [1, 2, 2, 3] 형태(오름차순)
    # print(sortPrior)

    # 실행 카운트 추적
    count = 0

    while tuplePrior:
        if tuplePrior[0][0] != sortPrior[-1]:
            tuplePrior.append(tuplePrior.popleft())
            print(tuplePrior)
        elif tuplePrior[0][0] == sortPrior[-1]:
            count += 1
            if location == tuplePrior[0][1]:
                return count
            tuplePrior.popleft()
            sortPrior.pop()