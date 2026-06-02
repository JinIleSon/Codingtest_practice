# 문자열에서 k개 만큼의 숫자를 없애서 해당 수가 가장 크게끔 해야 함
# (숫자, 인덱스)에 관해 오름차순으로 정렬된 리스트를 가지고 삭제 진행
# 최상위 값을 기준으로 가장 가까운 인덱스이면서, 가장 작은 수를 삭제 해야 함

def solution(number, k):
    # k 길이 내부에서 가장 큰 수를 찾아서 앞에 있는 숫자는 다 자르고 그 후 
    # 남은 개수 중에 값이 작은 수, 인덱스 순으로 나열 후 k 개수만큼 삭제

    maxN = []

    for i in range(k):
        maxN.append(number[i])

    maxValue = max(maxN)

    for i in range(k):
        if number[i] == maxValue:
            break
    
    k -= i
    number = number[i:]
    
    # print("k:", k)
    print("number:", number)

    sortNumber = number[1:]
    sortIndexNumber = []

    for i in range(len(sortNumber)):
        sortIndexNumber.append((sortNumber[i], i))

    # 가장 큰 수 + 가장 큰 수 중 첫 인덱스 제외한 수 정렬 필요
    sortIndexNumber.sort(key = lambda x: (x[0], x[1]))

    print("sortIndexNumber:", sortIndexNumber)

    # for i in range()

    return 0
