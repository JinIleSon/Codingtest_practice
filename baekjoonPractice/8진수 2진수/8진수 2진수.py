import sys

input = sys.stdin.readline

s = list(input().strip())

for i in range(len(s)):
    if i == 0:
        # 맨 앞자리일 때 0이 왔다면 1자리수이므로 0은 별도 if문으로 처리 안해도 됨
        if s[i] == '0':
            print('0', end='')
        elif s[i] == '1':
            print('1', end='')
        elif s[i] == '2':
            print('10', end='')
        elif s[i] == '3':
            print('11', end='')
        # i = 0일 때 여기에 continue를 적으면 4, 5, 6, 7과 같은 값이 들어가지 않음
    else:
        if s[i] == '0':
            print('000', end='')
        elif s[i] == '1':
            print('001', end='')
        elif s[i] == '2':
            print('010', end='')
        elif s[i] == '3':
            print('011', end='')
    if s[i] == '4':
        print('100', end='')
    if s[i] == '5':
        print('101', end='')
    if s[i] == '6':
        print('110', end='')
    if s[i] == '7':
        print('111', end='')