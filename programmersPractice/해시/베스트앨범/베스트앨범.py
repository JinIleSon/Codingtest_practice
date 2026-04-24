genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

songDict = {}

for i in range(len(genres)):
    # 해당 장르에 대해 리스트 넣기(장르가 없다면)
    if songDict.get(genres[i], 0) == 0:
        # 배운 점: list() 함수는 해당 값을 순회가능할 때(iterable)만 사용 가능하다. 숫자는 불가.
        # 따라서 []는 그 자체의 값을 리스트화 하기 때문에 이걸 사용하자.
        songDict[genres[i]] = songDict.get(genres[i], [plays[i]])
        print(songDict)
    # 장르 있으면 해당 리스트에 append 함수
    else:
        # 배운 점: append() 함수는 None을 반환하기 때문에 =으로 받아서는 안 된다.
        songDict.get(genres[i], 0).append(plays[i])
print(songDict)