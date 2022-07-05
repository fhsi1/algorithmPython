n, k = map(int, input().split())
score = list(map(int, input().split()))
num = score[k - 1]
result = 0

for i in score:
    if i >= num and i > 0:
        result += 1

print(result)