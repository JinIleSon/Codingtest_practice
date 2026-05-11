def solution(answers):
    # 1부터 5까지 계속 순회
    # first = [1, 2, 3, 4, 5, 1, 2, ...]
    
    # 2를 중간에 계속 넣고 2는 스킵하고 1 3 4 5 반복
    # second = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, ...]

    # 3311224455 반복 - 3을 2개 먼저 내고 나머지는 순차적으로 2개씩 올림
    # third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...]

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    firstLen = len(first)
    secondLen = len(second)
    thirdLen = len(third)

    countFirst = 0
    countSecond = 0
    countThird = 0

    for i in range(len(answers)):
        if i >= firstLen:
            firstIndex = i % firstLen
        else:
            firstIndex = i
        if i >= secondLen:
            secondIndex = i % secondLen
        else:
            secondIndex = i
        if i >= thirdLen:
            thirdIndex = i % thirdLen
        else:
            thirdIndex = i
        
        if first[firstIndex] == answers[i]:
            countFirst += 1
        if second[secondIndex] == answers[i]:
            countSecond += 1
        if third[thirdIndex] == answers[i]:
            countThird += 1

    sorting = [(countFirst, 1), (countSecond, 2), (countThird, 3)]
    sorting.sort(key=lambda x:x[0])

    result = [sorting[2][1]]

    if sorting[2][0] == sorting[1][0]:
        result.append(sorting[1][1])
    
    if sorting[2][0] == sorting[0][0]:
        result.append(sorting[0][1])

    result.sort()

    return result