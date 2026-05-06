# 현재 문제: 3개의 테스트에서 런타임 에러가 난다.
# => K에 대해서 맞춰가다 끝이 나지 않는 경우에 무한 반복에 빠지거나 인덱스 오류가 나게 된다.

import heapq

def solution(scoville, K):
    # heapq.heapify는 반환값이 없다.(None)
    heapq.heapify(scoville)

    count = 0

    while scoville[0] < K:
        # while문 진입 시 heappop하기 전에 길이가 1개일 때 바로 -1 리턴 해야 함
        if len(scoville) == 1:
            return -1
        n1 = heapq.heappop(scoville)
        n2 = heapq.heappop(scoville)
        result = n1 + (n2 * 2)
        heapq.heappush(scoville, result)
        count += 1

    return count