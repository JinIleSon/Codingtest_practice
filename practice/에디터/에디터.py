# 구현방식
# 처음에 왼쪽 배열에 모든 값을 다 넣어두고
# L: 커서를 왼쪽으로 한 칸 옮기면 오른쪽 배열로 넘어감
# D: 커서를 오른쪽으로 한 칸 옮기면 왼쪽 배열로 넘어감
# B: 커서 왼쪽 문자 삭제 - l.pop()
# P $: 왼쪽 배열에 문자 추가 - l.append($)
# 이후 왼쪽 배열과 오른쪽 배열(역순)으로 더함

import sys

input = sys.stdin.readline

# 첫 입력 문자열
string = input().strip()

# 커서를 중심으로 좌(l), 우(r)에 들어갈 임시 스택 리스트
l = []

# 왼쪽 배열에 모든 문자열 채우기
for s in string:
    l.append(s)

r = []

# 입력할 명령어 수
M = int(input().strip())

for i in range(M):
    # 입력한 명령어
    S = input().strip()
    if len(l) > 0 and S == 'L':
        r.append(l.pop())
    elif len(r) > 0 and S == 'D':
        l.append(r.pop())
    elif len(l) > 0 and S == 'B':
        l.pop()
    elif 'P' in S:
        l.append(S[2])

print(''.join(l + r[::-1]))

###################################################################
# 아래 방법은 스택을 사용하지 않고 구현(문자열 슬라이싱으로 인한 시간 초과) #
###################################################################
# import sys

# input = sys.stdin.readline

# # 주어진 문자열
# string = input().strip()

# # 명령어의 개수
# M = int(input().strip())

# # 현재 커서 위치. 인덱스(들어온 문자열의 수)
# C = len(string)

# for i in range(M):
#     # 입력되는 명령어
#     S = input().strip()
#     if C > 0 and S == 'L':
#         C -= 1
#     if not(C == len(string)) and S == 'D':
#         C += 1
#     if C > 0 and S == 'B':
#         string = string[0:C-1] + string[C:len(string)]
#         C -= 1
#     if 'P' in S:
#         string = string[0:C] + S[2] + string[C:len(string)]
#         C += 1
# print(string)