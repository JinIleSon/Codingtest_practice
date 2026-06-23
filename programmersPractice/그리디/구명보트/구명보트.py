# 최대한 적게 사용 -> 그리디 알고리즘

# 오름차순 정렬 후 앞에서부터 2명 짝지어보고 안되면 1명 넣고 출발
# limit의 2명 합했을 때. [앞에서부터] + [뒤에서부터] > limit면 거기서부터 전부 + 1. 이후부턴 전부 +1 취급

def solution(people, limit):

    count = 0

    people.sort()
    # print(people)

    # 스택? 큐? while문?
    # 2명씩 타는 경우(limit 이하일 때)
    i = 0
    j = len(people) - 1
    while i+1 < len(people) and i < j:
        # 두 명이 짝지어진 경우(가장 가벼운 + 무거운)
        if people[i] + people[j] <= limit:
            count += 1
            j -= 1
            i += 1
        # 두 명이 안되는 경우(무거운 사람만)
        else:
            count += 1
            j -= 1
    
    if i == j:
        count += 1

    return count