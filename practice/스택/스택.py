import sys

l = []
input = sys.stdin.readline
N = int(input().strip())

length = 0
for i in range(N):
  S = input().strip()
  if S[0:4] == "push":
    l.append(int(S[5:len(S)]))
    length += 1
  elif S[0:3] == 'pop':
    if length == 0:
      print(-1)
    else:
      print(l[length-1])
      l.pop()
      length -= 1
  elif S[0:4] == 'size':
    print(length)
  elif S[0:5] == 'empty':
    if length == 0:
      print(1)
    else:
      print(0)
  elif S[0:3] == 'top':
    if length == 0:
      print(-1)
    else:
      print(l[length-1])