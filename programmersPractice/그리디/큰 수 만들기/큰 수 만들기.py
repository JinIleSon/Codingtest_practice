# top과 현재 것을 계속 비교 -> 스택
# top보다 현재 것이 크면, k가 0보다 클 때 top을 pop, k-=1
# top보다 현재 것이 작으면 push

# 예외: k가 현재 남은 것보다 1

def solution(number, k):

    result = []

    for i in range(len(number)):
        while len(result) > 0 and result[-1] < number[i] and k > 0:
            result.pop()
            k -= 1
        if len(result) == 0 or result[-1] >= number[i] or k == 0:
            result.append(number[i])
    
    # 예외: 다 끝났는데도 k가 남아있다면 k만큼 다 pop
    for _ in range(k):
        result.pop()

    return ''.join(result)