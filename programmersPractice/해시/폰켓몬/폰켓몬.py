def solution(nums):
    return min(len(set(nums)), len(nums)//2)
    # 이렇게 비교하는 게 아니라 min()을 쓰면 값 중에 더 작은 값 사용 가능

    # numsSet = set(nums)
    # if len(numsSet) <= len(nums) // 2:
    #     return len(numsSet)
    # else:
    #     return len(nums) // 2