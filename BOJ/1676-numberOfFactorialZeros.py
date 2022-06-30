from math import factorial

n = int(input())
def five_cnt(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt

print(five_cnt(n))