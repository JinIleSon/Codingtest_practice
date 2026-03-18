import sys

input = sys.stdin.readline
n = int(input().strip())

# ps. 등차수열의 식은 n(n-1)/2이다.
# i가 1일 때 (i+1)인 2부터 n까지. (n-1)회 가능
# i가 2일 때 (i+2)인 3부터 n까지. (n-2)회 가능
# 따라서 (n-1) + (n-2) + ... + 1 = n(n-1)/2

print(n*(n-1)//2)
print(2)