# 배운 점: 스택이나 큐는 배열 내 인덱스에 직접 접근이 거의 없다.

def solution(arr):

    answer = []

    while len(arr) > 0:
        # answer에 아무것도 없을 때(빈 리스트는 False임)
        if not answer:
            answer.append(arr.pop())
        # 현재 answer[-1](마지막) 값이 넣었던 값과 동일한 값일 때
        if arr[-1] == answer[-1]:
            arr.pop()
        # 현재 answer[-1](마지막) 값이 넣었던 값과 다른 값일 때
        else:
            answer.append(arr.pop())
    return answer[::-1]