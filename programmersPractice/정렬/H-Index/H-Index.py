def solution(citations):
    citations.sort()

    count = []
    result = []

    for i in range(len(citations), 0, -1):
        count.append(i)
    
    for i in range(len(citations)):
        # 인용 횟수와 논문 편수 중 작은 값을 리스트에 넣음
        result.append(min(citations[i], count[i]))
    
    # 이 중 가장 큰 결과값에 넣음 -> H-Index
    return max(result)

print(solution([3, 4, 0, 6, 1, 5]))