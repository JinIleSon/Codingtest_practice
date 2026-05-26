# 매 알파벳마다 처음(A)부터 위치조정
# 앞에서부터 이동하는 게 이득이면 위쪽 방향
# 뒤에서부터 이동하는 게 이득이면 아래쪽 방향
# 오른쪽 커서로 이동하는 게 바꿔야하는 거에 대해 도달하는 횟수가 더 적으면 오른쪽
# 왼쪽 커서로 이동하는 게 도달하는 횟수가 더 적으면 왼쪽

# 알파벳으로 비교해도 될 거 같음 - ASCII CODE

# A / BCDEFGHIJKLM / NOPQRSTUVWXYZ - 25개 이동 가능 = 12개 / 13개로 나눠서 이 사이에 있으면 넣기
# 커서는 A가 아닌 게 있는 위치가 오른쪽으로 몇 칸, 왼쪽으로 갔을 때 몇 칸인지 계산해서 더 작은 걸로

def solution(name):
    count = 0

    answer = []
    nameList = []
    for i in range(len(name)):
        nameList.append(name[i])
        answer.append('A')
    
    # 현재 인덱스
    i = 0

    # 이동할 인덱스(i1은 오른쪽, i2는 왼쪽)
    i1 = 0
    i2 = 0
    while nameList != answer:
        # 해당 인덱스가 M이하인 경우 1씩 오른쪽으로 더함(사실상 1더하는 건 왼쪽이랑 동일. 최대 M까지)
        while nameList[i] != answer[i] and nameList[i] <= 'M':
            answer[i] = chr(ord(answer[i]) + 1)
            count += 1
        # 왼쪽으로 내려갈 때 1씩 더함(최대 N까지)
        while nameList[i] != answer[i] and nameList[i] >= 'N':
            # 아스키코드로 접근해서 만약 현재 값이 A일 때 answer를 Z로 다시 옮겨놔야 함(왼쪽 이동처럼)
            if answer[i] == 'A':
                answer[i] = 'Z'
                count += 1
                continue
            answer[i] = chr(ord(answer[i]) - 1)
            count += 1
        
        i1 = i + 1
        i2 = i - 1
        count1 = 1
        count2 = 1
        # 오른쪽으로 이동
        while i1 <= len(nameList) - 1:
            if nameList[i1] != answer[i1] and nameList[i1] != 'A':
                break
            i1 += 1
            count1 += 1
        if i1 == len(nameList) and nameList[len(nameList) - 1] == answer[len(nameList) - 1]:
            count1 = 21
            
        # 왼쪽으로 이동
        while i2 >= -len(nameList):
            if nameList[i2] != answer[i2] and nameList[i2] != 'A':
                break
            i2 -= 1
            count2 += 1
        if i2 == -len(nameList) - 1 and nameList[-len(nameList)] == answer[-len(nameList)]:
            count2 = 21

        print("count1:", count1)
        print("count2:", count2)
        print("i1:", i1)
        print("i2:", i2)

        # 모두 완성된 경우
        if count1 == 21 and count2 == 21:
            break

        # 최소한으로 이동하는 것으로 선택
        if count1 <= count2:
            i = i1
            count += count1
        else:
            i = i2
            count += count2
        
        print("answer:",answer)
        print("i:",i)
        print("count:",count)

    return count