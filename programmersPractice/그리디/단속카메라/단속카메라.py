# 적어도 한 번은 단속용 카메라를 만나게 카메라 설치
# 최소 몇 대 필요? <- 그리드
# 힙? 정렬?
# 전체 한 번 정렬 후 마지막 값에 대해서 하나씩 넣어보기?
# 차량 진출 지점에 카메라가 놓여야 적어도 다른 구간에 걸칠 확률이 올라감. 즉 촘촘하게 있는 구간들도 하나씩 두들겨 가볼 수 있음.

def solution(routes):
    count = 0 # 맨 처음 자기자신 포함해서 시작(첫 인덱스)
    length = len(routes)

    routes.sort(key=lambda x: (x[1], x[0]))

    i = 0
    while i < length:
        while i + 1 < length and routes[i][1] >= routes[i + 1][0] and routes[i][1] <= routes[i + 1][1]:
            i += 1
            if (i + 1 < length and not (routes[i][1] >= routes[i + 1][0] and routes[i][1] <= routes[i + 1][1])):
                count += 1
        
        # 다음 구간이 진출 시점에 대해서 해당되지 못하고 나왔을 때    
        count += 1
        i += 1

    return count

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))