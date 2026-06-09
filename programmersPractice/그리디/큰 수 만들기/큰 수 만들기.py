def solution(number, k):
    
    lenN = len(number)
    maxN = 0
    text = ""

    i = 0
    detectRange = lenN - k
    maxIndex = -1 # 인덱스 0부터 시작하도록 하기 위함
    while detectRange > 0:

        # 마지막 인덱스가 가장 큰 수였다면, maxIndex를 계속 고정 시킨다면 무한루프 가능성 있음
        # 따라서 골랐다면 그 다음 인덱스부터 보도록 하게 하면 됨
        j = maxIndex + 1
        maxN = 0

        # lenN -k -1 +i 같은 식의 경우는 직접 시작 인덱스, 끝 인덱스를 구해보면서 진행해야 함 - 이게 아님. 다른 테스트케이스에도 적용시켜봐야 함. 틀렸음
        # k + i를 범위로 넣으면 정확하게 작동함
        while j <= k + i:
            if maxN < int(number[j]):
                maxN = int(number[j])
                maxIndex = j
            
            j += 1

        text += str(maxN)
        i += 1
        detectRange -= 1

    return text