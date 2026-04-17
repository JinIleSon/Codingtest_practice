from collections import Counter

def solution(participant, completion):
    
    # Counter로 만든 뒤 빼면 value 개수가 0인 게 key로서 사라짐.
    # 즉 1인 Counter만 남음
    return list((Counter(participant) - Counter(completion)).keys())[0]
    
    # 아래처럼 하나씩 셀 수도 있지만, Counter를 import하여 리스트를 바로 딕셔너리 형태로 바꿀 수 있음
    
    # 중복에 대해 쉽게 접근을 위해 해시(딕셔너리) 사용
    # pDict = {}
    
    # for i in range(len(participant)):
    #     pDict[participant[i]] = pDict.get(participant[i], 0) + 1
    # for i in range(len(completion)):
    #     pDict[completion[i]] = pDict.get(completion[i], 0) - 1
    
    # answer = ''
    # 아래는 for문으로 key, value를 가져올 때 자주 쓰이니 외울 것
    # for key, value in pDict.items():
    #     if value == 1:
    #         answer = key
            
    # return answer