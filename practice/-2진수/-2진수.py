import sys

input = sys.stdin.readline

# 초점을 항상 나머지가 0 또는 1이 나오도록 해야 함
# 나눠야하는 수가 음수 + 홀수면 -1 더해서 -2로 나누기 진행 => -2로 나누면 나머지는 1이 남음. 예외로 구성



n = int(input().strip())

formation = []

# while n != 1:
#     if n == 0:
#         formation.append(0)
#         break
#     if n % -2 == 


# # 음수 홀수인 경우
# print((-101 +(-1)) // -2)
# print(-101 % -2 * -1)

# # 양수 홀수인 경우
# print((101 + (-1)) // -2)
# print(101 % -2 * -1)

# # 음수 짝수인 경우(일반적 경우)
# print(-100 // -2)
# print(-100 % -2)

# # 양수 짝수인 경우(일반적 경우)
# print(100 // -2)
# print(100 % -2)