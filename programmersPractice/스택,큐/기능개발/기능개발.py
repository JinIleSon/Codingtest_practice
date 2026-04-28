from collections import deque

def solution(progresses, speeds):
    answer = []
    # 앞에서부터 볼 거기 때문에 deque로 사용
    progresses = deque(progresses)
    speeds = deque(speeds)
    while len(progresses) > 0: 
        count = 0
        progresses = deque([ x + y for x, y in zip(progresses, speeds) ])
        # progresses와 speeds 함께 pop해야 함
        while len(progresses) > 0 and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            # 여기서 pop되는 개수 count
            count += 1
        # count가 있을 때만 개수 넣기
        if count:
            answer.append(count)
    return answer