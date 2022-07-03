n, k = map(int, input().split())
coinList = list()
for i in range(n):
	coinList.append(int(input()))
cnt = 0
for i in reversed(range(n)):
	cnt += k // coinList[i]
	k = k % coinList[i]
print(cnt)