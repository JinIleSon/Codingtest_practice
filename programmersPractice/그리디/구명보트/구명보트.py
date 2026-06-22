# 최대한 적게 사용 -> 그리디 알고리즘

# 오름차순 정렬 후 앞에서부터 2명 짝지어보고 안되면 1명 넣고 출발
# limit의 2명 합했을 때. [0] + [1] > limit면 거기서부터 전부 + 1. 이후부턴 전부 +1 취급

def solution(people, limit):

    count = 0

    people.sort()
    # print(people)

    # 스택? 큐? while문?
    # 2명씩 타는 경우(limit 이하일 때)
    i = 0
    while i+1 < len(people) and people[i] + people[i+1] <= limit:
        print("people[0] =", people[i], "people[1] =", people[i+1])
        count += 1        
        i += 2

    # 초과하는 순간 거기서부터는 1명씩밖에 못 탐
    for j in range(i, len(people)):
        print("people[j] =", people[j])
        count += 1

    return count