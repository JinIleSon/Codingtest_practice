# 고쳐야 할 부분: 노래는 횟수가 겹칠 수 있어 (노래횟수, 인덱스) 형태의 튜플로 항상 가지고 다녀야 한다.

def solution(genres, plays):
    songDict = {}

    for i in range(len(genres)):
        # 해당 장르에 대해 리스트 넣기(장르가 없다면)
        if songDict.get(genres[i], 0) == 0:
            # 배운 점: list() 함수는 해당 값을 순회가능할 때(iterable)만 사용 가능하다. 숫자는 불가.
            # 따라서 []는 그 자체의 값을 리스트화 하기 때문에 이걸 사용하자.
            songDict[genres[i]] = songDict.get(genres[i], [plays[i]])
        # 장르 있으면 해당 리스트에 append 함수
        else:
            # 배운 점: append() 함수는 None을 반환하기 때문에 =으로 받아서는 안 된다.
            songDict.get(genres[i], 0).append(plays[i])

    # sum한 딕셔너리를 만듦
    sumDict = {}

    # 노래 딕셔너리 내 큰 순 정렬
    for key, value in songDict.items():
        songDict[key].sort(reverse=True)
        # sum한 딕셔너리 값 넣기
        sumDict[key] = sum(value)

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

    # 장르 1개
    if len(sumDict) == 1:
        # 장르 1개, 노래 1개
        if len(songDict[0]) == 1:
            answer.append(0)
        # 장르 1개, 노래 2개 이상
        else:
            answer.append(plays.index(songDict[0][0]))
            answer.append(plays.index(songDict[0][1]))
        return answer

    # 장르 2개 이상
    else:
        for i in range(2):
            # 첫 번째로 큰 장르
            if i == 0:
                max1 = sumDict[0]
            # 두 번째로 큰 장르
            else:
                max2 = sumDict[1]

        # 첫 번째로 큰 장르 + 첫 번째 노래
        if len(songDict[max1]) == 1:
            answer.append(plays.index(songDict[max1][0]))

        # 첫 번째로 큰 장르 + 두 번째 노래    
        elif len(songDict[max1]) >= 2:
            answer.append(plays.index(songDict[max1][0]))
            answer.append(plays.index(songDict[max1][1]))

        # 두 번째로 큰 장르 + 첫 번째 노래    
        if len(songDict[max2]) == 1:
            answer.append(plays.index(songDict[max2][0]))
        
        # 두 번째로 큰 장르 + 두 번째 노래
        elif len(songDict[max2]) >= 2:
            answer.append(plays.index(songDict[max2][0]))
            answer.append(plays.index(songDict[max2][1]))

        return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))