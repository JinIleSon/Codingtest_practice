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
        i += 1

    n = len(name)
    # 오른쪽으로만 갔을 때 n - 1
    move = n - 1
    # 오른쪽으로만 가는 방법, non-A를 기점으로 하여 반대편으로 꺾는 방법 (오 -> 왼 / 왼 -> 오) 
    for i in range(n):
        next = i + 1
        while n > next and name[next] == 'A':
            next += 1

        # n - 1 - next가 아니라 n - next인 이유는 wrap하는 것도 개수에 포함되기 때문
        # 오른쪽 갔다가 왼쪽으로 간 후 wrap 후 오른쪽에서 왼쪽으로 이동
        move = min(move, i * 2 + (n - next))
        # 왼쪽 갔다가(wrap) 오른쪽에서 왼쪽 쭉 갔다가 다시 오른쪽으로 돌아가서 wrap 후 왼쪽에서 오른쪽으로 이동(i까지)  
        move = min(move, (n - next) * 2 + i)

    count += move

    return count