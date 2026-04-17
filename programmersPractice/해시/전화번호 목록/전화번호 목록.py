def solution(phone_book):
    # 시간 복잡도 문제 발생
    # 그 이유는 정렬을 했음에도 그 뒤의 모든 거를 보려고 했기 때문임
    # 정렬하면 가장 비슷한 수들이 가장 가까이 옴
    phone_book.sort()
    for i in range(len(phone_book)):
        # 굳이 끝까지 돌 필요 없음. 정렬했다면 그 다음 것만 봐도 충분
        # find() 함수도 사용 가능
        if i+1 < len(phone_book) and phone_book[i+1].startswith(phone_book[i]) == True:
            return False
    return True