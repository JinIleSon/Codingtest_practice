import sys

input = sys.stdin.readline

n = input().strip()

eightList = []

# %나 //가 들어가면 n의 값이 커질수록 기하급수적으로 시간복잡도가 늘어남

i = len(n)

while i > 0:
    # i - 3 == 0이 되는 순간 끝까지 값을 가져오지 못해서 <= 0으로 해야 함
    if i - 3 <= 0:
        # n[0::-1]은 인덱스 0을 가져오고 n[0:0:-1]은 아무것도 가져오지 않음. 차이점을 기억할 것
        eightList.append(n[i-1::-1][::-1])
        break
    # 문자열을 역순으로 만들고자 한다면, 원하는 걸 따와서 [::-1]로 할 것
    eightList.append(n[i-1:i-4:-1][::-1])
    i -= 3
# print(eightList[::-1])

# sort()는 오름차순 및 내림차순을 가지고 정렬하기 때문에 문자열 순서가 원하는대로 정렬되지 않음. '1' > '0'
# eightList.sort(reverse=True)
# print(eightList)
for s in eightList[::-1]:
    if s == '0' or s == '00' or s == '000':
        print(0, end='')
    elif s == '1' or s == '001':
        print(1, end='')
    elif s == '10' or s == '010':
        print(2, end='')
    elif s == '11' or s == '011':
        print(3, end='')
    elif s == '100':
        print(4, end='')
    elif s == '101':
        print(5, end='')
    elif s == '110':
        print(6, end='')
    elif s == '111':
        print(7, end='')