# 아이디어

# prices의 시간을 추적하기 위해 현재 인덱스를 prices 요소들과 함께 튜플로 묶음 - pricesTime
# time이라는 prices와 똑같은 길이의 공간을 만들어 놓고, 현재의 prices에 대해 이전의 것보다 작으면 pop하면서
# 저장해뒀던 '현재 인덱스 - 그 때의 인덱스'를 진행하여 time 리스트 안에 그 때의 인덱스에 저장
# 마지막까지 남아있으면 '마지막 인덱스 - 그 때의 인덱스' 진행. len(prices) - 1 - 그 때의 인덱스

# => 일단 스택에 남아있는 거는 적어도 다음 것보다 작거나 같아야 함.

def solution(prices):
    
    pricesTime = []
    time = []

    # 리턴할 값인 time 리스트에 prices만큼의 길이 추가
    for i in range(len(prices)):
        time.append(0)

    for i in range(len(prices)):
        if i == 0:
            pricesTime.append((i, prices[i]))
            continue
        # i가 0일 때는 굳이 예외처리를 하지 않고도 pricesTime에 값이 있는지만 확인해서 진행
        while pricesTime and prices[i] < pricesTime[-1][1]:
            time[pricesTime[-1][0]] = i - pricesTime[-1][0]
            pricesTime.pop()

        # 배운 점: 현재 위치의 가격 및 시간은 무조건 push해야 한다.
        pricesTime.append((i, prices[i]))

    # 끝까지 남아있는 스택 처리
    for i in range(len(pricesTime)):
        time[pricesTime[i][0]] = len(prices) - 1 - pricesTime[i][0]

    return time