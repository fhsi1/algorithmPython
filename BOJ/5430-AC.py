import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    deq = deque(arr)

    rev, front, back = 0, 0, len(deq) - 1
    flag = 0
    if n == 0:
        deq = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(deq) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    deq.popleft()
                else:
                    deq.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(deq) + "]")
        else:
            deq.reverse()
            print("[" + ",".join(deq) + "]")