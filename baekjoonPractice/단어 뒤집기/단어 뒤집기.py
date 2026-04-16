import sys

input = sys.stdin.readline
T = int(input().strip())

new_list = []
new_s = ""
length = 0

for i in range(T):
    S = input().strip()
    S_revered = S[::-1]
    new_list = []
    new_s = ""
    length = 0
    for j in S_revered:
        if j == ' ' or length == len(S_revered):
            new_list.append(new_s)
            new_s = ""
            length += 1
        else:
            new_s += j
            length += 1
            if length == len(S_revered):
                new_list.append(new_s)
                new_s = ""
    answer = new_list[::-1]
    for k in range(len(answer)):
        print(answer[k], end=' ')
    print()