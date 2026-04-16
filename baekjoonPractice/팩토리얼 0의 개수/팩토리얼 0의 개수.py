import sys

input = sys.stdin.readline

n = int(input().strip())

result = 1

count = 0

if n >= 2:
    for i in range(2, n+1):
        result *= i
else:
    result = 1

result = str(result)

for i in range(len(result)-1, 0, -1):
    if result[i] == "0":
        count += 1
    else:
        break

print(count)
