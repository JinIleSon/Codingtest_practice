# 정렬을 모두 하고 시작하는 것이 아닌,
# 해당 부분만 자르고 그 부분만 정렬하는 것

def solution(array, commands):
    result = []

    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        slicedStr = array[start:end]
        slicedStr.sort()
        result.append(slicedStr[commands[i][2] - 1])

    return result