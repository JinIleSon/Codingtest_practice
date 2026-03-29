import sys

input = sys.stdin.readline

n = int(input().strip())

result = 1

if n >= 2:
    for i in range(2, n+1):
        result *= i
else:
    if n == 0:
        result = 1
    else:
        result = 1
print(result)