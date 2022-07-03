n = int(input())
rope = list()
value = list()
for i in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)
for num in range(n):
    value.append(rope[num]*(num+1))
print(max(value))