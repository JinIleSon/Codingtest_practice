# 갈 수 있는 던전은 8개이기 때문에, 최악의 경우에 8!=40,320 밖에 되지 않는다. (백트래킹은 10!~12!까지 가능)
# 컴퓨터에서는 40,320는 작은 값이기 때문에 오히려 완전 탐색이 알맞다.
# 재귀 + 백트래킹 문제다. 이유는 모든 경우를 탐색해야 하는데, 선택을 취소하고 다른 걸 골라야 한다. (원하는 경우로 보기 위해 / 되돌리기 + 모든 경우 탐색)
# 동일한 for문으로 재귀를 진행해도 되는 이유는 visited[i] = 1인 부분은 다시 가지 않을 것이기 때문이다.

def solution(k, dungeons):
    count = 0
    result = 0

    # 방문한 곳을 1, 방문하지 않은 곳을 0으로 표기하기 위한 공간
    visited = []
    for _ in range(len(dungeons)):
        visited.append(0)

    def backtracking(k, count):
        # 변수 읽기나 리스트 변경은 nonlocal 필요 없지만, 변수 변경은 nonlocal 필요
        nonlocal result
        # 백트래킹에서 결과물은 for문 위에 두는 게 관례
        result = max(result, count)

        for i in range(len(dungeons)):
            # 방문하지 않았고 k가 충분하면
            if visited[i] == 0 and k >= dungeons[i][0]:
                visited[i] = 1
                # 재귀
                # 안으로 들어가면 피로도 및 count 변동. 변동되는 값은 별도로 지정하지 않고 인자에 변동사항을 넣고 가는 것이 깔끔함. 복사본으로 하기 때문에 추적이 쉬움(되돌려야 하는 값)
                backtracking(k - dungeons[i][1], count + 1)
                # 재귀로 인자를 넘기면 count를 되돌릴 필요 없음 - count 복사본이 들어갔기 때문
                # 재귀가 끝나면 밖으로 나온거니 count -= 1
                # count -= 1
                visited[i] = 0

    backtracking(k, count)
    return result

print(solution(80, [[80,20],[50,40],[30,10]]))