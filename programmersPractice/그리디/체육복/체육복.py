# 체육복을 적절히 빌려 '최대한 많은' 학생이 체육수업을 들어야 한다. -> 그리디 알고리즘 사용 가능성 多
# 잃어버린 체육복 번호 +- 1인 번호만 빌려 입기 가능

# n = 학생 수
# lost = 도난당한 번호
# reserve = 여벌 번호(여벌 있는 번호가 도난 당할 수도 있음 - 빌려주지 못함(한 개 있다고 취급))

# -> 수업 들을 수 있는 학생 최댓값 구하기

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    # 여벌 번호가 도난 당한 경우 - 빌려주지 못하기 때문에 없애고 시작
    for i in lost[:]:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    # 남은 lost 리스트 순차적으로 reserve 리스트 내 -+1이 되는 값으로 채워줌
    # -1인 것부터 찾음. 작은 수부터 볼수록 이득이 큼(i - 1 먼저 체크 -> i + 1 체크 순서 자체가 그리디 선택)
    # 값 제거에는 remove(값), 인덱스로 접근하려면 pop(인덱스)
    # lost 그 자체를 remove 시키기 때문에 복사본인 lost[:] 형식으로 진행
    for i in lost[:]:
        if i - 1 in reserve:
            lost.remove(i)
            reserve.remove(i - 1)
            continue
        if i + 1 in reserve:
            lost.remove(i)
            reserve.remove(i + 1)
            continue

    return n - len(lost)