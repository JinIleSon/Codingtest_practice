# 정수를 이어 붙여 만들 수 있는 가장 큰 수?
# 값 내부 수 분리는 안 함
# 정렬이긴 한데, 기준이 특이함(커스텀 정렬)
# sort 함수는 내부 모든 리스트를 순회함.
# 그래서 커스텀 함수를 정의할 때 A와 B가 있으면 어떤 경우에 B가 먼저(A가 더 큼), A가 먼저(B가 더 큼)인지를 판별해야 함

# 특수 기준에 따라 sort하고 위치 조정한 뒤에 그걸 return
# 문자열끼리 비교해도 아스키 코드를 비교하는 것이기 떄문에
# 숫자 두 개를 문자열로 변환한 다음 그걸 이어붙여서 AB < BA인지 >, 0인지 구별

from functools import cmp_to_key

# sort에 사용될 cmp_to_key 내부에는 항상 2개의 인자만 가능함
def compare(a, b):
    # a가 앞에 있는 게 더 큰 경우
    # -1 리턴 시 sort()에는 A, B 그대로 둚
    if str(a) + str(b) > str(b) + str(a):
        return -1
    # b가 앞에 있는 게 더 큰 경우
    # 1 리턴 시 sort()에는 B, A로 바꿈  
    elif str(a) + str(b) < str(b) + str(a):
        return 1
    # 둘이 같다고 표현 될 경우
    # 0 리턴 시 sort()에는 그대로 둚
    else:
        return 0

def solution(numbers):

    numbers.sort(key=cmp_to_key(compare))

    # 예외상황
    # 모두 정렬된 후 맨 앞이 0이면 전체가 0이므로 0 리턴
    if numbers[0] == 0:
        return "0"

    result = ""

    for i in range(len(numbers)):
        result += str(numbers[i])

    return result