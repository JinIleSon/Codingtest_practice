def solution(s):
    answer = []
    for i in s:
        if i == '(':
            answer.append(i)
        else:
            # 스택에 남은 (가 없으면 False
            if len(answer) == 0:
                return False
            answer.pop()
    # 배운 점: 남은 (가 있어도 정상적으로 닫히지 않은 것 유의하기
    if len(answer) > 0:
        return False
    return True