# 고쳐야 할 부분: 노래는 횟수가 겹칠 수 있어 (노래횟수, 인덱스) 형태의 튜플로 항상 가지고 다녀야 한다.
# 남은 문제: 재생수가 똑같을 때 고유 번호가 더 낮은 걸 골라야 하는데, 그걸 고려 안하고 있음
# => 고유 번호 자체는 오름차순으로 정렬하기
# 걸린 부분 - 문제 이해: 장르"별"로 최대 2곡씩 뽑아내야 함. 

def solution(genres, plays):
    songDict = {}

    for i in range(len(genres)):
        # 해당 장르에 대해 리스트 넣기(장르가 없다면)
        # 배운 점: list() 함수는 해당 값을 순회가능할 때(iterable)만 사용 가능하다. 숫자는 불가.
        # 따라서 []는 그 자체의 값을 리스트화 한다.
        # 배운 점: append() 함수는 None을 반환하기 때문에 =으로 받아서는 안 된다.
        # setdefault 함수는 딕셔너리의 해당 키가 없으면 오른쪽 값을 반환. 있으면 그대로 반환.
        songDict.setdefault(genres[i], []).append((plays[i], i))
    
    # sum한 딕셔너리를 만듦
    sumDict = {}

    # 노래 딕셔너리 내 큰 순 정렬
    for key, value in songDict.items():
        # 키 내부의 value들만 sort - 내림차순
        # 튜플끼리의 sort는 sort(key=lambda x: x[0])을 관용적으로 많이 쓴다
        # 비교용 튜플을 새로 생성해서 진행한다. 첫번째 인덱스는 내림차순을 사용하기 위해 -를, 기본은 오름차순이니 아무것도 붙이지 않음.
        # 튜플에서는 비교할 때 앞 인덱스가 1순위가 됨
        songDict[key].sort(key=lambda x: (-x[0], x[1]))

        sumValue = 0
        for i in range(len(value)):
            sumValue += value[i][0]
        # sum한 딕셔너리 값 넣기
        sumDict[key] = sumValue

    # sum 딕셔너리 내 큰 순 정렬
    # 배운 점: 리스트는 sort() 함수가 사용 가능하지만, 나머지는 sorted()를 사용해야 함.
    # sorted를 사용하면 단순히 key만 나열하기에 dict()함수를 써서 딕셔너리화시키면서, key로 기준이 되는 나열순서, sumDict.items()는 튜플 형태로 들어온다.
    # sumDict = dict(sorted(sumDict.items(), key=lambda x: x[1], reverse=True))
    
    # sorted(sumDict, reverse=True)로 작성하면 문자열(key) 기준으로 정렬된다.
    # sumDict = sorted(sumDict, reverse=True)

    # x에 sumDict.keys() 하나씩 넣고 sumDict[key]의 숫자값끼리 역순으로 sorted()
    sumDict = sorted(sumDict.keys(), key= lambda x: sumDict[x], reverse=True)

    max1, max2 = '', ''
    answer = []

    # 세트별로 정렬이 됐다고 가정
    # 장르 1개
    if len(sumDict) == 1:
        # 장르 1개, 노래 1개
        if len(songDict[sumDict[0]]) == 1:
            answer.append(songDict[sumDict[0]][0][1])
        # 장르 1개, 노래 2개 이상
        else:
            # songDict에 있는 인덱스 그 자체를 가져옴
            answer.append(songDict[sumDict[0]][0][1])
            answer.append(songDict[sumDict[0]][1][1])

    # 장르 2개 이상
    # 장르별로 최대 2곡씩 뽑아내야 함.
    else:
        for i in range(len(sumDict)):
            # 한 곡만 있는 장르
            if len(songDict[sumDict[i]]) == 1:
                answer.append(songDict[sumDict[i]][0][1])

            # 두 곡 이상 있는 장르
            elif len(songDict[sumDict[i]]) >= 2:
                answer.append(songDict[sumDict[i]][0][1])
                answer.append(songDict[sumDict[i]][1][1])
                
    return answer