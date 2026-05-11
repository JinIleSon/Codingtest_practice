# 최댓값 끼리만 가져갔을 때 모든 명함 수납 가능
# 하지만 명함 자체를 가로 세로를 전환시켜 수납도 가능

# 더 큰 수는 항상 오른쪽으로 몰면
# 비교적 작은 수끼리들끼리 가장 큰 수가 나올 것이고
# 오른쪽에는 더 큰 수들끼리만 경쟁하니까 간격이 최소화됨

# sort(key=lambda x: (x[1],x[0]))이면 순서는 그대로지만 x[1]이 우선시 되어 정렬됨
# 순서만 바꾸려면 [[x[1],x[0]] for x in 리스트]

def solution(sizes):
    # 내부 리스트 sort. 
    for item in sizes:
        item.sort()

    max0 = 0
    max1 = 0

    for i in range(len(sizes)):
        if max0 < sizes[i][0]:
            max0 = sizes[i][0]
        if max1 < sizes[i][1]:
            max1 = sizes[i][1]

    return max0 * max1