def solution(clothes):
    clothesDict = {}
    
    # 종류별 개수만 세면 되니 굳이 중첩 딕셔너리 필요 없음
    for i in range(len(clothes)):
        clothesDict[clothes[i][1]] = clothesDict.get(clothes[i][1], 0) + 1
    # 배운 점: 딕셔너리에서 key-value 할당은 get 함수 필요 없음. 나머지는 필요(읽기와 같은 경우)

    result = 1
    for key, value in clothesDict.items():
        result *= (value + 1)
    result -= 1
    
    return result
