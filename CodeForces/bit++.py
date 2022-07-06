n = int(input())
res = 0

for _ in range(n):
    cmd = input()
    if '++' in cmd:
        res += 1
    else:
        res -= 1

print(res)