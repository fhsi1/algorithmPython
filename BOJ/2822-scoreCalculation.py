score = []
res = []
maxi = 0
for i in range(8):
    score.append(int(input()))

for i in range(5):
    res.append(score.index(max(score))+1)
    maxi += score[score.index(max(score))]
    score[score.index(max(score))] = 0
res.sort()
print(maxi)

for i in res:
    print(i, end=" ")