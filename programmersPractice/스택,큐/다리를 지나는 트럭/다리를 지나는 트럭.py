# 해결 방법: bridge_length만큼의 큐(리스트)를 만들어 초가 지날 때마다
# 현재 weight가 sum(bridge_length_queue) + truck_weights[0]보다 크면
# bridge_length_queue.append(truck_weights.popleft())해서 넣고
# 아니면 0(아무것도 없음) 넣기
# 반복문이 1회차 끝나면 시간 1 경과

from collections import deque

def solution(bridge_length, weight, truck_weights):

    truck_weights = deque(truck_weights)

    bridge_length_queue = deque()
    for i in range(bridge_length):
        bridge_length_queue.append(0)

    time = 0
    current_weight = 0

    # bridge_length_queue에 값이 들어가 있을 때도 돌아가게끔 해야 함(다리에만 남아있을 때도 가정)
    # truck_weights가 비면 False, 아니면 True
    while current_weight or truck_weights:
        # 다리에서 빠지는 무게 current_weight에서 빼기
        current_weight -= bridge_length_queue[0]
        bridge_length_queue.popleft()
        # truck_weights가 있을 때만 if문에 들어가게끔 함(오른쪽 인덱스 참조 때문에)
        # 현재 문제: sum(bridge_length_queue)를 두 번, 매 루프마다 호출하면 무거워진다. 모든 수가 루프 한 번에 전체 호출됨
        # 개별의 변수(current_weight)로 전체 무게를 추적하면 됨
        if truck_weights and weight >= current_weight + truck_weights[0]:
            current_weight += truck_weights[0]
            bridge_length_queue.append(truck_weights.popleft())
        else:
            bridge_length_queue.append(0)
        time += 1

    return time