# 그대로인 버전
# -5134 -10 0 1 100 -> 최솟값은 -5134

# 마이너스 붙인 버전
# -100 -1 0 10 5134 -> 최댓값은 (-)100

### 음수인 것만 있을 때와 양수인 것만 있을 때의 최솟값/최댓값은 어떻게 분리할 것인가?

# => 굳이 음수, 양수를 나눠서 생각할 필요가 없었던 것임

# I 숫자면 최솟값 힙, 최댓값 힙에 넣고
# 원하는 값을 계속해서 뽑아내면 됨

# 빈 큐에 데이터 삭제 연산이 주어지면, 그 연산은 무시
# 모든 연산 후 큐가 비어있으면 [0,0] return
# 비어있지 않으면 [최댓값,최솟값] return

import heapq
from collections import deque
from collections import defaultdict

def solution(operations):
    operations = deque(operations)

    # defaultdict는 없는 키에 대해서 +1 연산같이 해도 그 값이 반영됨(오류 x)
    rDict = defaultdict(int)

    # 빈 리스트는 굳이 heapq.heapify() 안 해도 됨
    minHeap = []
    maxHeap = []

    # I 숫자가 들어오면 해당 숫자를 minHeap, maxHeap에 넣어줌
    while operations:

        if operations[0][0] == "I":
            # print("operations 16?:", type(int(operations[0][2:])))
            heapq.heappush(minHeap, int(operations[0][2:]))
            heapq.heappush(maxHeap, -int(operations[0][2:]))
            operations.popleft()
        
        elif operations[0] == "D -1":
            # 힙에 아무것도 없으면 넘어가기(operations에 있는 건 pop)
            if not minHeap:
                operations.popleft()
                continue
            
            # 힙에 값이 존재하면
            # rDict에서 minHeap[0] 값이 있는 경우(1 이상)
            while minHeap and rDict[minHeap[0]] > 0:
                rDict[minHeap[0]] -= 1
                heapq.heappop(minHeap)
                
            # 일반적인 처리. rDict에 등록
            # minHeap이 유령값으로 인해 전부 pop되었을 경우를 위해 minHeap이 있는 경우만 계산하도록 예외처리
            if minHeap:
                rDict[minHeap[0]] += 1
                heapq.heappop(minHeap)
                operations.popleft()
            # minHeap이 비어있으면 pop할 게 없으니 operations만 pop 후 다음으로
            else:
                # print("D 1 rDict:", rDict)
                # print("D 1 minHeap:", minHeap)
                # print("D 1 maxHeap:", maxHeap)
                operations.popleft()

        elif operations[0] == "D 1":
            # 힙에 아무것도 없으면 넘어가기(operations에 있는 건 pop)
            if not maxHeap:
                operations.popleft()
                continue
            # 힙에 값이 존재하면
            # rDict에서 maxHeap[0]에 -를 붙인 값이 있는 경우(1 이상)
            while maxHeap and rDict[-maxHeap[0]] > 0:
                rDict[-maxHeap[0]] -= 1
                heapq.heappop(maxHeap)
            
            # 일반적인 처리. rDict에 등록
            # maxHeap이 유령값으로 인해 전부 pop되었을 경우를 위해 maxHeap이 있는 경우만 계산하도록 예외처리
            if maxHeap:
                rDict[-maxHeap[0]] += 1
                heapq.heappop(maxHeap)
                operations.popleft()
            # maxHeap이 비어있으면 pop할 게 없으니 operations만 pop 후 다음으로
            else:
                operations.popleft()

        # print("rDict:", rDict)
        # print("minHeap:", minHeap)
        # print("maxHeap:", maxHeap)
        # print("남은 operations:", operations)

    # 남아있는 유령값 비우기(중간이 실제값이어서 비워지지 않으면 그게 최솟값, 최댓값)
    # 한 쪽에만 유령값이 남아있겠지만, 어느 쪽인지 모르므로 전체 청소
    while minHeap and rDict[minHeap[0]] > 0:
        rDict[minHeap[0]] -= 1
        heapq.heappop(minHeap)
    
    while maxHeap and rDict[-maxHeap[0]] > 0:
        rDict[-maxHeap[0]] -= 1
        heapq.heappop(maxHeap)

    # print("남은 rDict:", rDict)
    # print("남은 minHeap:", minHeap)
    # print("남은 maxHeap:", maxHeap)

    if not minHeap and not maxHeap:
        return [0, 0]
    # 완전히 삭제가 되지 않아 한 쪽에 몰려있을 경우
    if not minHeap and maxHeap:
        return [-maxHeap[0], -maxHeap[0]]
    # 완전히 삭제가 되지 않아 한 쪽에 몰려있을 경우
    if minHeap and not maxHeap:
        return [minHeap[0], minHeap[0]]
    if minHeap and maxHeap:
        return [-maxHeap[0], minHeap[0]]

print(solution(["I 1", "I 1", "I 1", "D 1", "D -1"]))
