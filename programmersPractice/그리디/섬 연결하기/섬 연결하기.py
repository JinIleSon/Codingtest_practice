# 섬 통행 최소 비용 -> 그리디
# 모든 섬을 건너는 경우 -> DFS, but 모든 경우의 수를 여러 경우로 확인해야 함 -> 백트래킹
# 백트래킹 중 min_value 값을 얻으면 됨

def backtracking(nums, path, visited, result):
    if len(nums) == len(path):
        result.append(path[:])
        return

    for num in nums:
        if num not in visited:
            path.append(num)
            visited.add(num)

            backtracking(nums, path, visited, result)

            path.pop()
            visited.remove(num)

# costs에서 인덱스 0, 1만 뽑아서 dict 형태(경로)로 만들고 set(어디가 끝인지 알아야 함)로도 추가
# 이후 min_value = min(backtracking())
# 함수 내부에 함수를 정의하고 사용하면 됨(함수 내부에서 정의 시 set, list는 append, add 등은 사용 가능. 그게 아니라면 nonlocal)
def solution(n, costs):
    path = []
    visited = set()

    def backtracking(n, costs):
        return 0
    
    return 0

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))