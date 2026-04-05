def solution(enemy_power):
    result = []

    for k in range(1, len(enemy_power) + 1):
        enemies = sorted(enemy_power)[:k]

        positives = sorted([e for e in enemies if e >= 0])               # 작은 것부터
        negatives = sorted([e for e in enemies if e < 0], reverse=True)  # 절댓값 작은 것부터
        order = positives + negatives

        start = 1    # 가능한 최솟값 1부터 시작, 조건 불만족 시 올림
        gained = 0   # 지금까지 잡은 적들의 전투력 합

        for e in order:
            current_power = start + gained  # 잡기 직전 내 전투력

            # 조건1: 적을 이길 수 있냐?
            if current_power <= e:
                start += e - current_power + 1

            gained += e                     # 적 잡음
            current_power = start + gained  # 잡고 난 후 내 전투력

            # 조건2: 잡고 나서 살아있냐?
            if current_power < 1:
                start += 1 - current_power

        result.append(start)

    return result