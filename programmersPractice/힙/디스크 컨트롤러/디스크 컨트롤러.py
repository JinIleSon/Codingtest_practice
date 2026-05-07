# 힙을 사용해야 하는 이유?
# jobs를 한 번만 정렬했을 때는 요청 시각이 먼저 우선순위로 분류되어 있는데
# 대기 큐에 넣을 때는 요청 시각이 먼저가 아닌, 소요시간이 우선순위로 먼저 고려되기 때문에
# 힙을 사용해서 동적으로, 실시간적으로 최솟값만을 뽑아내야 한다.

# 문제에서 주어지는 jobs는 [요청 시각, 소요시간]이므로 '현재위치'만 알면 된다.
# 얻어내야 하는 return은 (현재위치) - (요청 시각) + (소요시간)의 평균임
# 따라서 작업이 시작될 때의 '현재위치'만 구하면 됨 => (현재위치, 요청 시각, 소요시간)이라는 튜플로 구성

# '대기 큐'에 번호, 요청 시각, 소요시간이 들어옴
# 소요시간, 요청 시각, 번호가 낮은 순으로 대기 큐(힙)을 구성해야 함(실시간성이 강함)

# while 문을 도는데, jobs가 다 사라질 때까지 돌 것.
# 현재위치(시간)에 오면 대기 큐에 담고, 만약 실행하느라 시간이 넘어갔다면 그 때 아직 담지못한 jobs들은 while문으로 함께 담기

from collections import deque
import heapq

def solution(jobs):
    # jobs들의 요청 시각 정렬이 필요할 것임(문제에서 요청 시각에 대한 순서를 보장하지 않음)
    jobs = sorted(jobs, key=lambda x: (x[0], x[1]))

    # [요청 시각, 소요시간]에서 [소요시간, 요청 시각]으로 바꿔야 함
    # 리스트 내부의 값들의 요소들을 역순으로 하는 법
    # jobs = [x[::-1] for x in jobs]

    # 리스트 내부의 값들이 3개 이상일 때 요소 하나하나 위치 조정하는 법
    jobs = [[x[1], x[0]] for x in jobs]

    jobs = deque(jobs)
    print("jobs:", jobs)

    # 대기 큐(힙)
    waitQueue = []
    heapq.heapify(waitQueue)
    
    # 현재 위치(시간)
    currentTime = 0

    # 결과를 담을 변수
    result = 0

    i = 0
    # jobs나 waitQueue가 남아있는 경우 반복
    while jobs or waitQueue:

        # 현재위치(시각)이 jobs에 남아있는 요청 시각보다 작은 경우에 대기 큐에 계속 넣음
        while jobs and currentTime >= jobs[0][1]:
            
            # waitQueue에 넣을 요소를 popleft하면서 각각 꺼냄
            job = jobs.popleft()

            # 개별 요소를 각각 넣어 튜플 형식으로 변경함. tuple() 함수는 arg가 하나밖에 들어가지 않고,
            # ()로만 묶어 개별 요소들을 튜플 형식으로 다시 묶을 수 있다.
            # 내부 요소가 튜플이면 앞 요소부터 오름차순으로 낮은 것부터 차례로 알아서 정렬됨
            heapq.heappush(waitQueue, (job[0], job[1], i))
            
            # 아래처럼 heappush를 일반 append처럼 사용하면 안됨
            # waitQueue.heappush((job[0], job[1], i))
            
            # print("waitQueue:",waitQueue)

            i += 1
        
        # heappush한 데이터들은 [0]에 접근할 때 항상 최솟값임
        if waitQueue and currentTime >= waitQueue[0][1]:
            # print("waitQueue[0][0]:", waitQueue[0][0])
            # print("waitQueue[0][1]:", waitQueue[0][1])
            # 현재위치를 얻어냈으면 결과를 담음
            # result += result + a가 아니라 result += a와 result = result + a와 같음
            result += currentTime - waitQueue[0][1] + waitQueue[0][0]

            # print("result:", result)
            # 현재위치를 완료된 작업만큼 더함
            currentTime += waitQueue[0][0]

            # print("currentTime:", currentTime)

            # 완료된 큐를 pop시킴.
            # 여기서 heappop은 heap 내부의 최솟값만 뽑아냄(힙을 써야하는 이유)
            # deque랑 heap은 함께 사용 불가
            # heappush로 형태를 잡고 넣어야 heappop으로 뽑아낼 수 있음
            if waitQueue:
                heapq.heappop(waitQueue)
            
            # print("진행된 currentTime:", currentTime)
            # print("남은 waitQueue:", waitQueue)
            # print("남은 jobs:", jobs)
    
        # 대기 큐에 남아있는 작업이 없을 경우 현재위치(시간)을 1증가
        # 아직 넣지 않은 jobs들이 currentTime(현재 시간)과 요청시각이 맞물릴 경우 currentTime += 1 적용하지 않기
        if not waitQueue and jobs and currentTime < jobs[0][1]:
            currentTime += 1
    # print("끝난 i:", i)
    return result // i
print(solution([[0, 3], [1, 9], [3, 5]]))