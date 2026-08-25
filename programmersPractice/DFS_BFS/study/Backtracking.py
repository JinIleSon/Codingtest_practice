nums = [1, 2, 3]
result = []

def backtracking(nums, path, visited, result):
    if len(nums) == len(path): # 조건
        result.append(path[:])
        return
    
    for num in nums:
        if num not in visited: # visited가 set이므로 빠름
            # 1. 선택
            visited.add(num)
            path.append(num)
            
            # 2. 재귀
            backtracking(nums, path, visited, result)
            
            # 3. 취소
            visited.remove(num)
            path.pop()

backtrack(nums, [], set(), result)